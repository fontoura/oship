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
from openehr.rm.datastructures.itemstructure.itemtree import ItemTree
from bldcluster import bldCluster

def bldItemTree(itlist,errlog):
    
    if '[' in itlist[0]:
        archetypeNodeId=itlist[0].strip('ITEM_TREE')
    else:
        archetypeNodeId=''
        
    cardinality=itlist[6],itlist[8]
    
    if 'CLUSTER' in itlist[10]:
        items=bldCluster(itlist[10:len(itlist)],errlog)
    
    itObj= ItemTree(items)
    
    #print '\n\nItem Tree: ',itlist
    return itObj
