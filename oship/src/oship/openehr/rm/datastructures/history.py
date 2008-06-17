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


from zope.interface import implements
from zope.schema import List
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.dvdatetime import DvDateTime
from openehr.rm.datatypes.dvduration import DvDuration
from openehr.rm.datastructures.itemstructure import ItemStructure 
from openehr.rm.datastructures.datastructure import IDataStructure,DataStructure 


_ = MessageFactory('oship')

class IHistory(IDataStructure):
    u"""
    Root object of a linear history, i.e. time series structure. For a periodic series of
    events, period will be set, and the time of each Event in the History must correspond; i.e. the EVENT.offset must be a multiple of period for each Event. Missing
    events in a period History are however allowed.
    
    NOTE: The invariants have NOT been written yet for this interface.
    """
    
    origin = DvDateTime(
        title=_(u"origin"),
        description=_(u"Time origin of this event history. The first event is not necessarily at the origin point."),
        required=True
    )
    
    events = List(
        title=_(u"events"),
        description=_(u"The events in the series."),
        required= False
    )
    
    
    period=DvDuration(
        title=_(u"period"),
        description=_(u"Period between samples in this segment if periodic."),
        required=False
    )
    
    duration=DvDuration(
        title=_(u"duration"),
        description=_(u"""Duration of the entire History; either corresponds to the duration of all 
                    the events, and/or the duration represented by the summary, if it exists."""),
        required=False
    )
    
    summary=ItemStructure(
        title=_(u"summary"),
        description=_(u"""Optional summary data expressing e.g. text or image which summarises 
                         entire History."""),
        required=False
    )
    
    def isPeriodic(): 
        u"""Indicates whether history is periodic. Returns Boolean"""
        
    def asHierarchy():
        u"""Returns CLUSTER. Generate a CEN EN13606-compatible hierarchy of the physical representation."""


class History(DataStructure):
    u"""
    Root object of a linear history, i.e. time series structure. For a periodic series of
    events, period will be set, and the time of each Event in the History must correspond; i.e. the EVENT.offset must be a multiple of period for each Event. Missing
    events in a period History are however allowed.
    
    NOTE: The invariants have NOT been written yet for this interface.
    """
    
    implements(IHistory)
    
    def __init__(self,origin,events,period,duration,summary,**kw):
        self.origin=origin
        self.events=events
        self.period
        self.duration=duration
        self.summary=summary
        for n,v in kw.items():
            setattr(self,n,v)
            
    def isPeriodic(): 
        u"""Indicates whether history is periodic. Returns Boolean"""
        
    def asHierarchy():
        u"""Returns CLUSTER. Generate a CEN EN13606-compatible hierarchy of the physical representation."""

