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

from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.datatypes.quantity.dvamount import DvAmount
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvduration import IDvDuration

_ = MessageFactory('oship')

class DvDuration(DvAmount):
    u"""
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

    implements(IDvDuration)

    def __init__(self,value,**kw):
        self.value=value
        self.__name__=''
        for n,v in kw.items():
            setattr(self,n,v)

    def magnitude():
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """
        
        

    def valueValid(): 
        u"""validIso8601Duration(value)"""





    
    