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
from zope.schema import Field
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.locatable import ILocatable,Locatable 
from openehr.rm.datatypes.dvdatetime import DvDateTime
from openehr.rm.datatypes.dvduration import DvDuration
from openehr.rm.datastructures.itemstructure import ItemStructure 
from openehr.rm.datastructures.history import History 


_ = MessageFactory('oship')

class IEvent(ILocatable):
    u"""
    Defines the abstract notion of a single event in a series. This class is generic,allowing types 
    to be generated which are locked to particular spatial types, such as EVENT<ITEM_LIST> Subtypes 
    express point or interval data.
    """
    
    time=DvDateTime(
        title=_(u'time'),
        description=_(u"""Time of this event. If the width is non-zero, it is the time point of the 
                         trailing edge of the event."""),
        required=True
    )
    
            
    data=Field(
        title=_(u'data'),
        description=_(u'The data of this event.'),
        required=True
    )
    
    state=ItemStructure(
        title=_(u'state'),
        description=_(u'Optional state information.for this event.'),
        required=False
    )
    
    parent=History(
        title=_(u'parent'),
        description=_(u'redefinition of LOCATABLE.parent to type of History'),
        required=True
    )
    
    offset=DvDuration(
        title=_(u'offset'),
        description=_(u'Offset of this event from origin, computed as time.diff(parent.origin)'),
        required=True
    )

    def offsetValidity(event):
        u'is the offset valid?' 

class Event(Locatable):
    u"""
    Defines the abstract notion of a single event in a series. This class is generic,allowing types 
    to be generated which are locked to particular spatial types, such as EVENT<ITEM_LIST> Subtypes 
    express point or interval data.
    """
    
    implements(IEvent)
    
    def __init__(self,time,data,state,parent,offset,**kw):
        self.time=time
        self.data=data
        self.state=state
        self.parent=parent
        self.offset=offset
        for n,v in kw.items():
            setattr(self,n,v)
    

    def offsetValidity(event):
        u"""is the offset valid?""" 
        
