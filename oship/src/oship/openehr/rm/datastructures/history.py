# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Implementations for the Data Stuctures Information Model
History Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.interface import implements

from openehr.rm.datastructures.interfaces.history import *
from openehr.rm.datastructures.datastructure import DataStructure
from openehr.rm.common.archetyped import Locatable

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')



class History(DataStructure):
    u"""
    Root object of a linear history, i.e. time series structure. For a periodic series of
    events, period will be set, and the time of each Event in the History must correspond; i.e. the EVENT.offset must be a multiple of period for each Event. Missing
    events in a period History are however allowed.
    
    NOTE: The invariants have NOT been written yet for this interface.
    """
    
    implements(IHistory)
    
    def __init__(self,origin,events,period,duration,summary,**kwargs):
        self.origin=origin
        self.events=events
        self.period
        self.duration=duration
        self.summary=summary
            
    def isPeriodic(): 
        u"""Indicates whether history is periodic. Returns Boolean"""
        
    def asHierarchy():
        u"""Returns CLUSTER. Generate a CEN EN13606-compatible hierarchy of the physical representation."""

class Event(Locatable):
    u"""
    Defines the abstract notion of a single event in a series. This class is generic,allowing types 
    to be generated which are locked to particular spatial types, such as EVENT<ITEM_LIST> Subtypes 
    express point or interval data.
    """
    
    implements(IEvent)
    
    def __init__(self,time,data,state,parent,offset,**kwargs):
        self.time=time
        self.data=data
        self.state=state
        self.parent=parent
        self.offset=offset
    

    def offsetValidity(event):
        
class PointEvent(Event):
    u"""
    Defines a single point event in a series.
    """    
    
    implements(IPointEvent)
    
    pass
    
class IntervalEvent(Event):
    u""" 
    Defines a single interval event in a series.
    
    """
    
    implements(IIntervalEvent)
    
    def __init__(self,width,mfunc,scount,**kwargs):
        self.width=width
        self.mathFunction=mfunc
        self.sampleCount=scount
                                      
    def intervalStartTime():
         u"""Start time of the interval of this event."""
         


    