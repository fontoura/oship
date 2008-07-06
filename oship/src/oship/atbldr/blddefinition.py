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

def bldDefinition(parsed_adl,errlog,ontology):
    """
    Create a CComplexObject containing the definition.
    """
    definClassDict = parsed_adl.definition[0].asDict()
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
        defObj = bldSection(parsed_adl,errlog)
        return defObj
        
    if className == 'Composition':
        from bldcomposition import bldComposition
        defObj = bldComposition(parsed_adl,errlog)
        return defObj
        
    if className == 'Observation':
        from bldobservation import bldObservation
        defObj = bldObservation(parsed_adl,errlog)
        return defObj
        
    if className == 'ItemTree':
        from blditemtree import bldItemTree
        defObj = bldItemTree(parsed_adl,errlog)
        return defObj

    if className == 'AdminEntry':
        from bldadminentry import bldAdminEntry
        defObj = bldAdminEntry(parsed_adl,errlog)
        return defObj

    if className == 'Action':
        from bldaction import bldAction
        defObj = bldAction(parsed_adl,errlog)
        return defObj

    if className == 'Evaluation':
        from bldevaluation import bldEvaluation
        defObj = bldEvaluation(parsed_adl,errlog)
        return defObj
    
    if className == 'Instruction':
        from bldinstruction import bldInstruction
        defObj = bldInstruction(parsed_adl,errlog,ontology)
        return defObj

    if className == 'Element':
        from bldelement import bldElement
        defObj = bldElement(parsed_adl,errlog)
        return defObj

    if className == 'Cluster':
        from bldcluster import bldCluster
        defObj = bldCluster(parsed_adl,errlog)
        return defObj

    if className == 'Event':
        from bldevent import bldEvent
        defObj = bldEvent(parsed_adl,errlog)
        return defObj
    
    
