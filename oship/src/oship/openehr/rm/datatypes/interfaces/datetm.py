# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################
"""

These are the date_time data types from Data Types Information Model
DateTime Package Rev. 2.1.0.

In the specs the package is shown as data_types.quantity.date_time We have changed it 
in this implementation to data_types.datetm 

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.interface import implements
from zope.interface import invariant

from zope.schema.interfaces import IDate, IDatetime, ITime, ITimedelta
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.interfaces.basic import *
from openehr.rm.datatypes.interfaces.text import *
from openehr.rm.datatypes.interfaces.quantity import *
from openehr.rm.datatypes.text import DvCodedText



_ = MessageFactory('oship')


class IDvTemporal(IDvAbsoluteQuantity):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is DvDuration.
    """




class IDvDate(IDvTemporal, IDate):
    """
    Represents an absolute point in time, as measured on the Gregorian calendar, and
    specified only to the day. Semantics defined by ISO 8601.
    Used for recording dates in real world time. The partial form is used for 
    approximate birth dates, dates of death, etc.   
    """
    
    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 date string"""),
        required=True,
        )

    def diff(other):
        """Difference of two dates. Returns a Dv_Duration"""
        
        
    def magnitude():
        """ Returns the numeric value of the date as days since the calendar origin point 1/1/0000"""


    def valueValid(): 
        """validIso8601Date(value)"""
        
class IDvTime(IDvTemporal, ITime):
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

class IDvDateTime(IDvTemporal, IDatetime):
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


class IDvDuration(IDvAmount, ITimedelta):
    """
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

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 duration"""),
        required=True,
        )     
        
    def magnitude():
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """


    def valueValid(): 
        """validIso8601Duration(value)"""
