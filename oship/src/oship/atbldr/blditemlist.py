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

from openehr.rm.datastructures.itemstructure.itemlist import ItemList
from bldcluster import bldCluster

#called from bldEvent
def bldItemList(adl_list):    
    ilObj=None
    items=[]
    print adl_list
    
    """
    if '[' in adl_list[0]:
        archetypeNodeId=adl_list[0].strip('ITEM_LIST')
    else:
        archetypeNodeId=''
            
    for n,x in enumerate(adl_list):
        if isinstance(x,unicode) and 'CLUSTER' in x:
            cluster=bldCluster(adl_list[n:len(adl_list)])
            if cluster==None:
                logging.error("Cluster Failed in: "+archetypeNodeId)
                return None
            else:
                items.append(cluster)
    
    ilObj= ItemList(items)
    """
    #print '\n\nItem List: ',ilObj
    return ilObj
