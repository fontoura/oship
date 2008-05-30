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

from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.idvtime import IDvTime
from openehr.rm.datatypes.dvtemporal import DvTemporal


_ = MessageFactory('oship')

        
class DvTime(DvTemporal):
    u"""
    Represents an absolute point in time from an origin usually interpreted as meaning the start 
    of the current day, specified to the second. Semantics defined by ISO8601.
    
    Used for recording real world times, rather than scientifically measured fine
    amounts of time. The partial form is used for approximate times of events and
    substance administrations. 
    """

    implements(IDvTime)

    def __init__(self,value):
        self.value=time(value)

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
        return True