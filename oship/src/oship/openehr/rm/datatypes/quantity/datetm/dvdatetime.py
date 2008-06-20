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

from zope.interface import implements 
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.dvtemporal import DvTemporal,IDvTemporal


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

class DvDateTime(DvTemporal):
    u"""
    Represents an absolute point in time, specified to the second. Semantics defined by ISO 8601.
    Used for recording a precise point in real world time, and for approximate time
    stamps, e.g. the origin of a HISTORY in an OBSERVATION which is only partially known.
    """

    implements(IDvDateTime)

    def __init__(self,value):
        self.value=datetime(value)

    def diff(other):
        u"""Difference of two date/times. Returns a DvDuration"""
        return self.value-other
        
    def magnitude():
        u"""
        numeric value of the date/time as seconds since the calendar origin point.
        Result >= 0.0        
        """
        return time.time()

    def valueValid(): 
        u"""validIso8601DateTime(value)"""


class DvDuration(DvAmount, datetime):
    u"""
    Represents a period of time with respect to a notional point in time, which is not
    specified. A sign may be used to indicate the duration is “backwards” in time
    rather than forwards.
    
    Note that a deviation from ISO8601 is supported, allowing the ‘W’ designator to
    be mixed with other designators. See assumed types section in the Support IM.

    Used for recording the duration of something in the real world, particularly when
    there is a need a) to represent the duration in customary format, i.e. days, hours,
    minutes etc, and b) if it will be used in computational operations with date/time
    quantities, i.e. additions, subtractions etc.
    """

    implements(IDvDuration)

    def __init__(self,value):
        self.value=value
        
    def magnitude():
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """
        
        

    def valueValid(): 
        u"""validIso8601Duration(value)"""

