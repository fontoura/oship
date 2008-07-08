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
from oship.utils.flatten import flatten

def bldItemTree(parsed_adl,errlog):
    itlist=[]
    itgen=flatten(parsed_adl)
    for x in itgen:
        if isinstance(x,str):
            x=unicode(x)
            
        itlist.append(x)
               
    #print itlist,type(itlist)
    itObj= ItemTree(itlist)
    #print type(itObj)
    
    return itObj
