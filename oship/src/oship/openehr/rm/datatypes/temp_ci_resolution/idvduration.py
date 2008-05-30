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

from openehr.rm.datatypes.interfaces.idvamount import IDvAmount
_ = MessageFactory('oship')


class IDvDuration(IDvAmount):
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
        descripion=_(u"""ISO8601 duration"""),
        required=True,
        )     
        
    def magnitude():
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """


    def valueValid(): 
        """validIso8601Duration(value)"""
