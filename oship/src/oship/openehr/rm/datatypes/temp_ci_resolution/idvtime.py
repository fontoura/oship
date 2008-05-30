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


from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.interfaces.idvtemporal import IDvTemporal

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
