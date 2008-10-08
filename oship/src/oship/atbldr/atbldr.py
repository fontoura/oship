# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates in memory archetype objects from ADL files and stores them in the ZODB.        
        Parsing is performed in adl_1_4.py using Pyparsing. 
        
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

import pprint
import codecs
import pprint
import time
import sys
import os
import traceback
import mglob     
from sets import Set


x=os.getcwd().rfind('src')

logfile=os.getcwd()[:x]+'log/at_build_errors.log'

#create the logfile if it doesn't exist
f=open(logfile,'w')
f.close()

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=logfile,
                    filemode='w')

import ZODB
from ZODB import FileStorage,DB
from BTrees.OOBTree import OOBTree

import transaction
from zope.schema import Text
from zope.interface import Interface,implements
from persistent import Persistent 
from zope.exceptions import DuplicationError
from zope.app.folder import folder 
from zope.app.component.site import *
from pyparsing import *

from oship.openehr.rm.datatypes.text.codephrase import CodePhrase
from oship.openehr.rm.datatypes.text.dvtext import DvText
from oship.openehr.am.archetype.archetype import Archetype
from oship.openehr.rm.support.identification.terminologyid import TerminologyId
from oship.openehr.rm.support.identification.archetypeid import ArchetypeId

from blddefinition import bldDefinition
from bldinvariants import bldInvariants
from bldontolgy import bldOntology
from bldrevisionhistory import bldRevisionHistory

import adl_1_4


"""
edit the path below (no trailing '/') to point to your archetypes in ADL 1.4 format 
if you choose not use use the standard import directory. For example the commented out 
adlDir points to my SVN import tree of all archetypes on openEHR.org
"""

adlDir=os.getcwd()+'/import_adl'

x=os.getcwd().rfind('src')
dbDir=os.getcwd()[:x]+'var/OSHIP.fs'
fs=FileStorage.FileStorage(dbDir)
db=DB(fs)
conn=db.open()
root=conn.root()

# Setup the database for OSHIP - Each section gets a sitemanager.

if 'AR' not in root['Application']:
    root['Application']['AR']=folder.Folder()
    sm = LocalSiteManager(root['Application']['AR'])
    root['Application']['AR'].setSiteManager(sm)
    transaction.commit()
    
if 'CLINICAL' not in root['Application']:
    root['Application']['CLINICAL']=folder.Folder()
    sm = LocalSiteManager(root['Application']['CLINICAL'])
    root['Application']['CLINICAL'].setSiteManager(sm)
    transaction.commit()

if 'DEMOGRAPHICS' not in root['Application']:
    root['Application']['DEMOGRAPHICS']=folder.Folder()
    sm = LocalSiteManager(root['Application']['DEMOGRAPHICS'])
    root['Application']['DEMOGRAPHICS'].setSiteManager(sm)
    transaction.commit()    

if 'TR' not in root['Application']:
    root['Application']['TR']=folder.Folder()
    sm = LocalSiteManager(root['Application']['TR'])
    root['Application']['TR'].setSiteManager(sm)
    transaction.commit()

def CreateAT():
    """
    Create parse results to send to the builder.
    """
    
    fnames = mglob.expand("rec:"+adlDir+"=*.adl")
    n=0
    e=0
    errCount=0
    count=len(fnames)
    startTime=time.clock()
        
    fnames.sort()
    print "ADL File count: ",count

    for fname in fnames:
        n+=1               
        print "\n\nProcessing # ",n,' of ',count,' --->',fname
        adlSource = file(fname).read()
        
        try:
            # parsed_adl is the returned ParseResults object
            parsed_adl = adl_1_4.archetypeDefinition.parseString(adlSource)
        except ParseException: 
            e+=1
            logging.error("Error # "+str(e)+" Occured Parsing "+fname+':\n')
            print "Parsing Failed -- Error Logged!\n"
            errCount+=1
        else:   
            bldArchetype(parsed_adl)  
                
                
    print "\n\nParsed ",count," files in",time.clock()-startTime," seconds."
    print "There were ",errCount," parse errors. " 
    logging.info("There were "+repr(errCount)+" parse errors. ") 
    if errCount > 0:
        print "Please see: "+logfile+" file for errors & warnings."
        
    conn.close()
    db.close()
    os.remove(dbDir+'.lock')
    
    print "\n\nNow you should change back to "+(os.getcwd().rstrip('src/oship/atbldr')+'/oship')
    print "and execute 'bin/paster serve debug.ini' to restart your server."
    print "Then point your browser to http://localhost:8080/AR to see your repository.\n\n"
    logging.shutdown()
    
    return
        
        
def bldArchetype(parsed_adl):
    """
    Build the archetype object ready for persistence in the Archetype Repository site (AR).
    """
        
    adlVersion = unicode(parsed_adl.archetype.adl_version)
    archetypeId = ArchetypeId(unicode(parsed_adl.archetype[1]))
    concept = unicode(parsed_adl.concept)
    parentArchetypeId = archetypeId # it's the same minus specialisation;  I think. 
    parentArchetypeId.specialisation = u'' #strip any specialisation info off
    
    # the ontology must be built first so it can be used in the definition section.
    ontology=bldOntology(parsed_adl)
    definition=bldDefinition(parsed_adl)
    invariants=bldInvariants(parsed_adl)
    rev=None #bldRevisionHistory(parsed_adl) 
    uid=None # The OID can be assigned in the application instances
    #terminology ID for original language
    termID=TerminologyId(u"ISO_639-1::en",None)
    olang=CodePhrase(termID,u'en')
    trans=None #translations
    descr=None #ResourceDescription(olang,'testing',[],'the use','mis-use','copyright',{},{})
    ctrld=False #is controlled
    
    
    atObj=Archetype(adlVersion,archetypeId,uid,concept,parentArchetypeId,definition,ontology,invariants,olang,trans,descr,rev,ctrld)            
    # now fillin the data attribute with the object attributes so the Zope machinery works
    atObj.__name__ = unicode(parsed_adl.archetype[1])
    
    
    # now we need to persist the archetype in the ZODB
    try:
        root['Application']['AR'].__setitem__(atObj.__name__,atObj)
        transaction.commit()
    except NameError:
        logging.warning("WARNING: Error Occured Storing Archetype: "+atObj.__name__)
    except DuplicationError:
        print "WARNING:**** Duplicate Archetype ID. This Archetype was not committed to the repository. ***"
        logging.warning("Duplicate Archetype ID: "+atObj.__name__+" was not commited to the repository.")
        
    return
   
    
    
if __name__ == "__main__":
        CreateAT()     
