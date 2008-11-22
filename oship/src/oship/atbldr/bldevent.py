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

from blditemtree import bldItemTree
from blditemlist import bldItemList

def bldEvent(adl_list):
    eventDict={"ITEM_TREE":bldItemTree,
               "ITEM_LIST":bldItemList,
               }
    
    nodeid=''
    y=adl_list[6]
    
    if isinstance(y,unicode) and '[at' in y:
        start=y.find('[')
        nodeid=y[start:]
        keyword=y[:start]
    else:
        keyword=y

    if eventDict.has_key(keyword):
        eventObj=eventDict[keyword](adl_list[6:])
    else:
        logging.error("Unknown Event keyword: "+repr(keyword))

    return adl_list
