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

from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.rm.datatypes.text.dvtext import DvText

def bldComposition(parsed_adl,ontology):
    definClassDict=parsed_adl.definition[0].asDict()
    langTermId=parsed_adl.language['original_language'].split('::')[0].strip('[')
    langStr=parsed_adl.language['original_language'].split('::')[1].strip(']')   
    node_id = definClassDict['id'][definClassDict['id'].find('[at'):]
    category=definClassDict['body']['attributes']['category']
    
    if 'content' in definClassDict['body']['attributes'].keys():
        content=definClassDict['body']['attributes']['content']
    else:
        content=None
        
    if 'context' in definClassDict['body']['attributes'].keys():
        context=definClassDict['body']['attributes']['context']            
    else:
        context=None     
    
    composer = "PartyProxy"
    language = CodePhrase(langTermId,langStr)
    territory = CodePhrase('ISO_3166-1','AU') #see implementation notes.
    uid = "UidBasedId()"       
    name = DvText(parsed_adl.archetype[1],{},'','','','') # should be concatenated with path to instance at runtime
    archetypeDetails = parsed_adl.archetype[1],'','1.0.1'
    feederAudit = "FeederAudit()"
    links = []
    
    definition=[context,content,category,composer,language,territory,uid,\
                          name,archetypeDetails,feederAudit,links]
    """    
    definition=CComplexObject(context,content,category,composer,language,territory,uid,\
                          name,archetypeDetails,feederAudit,links)
    """    
    return definition
    

   
