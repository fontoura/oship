# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates Python instances from ADL files and stores them in the ZODB 'ar' .        
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

from archetype import Archetype,ArchetypeOntology,ArchetypeTerm

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
        print "Parsing Failed!\n"
        
    return bldArchetype(fname,parsed_adl)
                
        
        
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
    
    ontmap=bldOntology(parsed_adl.ontology)
    definmap=bldDefinition(parsed_adl.definition,ontmap)
    descmap=bldDescription(parsed_adl.description)
    
    arch=Archetype(unicode(parsed_adl.archetype[0][1]),unicode(parsed_adl.archetype[1]),u"",u"at0000",u"",definmap,ontmap,[],u"en",None,None,None,False)
    print "\n\nAll finished processing ADL for: ",class_name, "\n\n"
    
    return [class_name,arch]

def bldOntology(ontlist):
    """Build an ontology."""
    
    # pre-assign all attributes
    termAvail=[]
    specDepth=0
    termCodes={}
    constCodes={}
    termAN=[]
    parent=u''
    
    #cleanup the list
    ontlist=flatten(ontlist)
    key_list=[u'terminologies_available',u'term_definitions',u'term_binding',u'constraint_definitions']
    lang_list=[u'en',u'de',u'nl']
    itemlist=[]
    # now go through ontlist and map all the words.  
    
    ontmap={}

    for index, item in enumerate(ontlist):
        ontmap[index]=item  
    
    if ontmap[0]==u'term_definitions':      
        ontlist=ontmap.items()
        try:
            for x in ontlist:
                if x[1] in lang_list:
                    itemlist.append(x[1])
                if x[1].startswith(u'at0'): 
                    #print x
                    n=x[0] # the index  number of this at code
                    #print n
                    itemlist.append({x[1]:{ontlist[n+1][1]:ontlist[n+2][1],ontlist[n+3][1]:ontlist[n+4][1]}})
        except IndexError:
            pass
        
        
        ##Language test
        #for y in itemlist:
            #if y == u'en':
                #print y
        
    #for x in ontlist:
        #if x[1].startswith(u'ac0'):        
            #print x

        
    
        
    
    
    
    
    
    
    termCodes=itemlist        
    ontology=ArchetypeOntology(termAvail,specDepth,termCodes,constCodes,termAN,parent)    
    return ontology

   
    
    
def bldDefinition(definlist,ontmap):
    """Build a definition object using the ontmap to lookup the at & ac codes"""
        
    # flatten and unicode the nested input list.    
    definlist=flatten(definlist)
    defmap={}
    
    for index, item in enumerate(definlist):
        defmap[index]=item
        
        
    if "COMPOSITION" in defmap[0]:
        bldComposition(defmap,ontmap)
        
    # add all the other possibilities here
    
        
    #
    #print "Ontology: ",ontmap   
    #print "Definition: ",defmap  
    
    
    return defmap
    
def bldSection(defmap,ontmap):
    pass

def bldComposition(defmap,ontmap):
    pass

def bldObservation(defmap,ontmap):
    pass

def bldItemTree(defmap,ontmap):
    pass

def bldAdminEntry(defmap,ontmap):
    pass

def bldAction(defmap,ontmap):
    pass

def bldEvaluation(defmap,ontmap):
    pass

def bldInstruction(defmap,ontmap):
    pass

def bldElement(defmap,ontmap):
    pass

def bldCluster(defmap,ontmap):
    pass

def bldEvent(defmap,ontmap):
    pass

def bldAddress(defmap,ontmap):
    pass

def bldDescription(desclist):
    """Build a description object"""
    
    desclist=flatten(desclist)
    descmap={}
    for index, item in enumerate(desclist):
        descmap[index]=item

    return descmap
    


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
            # replace any brackets with underscores so Python doesn't thnk it's a list and we still havea seperator.
            x=x.replace('[','_')
            x=x.replace(']','_')
            try:
                x=unicode(x, "utf-8")  # need more decode types here
            except UnicodeDecodeError:
                x=unicode(x, "latin1")
        
        rtnlist.append(x)

    return rtnlist    
    