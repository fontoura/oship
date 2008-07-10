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

def bldHistory(data,state):
    origin=DvDateTime(datetime.now())
    events=[]
    period=DvDuration('')
    duration=DvDuration('')
    summary=ItemStructure('','','','','','')
    histObj=History(origin,events,period,duration,summary)
    
    return histObj
