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

In the specs the package is shown as data_types.quantity.date_time We have changed it 
in this implementation to datatypes.datetime

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory

from dvtemporal import IDvTemporal

_ = MessageFactory('oship')


class IDvDate(IDvTemporal):
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

