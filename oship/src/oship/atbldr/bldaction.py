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

import logging

from oship.openehr.rm.ehr.composition.content.entry.action import Action

from oship.utils.flatten import flatten

def bldAction(parsed_adl):
    actionList=[]
    actionObj=None
    
    #turn the parsed definition into a list with all strings converted to unicode
    flat_adl = flatten(parsed_adl.definition)
    for x in flat_adl:
        if isinstance(x,str):
            x=unicode(x)
            
        actionList.append(x)
        
    """
    Action is composed of:
    time -->DvDateTime
    description-->ItemStructure
    ismTransition-->IsmTransition
    instructionDetails-->InstructionDetails
    """
    archetypeNodeId=actionList[0].strip('ACTION')
        
    
    return actionList

def mkdescr(desclist):
    descrObj=None
    valid=False
    #print 'description: ',desclist
    for n,x in enumerate(desclist):
        if isinstance(x,unicode) and 'ITEM_TREE' in x:
            descrObj=bldItemTree(desclist[n:len(desclist)])
            valid=True
            
    if not valid:
        logging.error("Invalid Action Description."+repr(desclist))
        print "\nUnknown Data Type for Action Description",desclist
        return None

    #print descrObj
    
    return descrObj
 