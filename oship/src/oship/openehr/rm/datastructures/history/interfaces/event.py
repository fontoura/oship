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

from zope.schema import Field, Object
from zope.i18nmessageid import MessageFactory


from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvduration import IDvDuration
from oship.openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure 
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef

_ = MessageFactory('oship')

class IEvent(ILocatable):
    u"""
    Defines the abstract notion of a single event in a series. This class is generic,allowing types 
    to be generated which are locked to particular spatial types, such as EVENT<ITEM_LIST> Subtypes 
    express point or interval data.
    """
    
    time=Object(
        schema=IDvDateTime,
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
    
    state=Object(
        schema=IItemStructure,
        title=_(u'state'),
        description=_(u'Optional state information.for this event.'),
        required=False
    )
    
    parent=Object(
        schema=IObjectRef,
        title=_(u'parent'),
        description=_(u'redefinition of LOCATABLE.parent to type of History'),
        required=True
    )
    
    offset=Object(
        schema=IDvDuration,
        title=_(u'offset'),
        description=_(u'Offset of this event from origin, computed as time.diff(parent.origin)'),
        required=True
    )

    def offsetValidity(event):
        u'is the offset valid?' 
