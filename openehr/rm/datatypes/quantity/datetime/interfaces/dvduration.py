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

from oship.openehr.rm.datatypes.quantity.dvamount import IDvAmount

_ = MessageFactory('oship')


class IDvDuration(IDvAmount):
    """
    Represents a period of time with respect to a notional point in time, which is not
    specified. A sign may be used to indicate the duration is "backwards" in time
    rather than forwards.
    
    Note that a deviation from ISO8601 is supported, allowing the 'W' designator to
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
