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

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import List

from openehr.rm.datatypes.basic.interfaces.datavalue import IDataValue
from openehr.rm.datatypes.quantity.dvinterval import DvInterval
from openehr.rm.datatypes.text.codephrase import CodePhrase

_= MessageFactory('oship')

class IDvOrdered(IDataValue):
    """
    Purpose:           
    Abstract class defining the concept of ordered values, which includes ordinals as
    well as true quantities. It defines the functions ‘<’ and is_strictly_comparable_to,
    the latter of which must evaluate to True for instances being compared with the
    ‘<’ function, or used as limits in the DV_INTERVAL<T> class.

    Use:    
    Data value types which are to be used as limits in the DV_INTERVAL<T> class
    must inherit from this class, and implement the function
    is_strictly_comparable_to to ensure that instances compare meaningfully. For
    example, instances of DV_QUANTITY can only be compared if they measure the
    same kind of physical quantity.
    """
    
    normalRange = DvInterval(
        title = _(u"normalRange"),
        description = _(u"""Optional normal range."""),
        required = False
        )
    
    otherReferenceRanges = List(
        title = _(u"otherReferenceRanges"),
        description = _(u"""Optional tagged other reference ranges for this value in 
                      its particular measurement context. A list of ReferenceRange types."""),
        required = False
        )
    
    normalStatus = CodePhrase('','',
        title = _(u"normalStatus"),
        description = _(u"""Optional normal status indicator of value with respect to normal 
                     range for this value. Often included by lab, even if the normal range 
                     itself is not included. Coded by ordinals in series HHH, HH, H, 
                     (nothing), L, LL, LLL; see openEHR terminology group “normal status”."""),
        required = False
    )
                
       
    def isStrictlyComparableTo(other):
        """Test if two instances are strictly comparable. Called by object.__cmp__"""


    def isNormal():
        """ 
        Value is in the normal range, determined by comparison of the value to the normalRange 
        if present, or by the normalStatus marker if present.

        isNormal: Boolean
        require
        normalRange /= Void or normalStatus /= Void
        ensure
        normalRange /= Void implies Result = normalRange.has(Current)
        normalStatus /= Void implies normal_status.code_string.is_equal(“N”)
        """
        
        
    def isSimple():
        """
        is_simple: Boolean 
        True if this quantity has no reference ranges.
        """
                  
