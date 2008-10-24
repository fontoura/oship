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
import logging

from oship.utils.flatten import flatten

from bldhistory import bldHistory
from oship.openehr.rm.ehr.composition.content.entry.observation import Observation

def bldObservation(parsed_adl):
    obsDict={
        "HISTORY":bldHistory,
        }
    
    definList=[]
    definObj=None
    stateObj=None
    nodeid=''
    
    #turn the parsed definition into a list with all strings converted to unicode
    flat_adl = flatten(parsed_adl.definition)
    for x in flat_adl:
        if isinstance(x,str):
            x=x.decode('utf-8')
        
        definList.append(x)
        
    y=definList[5]
    
    if isinstance(y,unicode) and '[at' in y:
        start=y.find('[')
        nodeid=y[start:]
        keyword=y[:start]
    else:
        keyword=y
        
    if obsDict.has_key(keyword):
        definObj=obsDict[keyword](definList[5:])
    else:
        logging.error("Unknown Observation keyword: "+repr(keyword))
        
            
    obsObj=Observation(definObj,stateObj,nodeid)
   
    return obsObj

        