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
from openehr.rm.datastructures.itemstructure.representation.cluster import Cluster

from bldelement import bldElement

def bldCluster(clist,errlog):
    items=[]
    if '[' in clist[0]:
        archetypeNodeId=clist[0].strip('ITEM_TREE')
    else:
        archetypeNodeId=''
        
    occurrences=clist[2],clist[4]
    x=0
    for y in clist:
        if isinstance(y,unicode) and 'ELEMENT' in y:
            items.append(bldElement(clist[x:x+10],errlog))
        x+=1
        
    print '\n\n',items
    
    return items
