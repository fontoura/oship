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

from datetime import datetime
from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.datatypes.quantity.datetime.dvtemporal import DvTemporal
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime

_ = MessageFactory('oship')

class DvDateTime(DvTemporal):
    u"""
    Represents an absolute point in time, specified to the second. Semantics defined by ISO 8601.
    Used for recording a precise point in real world time, and for approximate time
    stamps, e.g. the origin of a HISTORY in an OBSERVATION which is only partially known.
    """

    implements(IDvDateTime)

    def __init__(self,value):
        # need to separate value into a Python tuple to submit to the datetime module.
        #self.value=datetime(value)
        self.value=datetime.now()
        self.__name__=''
        

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

