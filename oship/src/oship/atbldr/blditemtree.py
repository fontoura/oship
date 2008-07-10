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

#called from bldActivity
def bldItemTree(itlist):    
    itObj=None
    items=[]
    if '[' in itlist[0]:
        archetypeNodeId=itlist[0].strip('ITEM_TREE')
    else:
        archetypeNodeId=''
            
    for y,x in enumerate(itlist):
        if isinstance(x,unicode) and 'CLUSTER' in x:
            items.append(bldCluster(itlist[y:len(itlist)]))
    
    itObj= ItemTree(items)
    
    #print '\n\nItem Tree: ',itObj
    return itObj
