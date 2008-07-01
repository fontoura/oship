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

def bldOntology(adlParsed):
    u"""
    Create the Ontolgy section of an archetype.
    """

    sections = adlParsed.ontology.keys()    
    tANList = []
    termCodes = []
    constraintCodes = []
    
    if len(adlParsed.specialize) == 0 or adlParsed.specialize == '':
        specialsationDepth = 0
    else:
        specialsationDepth = 1 
            
            
    if 'terminologies_available' in sections:
        terminologies_available=repr(adlParsed.ontology['terminologies_available'])
    else:
        terminologies_available=''
            
    if 'term_definitions' in sections:
        avail_lang = []
        for language in adlParsed.ontology['term_definitions']:
            avail_lang.append(language[0])
        
        for l in avail_lang:
            at_codes = adlParsed.ontology['term_definitions'][l]['items']
            for code in at_codes:
                    for x in range(1,len(code)):
                            tANList.append(code[x][0])
                    termCodes.append([l,code[0]])
            
    if 'constraint_definitions' in sections:
        avail_lang = []
        for language in adlParsed.ontology['constraint_definitions']:
            avail_lang.append(language[0])       
        for l in avail_lang:
            ac_codes = adlParsed.ontology['constraint_definitions'][l]['items']
            for code in ac_codes:
                for x in range(1,len(code)):
                        tANList.append(code[x][0])
                constraintCodes.append([l,code[0]])

    else:
        constraintCodes=[]
            
    termAttributeNames=tANList
    
    return [terminologies_available,termCodes,constraintCodes,termAttributeNames]                    
