# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the Data Stuctures Information Model
History Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.schema import List,Field,Int 

from openehr.rm.datastructures.interfaces.datastructure import IDataStructure
from openehr.rm.datatypes.datetm import DvDateTime 
from openehr.rm.datatypes.datetm import DvDuration
from openehr.rm.datatypes.text import DvCodedText 

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')



class IHistory(IDataStructure):
    u"""
    Root object of a linear history, i.e. time series structure. For a periodic series of
    events, period will be set, and the time of each Event in the History must correspond; i.e. the EVENT.offset must be a multiple of period for each Event. Missing
    events in a period History are however allowed.
    
    NOTE: The invariants have NOT been written yet for this interface.
    """
    
    origin = DvDateTime('',
        title=_(u"""origin"""),
        description=_(u"""Time origin of this event history. The first event is not necessarily at the origin point."""),
        required=True
    )
    
    events = List(
        title=_(u"""events"""),
        description=_(u"""The events in the series."""),
        required= False
    )
    
    
    period=DvDuration(
        title=_(u"""period"""),
        description=_(u"""Period between samples in this segment if periodic."""),
        required=False
    )
    
    duration=DvDuration(
        title=_(u"""duration"""),
        description=_(u"""Duration of the entire History; either corresponds to the duration of all 
                    the events, and/or the duration represented by the summary, if it exists."""),
        required=False
    )
    
    summary=ItemStructure(
        title=_(u"""summary"""),
        description=_(u"""Optional summary data expressing e.g. text or image which summarises 
                         entire History."""),
        required=False
    )
    
    def isPeriodic(): 
        u"""Indicates whether history is periodic. Returns Boolean"""
        
    def asHierarchy():
        u"""Returns CLUSTER. Generate a CEN EN13606-compatible hierarchy of the physical representation."""

class IEvent(ILocatable):
    u"""
    Defines the abstract notion of a single event in a series. This class is generic,allowing types 
    to be generated which are locked to particular spatial types, such as EVENT<ITEM_LIST> Subtypes 
    express point or interval data.
    """
    
    time=DvDateTime(
        title=_(u"""time"""),
        description=_(u"""Time of this event. If the width is non-zero, it is the time point of the 
                         trailing edge of the event."""),
        required=True
    )
    
            
    data=Field(
        title=_(u"""data"""),
        description=_(u"""The data of this event."""),
        required=True
    )
    
    state=ItemStructure(
        title=_(u"""state"""),
        description=_(u"""Optional state information.for this event."""),
        required=False
    )
    
    parent=History(
        title=_(u"""parent"""),
        description=_(u"""redefinition of LOCATABLE.parent to type of History"""),
        required=True
    )
    
    offset=DvDuration(
        title=_(u"""offset"""),
        description=_(u"""Offset of this event from origin, computed as time.diff(parent.origin)"""),
        required=True
    )

    def offsetValidity(event):
        
class IPointEvent(IEvent):
    u"""
    Defines a single point event in a series.
    """    
    
    
class IIntervalEvent(IEvent):
    u""" 
    Defines a single interval event in a series.
    
    NOTE: Invariants are incomplete.
    """
    
    width=DvDuration(
        title=_(u"""width"""),
        description=_(u"""Length of the interval during which the state was true. 
                      Void if an instantaneous event. OSHIP NOTE: The specs indicate 
                      this attribute is required but the text says it is Void if instantaneous.
                      How should this conflict be resolved?"""),
        required=True
    )
    
    mathFunction=DvCodedText('',
        title=_(u"""mathFunction"""),
        description=_(u"""Mathematical function of the data of this event, e.g. “maximum”, “mean” etc. 
                      Coded using openEHR Terminology group “event math function”."""),
        required=True
    )
    
    sampleCount=Int(
        title=_(u"""sampleCount"""),
        description=_(u"""Optional count of original samples to which this event corresponds."""),
        required=False
    )
    
                              
    def intervalStartTime():
         u"""Start time of the interval of this event."""
         


    