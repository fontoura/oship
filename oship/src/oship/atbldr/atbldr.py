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

logfile=os.getcwd().rstrip('src/oship/atbldr')+'/oship/log/ADL14parse_errors.log'

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=logfile,
                    filemode='w')

import ZODB
from ZODB import FileStorage,DB

import transaction
from zope.schema import Text
from zope.interface import Interface,implements,classProvides
from persistent import Persistent 
from zope.exceptions import DuplicationError
from zope.app.folder import folder 
from zope.app.component.site import *
from pyparsing import *

from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.rm.datatypes.text.dvtext import DvText
from openehr.am.archetype.archetype import Archetype

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
adlDir=os.getcwd().rstrip('atbldr')+'/import_adl'
#adlDir='/home/tim/Documents/openEHR/knowledge/archetypes'
#adlDir='/home/tim/Documents/openEHR/knowledge/archetypes/dev-uk-nhs/adl/openehr/ehr/entry/observation'


dbDir=os.getcwd().rstrip('src/oship/atbldr')+'/oship/var/Data.fs'
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
    print "Please see: "+logfile+" file for errors & warnings."
    conn.close()
    db.close()
    os.remove(dbDir+'.lock')
    
    print "\n\nNow you should change back to "+(os.getcwd().rstrip('src/oship/atbldr')+'/oship')
    print "and execute '$bin/paster serve debug.ini' to restart your server."
    print "The point your browser to http://localhost:8080/AR to see your repository.\n\n"
    
    return
        
        
def bldArchetype(parsed_adl):
    """
    Build the archetype object ready for persistence in the Archetype Repository site (AR).
    """
        
    adl_version=parsed_adl.archetype.adl_version
    archetype_id=parsed_adl.archetype[1]
    concept=parsed_adl.concept
    parent_archetype_id=parsed_adl.specialize
    ontology=bldOntology(parsed_adl)
    definition=bldDefinition(parsed_adl,ontology)
    invariants=bldInvariants(parsed_adl)
    rev=bldRevisionHistory(parsed_adl) 
    uid=None
    
    
    atObj=Archetype(adl_version,archetype_id,uid,concept,parent_archetype_id,definition,ontology,invariants,rev)            
    #print 'ADL Version: ',atObj.adlVersion        
    #print '__name__ = ', atObj.__name__
    #print 'UID: ', atObj.uid
    #print 'Concept: ',atObj.concept
    #print 'Parent: ', atObj.parentArchetypeId
    #print 'Definition: ',atObj.definition
    
    """
    print 'Ontology: '
    print '   terminologies_available = ',atObj.ontology[0]
    print '   specialisation_depth = ',atObj.ontology[1]
    print '   term_codes = ',atObj.ontology[2]
    print '   constraint_codes = ',atObj.ontology[3]
    print '   term_attribute_names = ',atObj.ontology[4]
    print '   parent_archetype = ',atObj.ontology[5]
    print 'Invariants: ', atObj.invariants
    print 'Revision History: ',atObj.revisionHistory
    """
        
    # now we need to persist the archetype in the ZODB
    try:
        root['Application']['AR'].__setitem__(archetype_id,atObj)
        transaction.commit()
    except NameError:
        logging.warning("WARNING: Error Occured Storing Archetype: "+archetype_id)
    except DuplicationError:
        print "WARNING:  ****Duplicate Archetype ID.***"
        logging.warning("Duplicate Archetype ID: "+archetype_id)
        
    return
   
    
    
if __name__ == "__main__":
        CreateAT()     
