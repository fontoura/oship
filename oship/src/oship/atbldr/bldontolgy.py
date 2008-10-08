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

from zope.schema import Dict,TextLine,Tuple,Set,Int
from zope.app.folder import Folder

from oship.openehr.am.archetype.ontology.archetypeontology import ArchetypeOntology
from oship.openehr.am.archetype.ontology.archetypeterm import ArchetypeTerm
from oship.openehr.rm.support.identification.objectref import ObjectRef
from oship.openehr.rm.support.identification.objectid import ObjectId

def bldOntology(parsed_adl):
    u"""
    Create the Ontolgy section of an archetype expressed in ADL.
    The specifications for attributes of ArchetypeOntology call for the types of set and list.
    The Python implementation uses dictionaries for term_codes and constraint_codes.
    This simplifies the end-user application code required to lookup the description and text of the codes.
    Within each language section (dictionary) the codes are keys to a tuple containing the description and text.
    for example: {'en':{'at0001':{'description':'some description','text':'some text')}...}
    
    """
    
    
    ontObj = ArchetypeOntology()    
    termCodes = {}
    termsDict={}
    codeList=[]
    constraintCodes = {}
    sections = parsed_adl.ontology.keys() #which sections are included in this ontology?   
    
    #ontObj.parentArchetype = ObjectRef(ObjectId(unicode(parsed_adl.archetype[1])),u'openehr',u'ARCHETYPE')
    ontObj.parentArchetype = ''
    
    if len(parsed_adl.specialize) == 0 or parsed_adl.specialize == '':
        ontObj.specialsationDepth = Int(0)
    else:
        ontObj.specialsationDepth = Int(parsed_adl.specialize) 
            
            
    if 'terminologies_available' in sections:
        ontObj.terminologiesAvailable = parsed_adl.ontology['terminologies_available'][0]
    else:
        ontObj.terminologiesAvailable = []
            
        
    if 'term_definitions' in sections:
        avail_lang = []
        for language in parsed_adl.ontology['term_definitions']:
            avail_lang.append(language[0])
        
        for l in avail_lang: # now process each language section
            at_codes = parsed_adl.ontology['term_definitions'][l]['items']
            for code in at_codes:
                # At some future point this should be more flexible than only having text and description
                termsDict[code[0]] = {'description':code[1][1],'text':code[2][1]}
            ontObj.termCodes[l] = termsDict  # for each language add the terms list.
            
    # this needs to be fixed to actually get the keywords in case there are more than these two
    ontObj.termAttributeNames = ['description','text']
    
    if 'constraint_definitions' in sections:
        avail_lang = []
        for language in parsed_adl.ontology['constraint_definitions']:
            avail_lang.append(language[0])    
            
        for l in avail_lang: # now process each language section
            at_codes = parsed_adl.ontology['constraint_definitions'][l]['items']
            for code in at_codes:
                # At some future point this should be more flexible than only having text and description
                termsDict[code[0]] = {'description':code[1][1],'text':code[2][1]}
            ontObj.constraintCodes[l] = termsDict  # for each language add the terms list.
     
    
    ontObj.__name__ = u'ontology'

    return ontObj
