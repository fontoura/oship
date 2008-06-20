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
from zope.schema import Int
from zope.i18nmessageid import MessageFactory

from openehr.rm.datastructures.event import IEvent,Event
from openehr.rm.datatypes.dvduration import DvDuration
from openehr.rm.datatypes.dvcodedtext import DvCodedText


_ = MessageFactory('oship')


class IIntervalEvent(IEvent):
    u""" 
    Defines a single interval event in a series.
    """
    
    width=DvDuration(
        title=_(u"width"),
        description=_(u"""Length of the interval during which the state was true. 
                      Void if an instantaneous event. OSHIP NOTE: The specs indicate 
                      this attribute is required but the text says it is Void if instantaneous.
                      How should this conflict be resolved?"""),
        required=True
    )
    
    mathFunction=DvCodedText(
        title=_(u"mathFunction"),
        description=_(u"""Mathematical function of the data of this event, e.g. “maximum”, “mean” etc. 
                      Coded using openEHR Terminology group “event math function”."""),
        required=True
    )
    
    sampleCount=Int(
        title=_(u"sampleCount"),
        description=_(u"""Optional count of original samples to which this event corresponds."""),
        required=False
    )
    
                              
    def intervalStartTime():
        u"""Start time of the interval of this event."""
         


    
class IntervalEvent(Event):
    u""" 
    Defines a single interval event in a series.
    
    """
    
    implements(IIntervalEvent)
    
    def __init__(self,width,mfunc,scount,**kw):
        self.width=width
        self.mathFunction=mfunc
        self.sampleCount=scount
        for n,v in kw.items():
            setattr(self,n,v)
                                      
    def intervalStartTime():
        u"""Start time of the interval of this event."""
         


    