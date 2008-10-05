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

from oship.openehr.rm.datastructures.itemstructure.itemtree import ItemTree
from bldcluster import bldCluster

#called from bldActivity
def bldItemTable(itlist):    
    itObj=None
    items=[]
    if '[' in itlist[0]:
        archetypeNodeId=itlist[0].strip('ITEM_TREE')
    else:
        archetypeNodeId=''
            
    for n,x in enumerate(itlist):
        if isinstance(x,unicode):
            if 'CLUSTER' in x:
                cluster=bldCluster(itlist[n:len(itlist)])
                if cluster==None:
                    logging.error("Cluster Failed in: "+archetypeNodeId)
                    return None
                else:
                    items.append(cluster)
            elif 'ELEMENT' in x:
                element=bldElement(itlist[n:len(itlist)])
                if element==None:
                    logging.error("Element Failed in: "+archetypeNodeId)
                    return None
                else:
                    items.append(element)
    
    itObj= ItemTree(items)
    
    return itObj
