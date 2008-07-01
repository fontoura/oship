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

import logging
logging.basicConfig()

import ZODB
from ZODB import FileStorage,DB

import transaction
from zope.schema import Text
from zope.interface import Interface,implements
from persistent import Persistent 
from zope.exceptions import DuplicationError
from zope.app.folder import folder 
from zope.app.component.site import *
import pprint
import codecs
import pprint
import time
import sys
import os
import traceback
import mglob     
from sets import Set
from pyparsing import *

from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.rm.datatypes.text.dvtext import DvText
from openehr.am.archetype.archetype import Archetype

from oship.atdemo.atdemo import ATDemo
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
    

logDir=os.getcwd().rstrip('src/oship/atbldr')+'/oship/log/'
errlog=open(logDir+'ADL14parse_errors.log', 'w')

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
            # adlParsed is the returned ParseResults object
            adlParsed = adl_1_4.archetypeDefinition.parseString(adlSource)
        except ParseException: 
            e+=1
            errlog.write("Error # "+str(e)+" Occured Parsing "+fname+':\n')
            traceback.print_exc(2,file=errlog)
            errlog.write("\n\n")
            print "Parsing Failed -- Error Logged!\n"
            errCount+=1
        else:   
            bldArchetype(adlParsed)  
                
                
    print "\n\nParsed ",count," files in",time.clock()-startTime," seconds."
    print "There were ",errCount," parse errors. " 
    print logDir+"ADL14parse_errors.log file for errors & warnings."
    errlog.write("***END of Error Log***\n\n")       
    errlog.close()
    conn.close()
    db.close()
    os.remove(dbDir+'.lock')
    
    print "\n\nNow you should change back to "+(os.getcwd().rstrip('src/oship/atbldr')+'/oship')
    print "and execute '$bin/paster serve debug.ini' to restart your server."
    print "The point your browser to http://localhost:8080/AR to see your repository.\n\n"
    
    return
        
        
def bldArchetype(adlParsed):
    """
    Build the archetype object ready for persistence in the Archetype Repository site (AR).
    """
        
    adl_version=adlParsed.archetype.adl_version
    archetype_id=adlParsed.archetype[1]
    concept=adlParsed.concept
    parent_archetype_id=adlParsed.specialize
    definition=bldDefinition(adlParsed)
    ontology=bldOntology(adlParsed)
    invariants=bldInvariants(adlParsed)
    rev=bldRevisionHistory(adlParsed) 
       
    atObj=ATDemo(adl_version,archetype_id,concept,parent_archetype_id,definition,ontology,invariants,rev)            
    #atObj=Archetype(adl_version,archetype_id,concept,parent_archetype_id,definition,ontology,invariants,rev)            
    
    # now we need to persist the archetype in the ZODB
    try:
        root['Application']['AR'].__setitem__(archetype_id,atObj)
        transaction.commit()
    except NameError:
        errlog.write("WARNING: Error Occured Storing Archetype:\n")
        traceback.print_exc(2,file=errlog)
        errlog.write("\n\n")
    except DuplicationError:
        errlog.write("WARNING: Error Occured Storing Archetype:\n")
        traceback.print_exc(2,file=errlog)
        errlog.write("\n\n")       
        
    return
   
    
    
if __name__ == "__main__":
        CreateAT()     
