# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates Python source files from ADL files.        
        Parsing is performed in adl_1_4.py using Pyparsing. 
        You will need to easy_install pyparsing and mglob in your 'oshipenv'
        
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


import codecs
import time
import os
import traceback   
import sys
import mglob
import logging
import string

from pyparsing import ParseBaseException

import adl_1_4


import grok
import datetime
from zope.app.folder import Folder
from zope.schema import TextLine

#logfile=os.getcwd()+'/at_build.log'

#create the logfile if it doesn't exist
#f=open(logfile,'w')
#f.close()

#logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s %(levelname)s %(message)s',
                    #filename=logfile,
                    #filemode='w')



"""
edit the path below (no trailing '/') to point to your archetypes in ADL 1.4 format 
if you choose not use use the standard import directory.
"""

def getFileList():
    adlDir=os.getcwd()+'/src/oship/openehr/adl'    
    fnames = mglob.expand("rec:"+adlDir+"=*.adl")
    fnames.sort()
    return fnames

def CreateAT(fname):
    """
    Create parse results to send to the builder.
    """
    
   
    adlSource = file(fname).read()
    file(fname).close()
    try:
        # parsed_adl is the returned ParseResults object
        parsed_adl = adl_1_4.archetypeDefinition.parseString(adlSource)
       
        item_name = repr(parsed_adl.archetype[1])
    except ParseException: 
        #logging.error("Error Occured Parsing "+fname+':\n')
        print "Parsing Failed -- Error Logged!\n"
    #else: 
        #logging.info("Processing: "+item_name) 
        
    return [item_name.replace('.','_'),bldArchetype(fname,parsed_adl)]  
                

#logging.info("There were ADL parse errors. ") 
#logging.info("*******END OF LOG FILE FOR THIS RUN*******")         
#logging.shutdown()
    

        
        
def bldArchetype(fname,parsed_adl):
    """
    Build the archetype content for the ar.
    """
    #now lets turn the archetypeid into a normal Python CamelCase name
    class_name=(parsed_adl.archetype[1]).partition('.')[2]
    class_name.lower()
    class_name=class_name.replace('.',' ') # replace periods with spaces
    class_name=class_name.replace('-',' ') # replace dashes with spaces
    class_name=class_name.replace('_',' ') # replace underscores with spaces
    class_name = string.capwords(class_name)
    class_name=class_name.replace(' ','') # replace spaces    
    
    at=Folder()  # The folder that holds each archetype
    at.__setitem__(class_name,parsed_adl.archetype[1])
    at.__setitem__(u"adlVersion",parsed_adl.archetype[0][1])
    at.__setitem__(u"Description",bldDescription(parsed_adl.description))
    at.__setitem__(u"Ontology",bldOntology(parsed_adl.ontology))
    at.__setitem__(u"Definition",bldDefinition(parsed_adl.definition))
 
    print "\n\nAll finished processing ADL for: ",class_name, "\n\n"
    
    return at

def bldOntology(ontlist):
    """Build an ontology dictionary."""

    
    
    #term_defs=Folder() # contains folders of all languages
    #languages=Folder() #contains folders of all items in a language
    #items=Folder() # contains a dictionary of codes as keys and a list of description and text 
    
    
    return flatten(ontlist)

   
def bldDescription(desclist):
    """Build a description object"""

    return flatten(desclist)
    
    
    
def bldDefinition(definlist):
    """Build a definition object"""
        
    return flatten(definlist)
    
    
def flatten(x):
    """flatten(sequence) -> list

    Returns a single, flat list which contains all elements retrieved
    from the sequence and all recursively contained sub-sequences
    (iterables). All strings are converted to unicode.
    
    """
    result = []
    for el in x:
        #if isinstance(el, (list, tuple)):
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
            
            
    # all strings must be unicode
    rtnlist=[]
    for x in result:
        if isinstance(x,str):
            x=unicode(x)
        
        rtnlist.append(x)

    return rtnlist    
    