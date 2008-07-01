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

definClassMap={'SECTION':'Section','COMPOSITION':'Composition','OBSERVATION':'Observation',\
               'ITEM_TREE':'ItemTree','ADMIN_ENTRY':'AdminEntry','ACTION':'Action',\
                'EVALUATION':'Evaluation','INSTRUCTION':'Instruction','ELEMENT':'Element',\
                'CLUSTER':'Cluster','EVENT':'Event'}

def bldDefinition(adlParsed):
    """
    Create a CComplexObject containing the definition.
    """
    definClassDict = adlParsed.definition[0].asDict()
    oeClass = definClassDict['id']
    
    if oeClass.find('[at')!=-1:
        oeClass = oeClass[:oeClass.find('[at')]
        
    if definClassMap.has_key(oeClass):
        className = definClassMap[oeClass]
    else:
        className = ''
        print "Unknown class name: ",oeClass
        
    if className == 'Section':
        from bldsection import bldSection
        defObj = bldSection(adlParsed)
        return defObj
        
    if className == 'Composition':
        from bldcomposition import bldComposition
        defObj = bldComposition(adlParsed)
        return defObj
        
    if className == 'Observation':
        from bldobservation import bldObservation
        defObj = bldObservation(adlParsed)
        return defObj
        
    if className == 'ItemTree':
        from blditemtree import bldItemTree
        defObj = bldItemTree(adlParsed)
        return defObj

    if className == 'AdminEntry':
        from bldadminentry import bldAdminEntry
        defObj = bldAdminEntry(adlParsed)
        return defObj

    if className == 'Action':
        from bldaction import bldAction
        defObj = bldAction(adlParsed)
        return defObj

    if className == 'Evaluation':
        from bldevaluation import bldEvaluation
        defObj = bldEvaluation(adlParsed)
        return defObj
    
    if className == 'Instruction':
        from bldinstruction import bldInstruction
        defObj = bldInstruction(adlParsed)
        return defObj

    if className == 'Element':
        from bldelement import bldElement
        defObj = bldElement(adlParsed)
        return defObj

    if className == 'Cluster':
        from bldcluster import bldCluster
        defObj = bldCluster(adlParsed)
        return defObj

    if className == 'Event':
        from bldevent import bldEvent
        defObj = bldEvent(adlParsed)
        return defObj
    
    
