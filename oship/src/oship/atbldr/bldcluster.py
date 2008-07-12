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

from openehr.rm.datastructures.itemstructure.representation.cluster import Cluster

from bldelement import bldElement

#called from bldItemTree
def bldCluster(clist):
    items=[]
    if '[' in clist[0]:
        archetypeNodeId=clist[0].strip('CLUSTER')
    else:
        archetypeNodeId=''
            
    for n,x in enumerate(clist):
        if isinstance(x,unicode) and 'ELEMENT' in x:
            elem=bldElement(clist[n:n+10])
            if elem == None:
                logging.error("Element Failed in: "+archetypeNodeId)
                return None
            else:
                items.append(elem)
        
    #print '\n\n Items in Cluster:',items
    
    return items
