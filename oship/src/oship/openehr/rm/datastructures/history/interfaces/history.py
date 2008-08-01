# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the Data Stuctures Information Model
History Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


from zope.schema import List,Object
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime
from openehr.rm.datatypes.quantity.datetime.interfaces.dvduration import IDvDuration
from openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure 
from openehr.rm.datastructures.interfaces.datastructure import IDataStructure 


_ = MessageFactory('oship')

class IHistory(IDataStructure):
    u"""
    Root object of a linear history, i.e. time series structure. For a periodic series of
    events, period will be set, and the time of each Event in the History must correspond; i.e. the EVENT.offset must be a multiple of period for each Event. Missing
    events in a period History are however allowed.
    
    NOTE: The invariants have NOT been written yet for this interface.
    """
    
    origin = Object(
        schema=IDvDateTime,
        title=_(u"origin"),
        description=_(u"Time origin of this event history. The first event is not necessarily at the origin point."),
        required=True
    )
    
    events = List(
        value_type = Object(schema=IEvent),
        title=_(u"events"),
        description=_(u"The events in the series."),
        required= False
    )
    
    
    period=Object(
        schema=IDvDuration,
        title=_(u"period"),
        description=_(u"Period between samples in this segment if periodic."),
        required=False
    )
    
    duration=Object(
        schema=IDvDuration,
        title=_(u"duration"),
        description=_(u"""Duration of the entire History; either corresponds to the duration of all 
                    the events, and/or the duration represented by the summary, if it exists."""),
        required=False
    )
    
    summary=Object(
        schema=IItemStructure,
        title=_(u"summary"),
        description=_(u"""Optional summary data expressing e.g. text or image which summarises 
                         entire History."""),
        required=False
    )
    
    def isPeriodic(): 
        u"""Indicates whether history is periodic. Returns Boolean"""
        
    def asHierarchy():
        u"""Returns CLUSTER. Generate a CEN EN13606-compatible hierarchy of the physical representation."""

