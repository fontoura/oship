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

from bldevent import bldEvent
from bldcluster import bldCluster
from bldelement import bldElement
from bldinstruction import bldInstruction
from bldevaluation import bldEvaluation
from bldaction import bldAction
from bldadminentry import bldAdminEntry
from blditemtree import bldItemTree
from bldobservation import bldObservation
from bldcomposition import bldComposition
from bldsection import bldSection

definClassMap={'SECTION':bldSection,'COMPOSITION':bldComposition,'OBSERVATION':bldObservation,\
               'ITEM_TREE':bldItemTree,'ADMIN_ENTRY':bldAdminEntry,'ACTION':bldAction,\
                'EVALUATION':bldEvaluation,'INSTRUCTION':bldInstruction,'ELEMENT':bldElement,\
                'CLUSTER':bldCluster,'EVENT':bldEvent}

def bldDefinition(parsed_adl):
    u"""
    Create an object containing the definition.
    This function determines the type of definition section to create 
    and calls that builder.
    """
    
    definClassDict = parsed_adl.definition[0].asDict()
    oeClass = definClassDict['id']
    definition=None
    
    #strip off the nodeid if there is one
    if oeClass.find('[at')!=-1:
        oeClass = oeClass[:oeClass.find('[at')]
        
        
    #call the appropriate builder
    try:
        definition=definClassMap[oeClass](parsed_adl)
    except KeyError ("Unknown Definition Type",oeClass):
        logging.error("Unknown Definition Type",oeClass)
    
    return definition


