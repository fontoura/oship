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

from zope.schema import Int,Object
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.datastructures.history.interfaces.event import IEvent
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvduration import IDvDuration
from oship.openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText


_ = MessageFactory('oship')


class IIntervalEvent(IEvent):
    u""" 
    Defines a single interval event in a series.
    """
    
    width=Object(
        schema=IDvDuration,
        title=_(u"width"),
        description=_(u"""Length of the interval during which the state was true. 
                      Void if an instantaneous event. OSHIP NOTE: The specs indicate 
                      this attribute is required but the text says it is Void if instantaneous.
                      How should this conflict be resolved?"""),
        required=True
    )
    
    mathFunction=Object(
        schema=IDvCodedText,
        title=_(u"mathFunction"),
        description=_(u"""Mathematical function of the data of this event, e.g. "maximum", "mean" etc. 
                      Coded using openEHR Terminology group "event math function"."""),
        required=True
    )
    
    sampleCount=Int(
        title=_(u"sampleCount"),
        description=_(u"""Optional count of original samples to which this event corresponds."""),
        required=False
    )
    
                              
    def intervalStartTime():
        u"""Start time of the interval of this event."""
         

