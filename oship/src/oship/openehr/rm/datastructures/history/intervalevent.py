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


from zope.interface import implements,classProvides
from zope.i18nmessageid import MessageFactory

from event import Event
from interfaces.intervalevent import IIntervalEvent

_ = MessageFactory('oship')
    
class IntervalEvent(Event):
    u""" 
    Defines a single interval event in a series.
    
    """
    
    implements(IIntervalEvent)
    classProvides(IIntervalEvent)
    
    def __init__(self,width,mfunc,scount):
        self.width=width
        self.mathFunction=mfunc
        self.sampleCount=scount
                                      
    def intervalStartTime():
        u"""Start time of the interval of this event."""
         


    