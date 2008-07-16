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

from datetime import datetime

from openehr.rm.datastructures.history.history import History
from openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime
from openehr.rm.datatypes.quantity.datetime.dvduration import DvDuration
from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from bldevent import bldEvent
from bldpointevent import bldPointEvent
from bldintervalevent import bldIntervalEvent

#called from bldObservation
def bldHistory(adl_list):
    histDict={
        "EVENT":bldEvent,
        "POINT_EVENT":bldPointEvent,
        "INTERVAL_EVENT":bldIntervalEvent
        }
    events=[]
    nodeid=''
    histObj=None
    if isinstance(adl_list[0],unicode) and '[at' in adl_list[0]:
        start=adl_list[0].find('[')
        nodeid=adl_list[0][start:]
        keyword=adl_list[0][:start]
        
    
    keylist=histDict.keys()
    keyloc=[]
     
    # locate all of the events
    for n,val in enumerate(adl_list):
        if isinstance(val,unicode) and '[at' in val:
            start=val.find('[')
            val=val[:start]
            if val in keylist:
                keyloc.append((n,val))
            
    #step backwards through the list of events and create it, 
    #removing it from the adl_list list, appending the object to the events list.
    keyloc.reverse()
    for x in keyloc:
        sublist=adl_list[x[0]:]
        adl_list=adl_list[:x[0]]
        events.append(histDict[x[1]](sublist))
        
    
    """
    origin=DvDateTime(datetime.now())
    period=DvDuration('')
    duration=DvDuration('')
    summary=ItemStructure('','','','','','')
    
    
    histObj=History(origin,events,period,duration,summary)
    """
    
    return histObj
