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
from bldelement import bldElement


def bldItemTree(itlist): 
    itDict = {
        "CLUSTER":bldCluster,
        "ELEMENT":bldElement
        }
    
    keylist = itDict.keys()
    keyloc = []
    elements = []
    clusters = []
    items = []
    if '[' in itlist[0]:
        archetypeNodeId=itlist[0].strip('ITEM_TREE')
        archetypeNodeId = archetypeNodeId.strip('[]')
    else:
        archetypeNodeId=u''
        
        
    # locate all of the elements and clusters
    for n,val in enumerate(itlist):
        if isinstance(val,unicode) and '[at' in val:
            start=val.find('[')
            val=val[:start]
            if val in keylist:
                keyloc.append((n,val)) # create a tuple of the keyword and location

    #step backwards through the list, find all clusters   
    #removing them from itlist, appending the object to the clusters list.
    keyloc.reverse()
    for x in keyloc:
        if x[1] == "CLUSTER":
            sublist=itlist[x[0]:]
            itlist=itlist[:x[0]]
            clusters.append(bldCluster(sublist))
            
    #step backwards through the list, find all elements outside of a cluster   
    #removing them from itlist, appending the object to the elements list.
    for x in keyloc:
        if x[1] == "ELEMENT":
            sublist=itlist[x[0]:]
            itlist=itlist[:x[0]]
            if len(sublist)>0:
                elements.append(bldElement(sublist))
            
    
    itObj = ItemTree('',archetypeNodeId,'','','','',items)
    itObj.__name__ = itlist[0]

    return itObj
