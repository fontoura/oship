# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From Data Types Information Model
Quantity Package Rev. 2.1.0.
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory

from dvtemporal import IDvTemporal


_ = MessageFactory('oship')


class IDvTime(IDvTemporal):
    """
    Represents an absolute point in time from an origin usually interpreted as meaning the start 
    of the current day, specified to the second. Semantics defined by ISO8601.
    
    Used for recording real world times, rather than scientifically measured fine
    amounts of time. The partial form is used for approximate times of events and
    substance administrations. 
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 time string"""),
        required=True,
        )

    def diff(other):
        """Difference of two times. Returns a DvDuration"""
        
        
    def magnitude():
        """
        Returns the numeric value of the seconds since midnight.
        Result >= 0.0        
        """


    def valueValid(): 
        """validIso8601Time(value)"""
        
