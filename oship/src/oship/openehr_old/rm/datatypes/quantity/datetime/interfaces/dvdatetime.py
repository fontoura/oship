# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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


class IDvDateTime(IDvTemporal):
    """
    Represents an absolute point in time, specified to the second. Semantics defined by ISO 8601.
    Used for recording a precise point in real world time, and for approximate time
    stamps, e.g. the origin of a HISTORY in an OBSERVATION which is only partially known.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 date/time string"""),
        required=True,
        )

    def diff(other):
        """Difference of two date/times. Returns a DvDuration"""
        
        
    def magnitude():
        """
        numeric value of the date/time as seconds since the calendar origin point.
        Result >= 0.0        
        """


    def valueValid(): 
        """validIso8601DateTime(value)"""
