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


from pyparsing import ParseBaseException,ParseException 

import adl_1_4


import grok

from archetype import Archetype,ArchetypeOntology,ArchetypeTerm
from datatypes import CodePhrase

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
    adlver=unicode(parsed_adl.archetype[0][1])
    atid=unicode(parsed_adl.archetype[1])
    ontmap=bldOntology(parsed_adl.ontology)
    definmap=bldDefinition(parsed_adl.definition,ontmap)
    descmap=bldDescription(parsed_adl.description)
    
    arch=Archetype()
    #parch=grok.Container()
    
    arch[u"adlVersion"]=adlver
    arch[u"archetypeId"]=atid
    arch[u"uid"]=u""
    arch[u"concept"]=u"at0000"
    arch[u"parentArchetypeId"]=None
    arch[u"definition"]=definmap
    arch[u"ontology"]=ontmap
    arch[u"invariants"]=[]
    arch[u"originalLanguage"]=u"en"
    arch[u"translations"]=None
    arch[u"description"]=descmap
    arch[u"revisionHistory"]=None
    arch[u"isControlled"]=False
    
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
    key_list=[u'terminologies_available',u'term_definitions',u'constraint_definitions',u'term_binding',u'constraint_binding']
    lang_list=[u'en',u'de',u'nl',u'fr'] # needs to access termserver
    itemlist=[]
    # now go through ontlist and map all the words.  
    
    ontmap={}
    for index, item in enumerate(ontlist):
        ontmap[index]=item  
    
        
    a = ontmap.items()
    keywords=[]
    for x in a:
        for v in key_list:
            if v in x:
                keywords.append(x)
            
    """
    keywords now contains tuples of all the possible section names and their index:
    i.e. [(0, u'terminologies_available'), (3, u'term_definitions'), (346, u'term_binding')]
    """
    numkeys=len(keywords)
    ends=[]
    endsection=[]
    for x in keywords:
        ends.append([x][0][0])
    
    ends=ends[1:]
    for x in ends:
        y=x-1
        endsection.append(y)
        
    endsection.append(len(a)) # final word in the ontology.
        
    sections=[]
    n=0
    for x in keywords:
        t=(x[1],x[0],endsection[n])
        sections.append(t)
        n+=1
     
    """
    Now sections contain tuples of the name of the present sections in the ontology, 
    the starting word and the ending word.
    i.e. [(u'terminologies_available', 0, 2), (u'term_definitions', 3, 345), (u'term_binding', 346, 405)]
    
    We need to prcess the sections in the order that they are expected to appear so that they break will work correctly (I think).
    """
    
    #print "Sections: ",sections
    
    # process terminologies available
    itemlist=[]
    for y in sections:    
        if y[0]==u'terminologies_available':      
            ontlist=ontmap.items() 
            #print ontlist
            try:
                for x in ontlist:
                    n=x[0]
                    if n > y[2]: 
                        break # if we have reached the end of the section then leave.
                    else:
                        itemlist.append(x[1])
            except IndexError:
                pass

    termAvail=itemlist
    
    # process termCodes - 
    """
    In OSHIP we added the word 'bind' as a key to every entry in order to maintain a 
    balanced structure for those that have term bindings and those that do not.  
    I find the word 'provenance as used in the specifications to be less than intuitive.  
    """
    itemlist=[]
    for y in sections:    
        if y[0]==u'term_definitions':      
            ontlist=ontmap.items() 
            try:
                for x in ontlist:
                    if x[1] in lang_list: # If it's a langugage change just enter it.
                        itemlist.append(x[1]) 
                    if x[1].startswith(u'at0'): # check to see if this is an at code. 
                        n=x[0] # the index  number of this tuple
                        if n > y[2]: 
                            break # if we have reached the end of the section then leave.
                        else:
                            itemlist.append({x[1]:{ontlist[n+1][1]:ontlist[n+2][1],ontlist[n+3][1]:ontlist[n+4][1],u"bind":None}})
            except IndexError:
                pass
        
    termCodes=itemlist  
    
    #process constraint codes
    itemlist=[]
    for y in sections:    
        if y[0]==u'constraint_definitions':      
            ontlist=ontmap.items() 
            try:
                for x in range(y[1],y[2]):
                    if ontlist[x][1] in lang_list: # If it's a langugage change just enter it.
                        itemlist.append(ontlist[x][1]) 
                    if ontlist[x][1].startswith(u'ac0'): # check to see if this is an ac code. 
                        n=ontlist[x][0] # the index  number of this tuple
                        itemlist.append({ontlist[x][1]:{ontlist[x+1][1]:ontlist[x+2][1],ontlist[x+3][1]:ontlist[x+4][1],u"bind":None}})
            except IndexError:
                pass
            
    constCodes=itemlist
   
    #process term bindings 
    itemlist=[]
    binddict={}
    for y in sections:    
        if y[0]==u'term_binding':      
            ontlist=ontmap.items() 
            tmplist=ontlist[y[1]:y[2]]
            try:
                z=3 # key of first at code
                for x in tmplist:
                    
                    binddict[tmplist[z][1]]=tmplist[z+1][1]
                    z+=2                             
            except IndexError:
                pass
            
        for y in termCodes:
            if isinstance(y,dict):
                z=y.keys() # always only one
                if binddict.has_key(z[0]):
                    codestr=binddict[z[0]].replace('_','')
                    codelist=codestr.split('::')
                    cp=CodePhrase(codelist[0],codelist[1])
                    y[z[0]][u'bind']=cp
                                
               
        
            
    #process constraint bindings
    itemlist=[]
    binddict={}
    for y in sections:    
        if y[0]==u'constraint_binding':      
            ontlist=ontmap.items() 
            try:
                for x in range(y[1],y[2]):
                    if ontlist[x][1].startswith(u'ac0'): # check to see if this is an ac code.
                        
                        for y in constCodes:
                            if isinstance(y,dict):
                                print y
                                if y.has_key(ontlist[x][1]):
                                    #constCodes[y][u'bind']=ontlist[x+1]
                                    print constCodes[x]
            except IndexError:
                pass
    
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
    