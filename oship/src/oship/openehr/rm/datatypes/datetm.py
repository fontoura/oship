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
Quantity Package Rev. 2.1.0.

In the specs the package is shown as data_types.quantity.date_time We have changed it 
in this implementation to datatypes.datetm

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from datetime import datetime
from time import time
from zope.interface import implements 
from zope.schema import TextLine,Field 
from zope.i18nmessageid.message import MessageFactory

"""
    OSHIP supports a common subset of ISO8601 strings for input. Partial dates are not yet supported.
    You must pass at least YYYY-MM-DD HH:MM even if they are zero filled. 
    OSHIP output is supported fully using the Python isoformat() method.
    The datetime parser is from the zc.iso8601 egg it needs to be expanded and I also 
    wanted to rename it so it has been placed in the utils package.
"""    
from utils.iso8601parser import isodt
from utils.iso8601parser import isodtz
from openehr.rm.support import *
from openehr.rm.datatypes.quantity import *
from openehr.rm.datatypes.interfaces.datetm import *


_ = MessageFactory('oship')


class DvTemporal(DvAbsoluteQuantity):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is
    DV_DURATION.
    """




class DvDate(DvTemporal):
    """
    Represents an absolute point in time, as measured on the Gregorian calendar, and
    specified only to the day. Semantics defined by ISO 8601.
    Used for recording dates in real world time. The partial form is used for 
    approximate birth dates, dates of death, etc.  
    
    """

    implements(IDvDate)

    def __init__(self,value,**kwargs):
        if value==None or value=='':
            value=datetime.date().isoformat()
            
        try:
            self.value=isodt(value).date()
        except ValueError:
            self.value=isodtz(value).date()
            
        Field.__init__(self,**kwargs)


    def diff(other):
        """Difference of two dates. Returns a Dv_Duration"""
        return other-self.value
        
    def magnitude():
        """ Returns the numeric value of the date as days since the calendar origin point 1/1/0000"""
        return self.value.toordinal()

    def valueValid(): 
        u"""validIso8601Date(value)"""
        
class DvTime(DvTemporal):
    u"""
    Represents an absolute point in time from an origin usually interpreted as meaning the start 
    of the current day, specified to the second. Semantics defined by ISO8601.
    
    Used for recording real world times, rather than scientifically measured fine
    amounts of time. The partial form is used for approximate times of events and
    substance administrations. 
    """

    implements(IDvTime)

    def __init__(self,value='',**kwargs):
        if value==None or value=='':
            value=time.time().isoformat()
        try:
            self.value=isodt(value).time()
        except ValueError:
            self.value=isodtz(value).time()
            
        Field.__init__(self,**kwargs)

    def diff(other):
        u"""Difference of two times. Returns a DvDuration"""
        return other-self.value
        
        
    def magnitude():
        u"""
        Returns the numeric value of the seconds since midnight.
        Result >= 0.0        
        """
        n=time.localtime()
        y,m,d,z=n[0],n[1],n[2],n[8]
        return time.mktime(n)-time.mktime((y,m,d,0,0,0,0,z))


    def valueValid(): 
        u"""validIso8601Time(value)"""

class DvDateTime(DvTemporal):
    u"""
    Represents an absolute point in time, specified to the second. Semantics defined by ISO 8601.
    Used for recording a precise point in real world time, and for approximate time
    stamps, e.g. the origin of a HISTORY in an OBSERVATION which is only partially known.
    """

    implements(IDvDateTime)

    def __init__(self,value,**kwargs):
        if value==None or value=='':
            value=datetime.today().isoformat()
        try:
            self.value=isodt(value)
        except ValueError:
            self.value=isodtz(value)
            
        Field.__init__(self,**kwargs)

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


class DvDuration(DvAmount):
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

    def __init__(self,value,**kwargs):
        self.value=value
        Field.__init__(self,**kwargs)

    def magnitude():
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """
        
        

    def valueValid(): 
        u"""validIso8601Duration(value)"""





    
    