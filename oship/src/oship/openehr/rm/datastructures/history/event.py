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
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.archetyped.locatable import Locatable 
from interfaces.event import IEvent

_ = MessageFactory('oship')

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
        
