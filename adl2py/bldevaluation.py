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


from oship.utils.flatten import flatten

from oship.openehr.rm.ehr.composition.content.entry.evaluation import Evaluation
from blditemtree import bldItemTree
from blditemlist import bldItemList
from blditemsingle import bldItemSingle
from blditemtable import bldItemTable

def bldEvaluation(parsed_adl):
    
    definList = []
    evaDict = {
        "ITEM_LIST":bldItemList,
        "ITEM_SINGLE":bldItemSingle,
        "ITEM_TABLE":bldItemTable,
        "ITEM_TREE":bldItemTree,
        }
    
    #turn the parsed definition into a list with all strings converted to unicode
    flat_adl = flatten(parsed_adl.definition)
    for x in flat_adl:
        if isinstance(x,str):
            x=x.decode('utf-8')
        
        definList.append(x)
        
    y=definList[5]
    
    if isinstance(y,unicode) and '[at' in y:
        start=y.find('[')
        name = y[start+1:].strip(']')
        nodeid=y[start:]
        keyword=y[:start]
    else:
        keyword=y
        definObj.__name__ = y 
        
    # now go build the type of evaluation object based on the keyword   
    if evaDict.has_key(keyword):
        definObj.__setitem__(keyword, evaDict[keyword](definList[5:]))
    else:
        logging.error("Unknown Evaluation keyword: "+repr(keyword))

    definObj.__name__ = name
    
    return definObj
