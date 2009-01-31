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

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements 

from oship.openehr.rm.datatypes.basic.datavalue import DataValue
from oship.openehr.rm.datatypes.quantity.interfaces.dvordered import IDvOrdered

_= MessageFactory('oship')

class DvOrdered(DataValue):
    """
    Purpose:           
    Abstract class defining the concept of ordered values, which includes ordinals as
    well as true quantities. It defines the functions '<' and is_strictly_comparable_to,
    the latter of which must evaluate to True for instances being compared with the
    '<' function, or used as limits in the DV_INTERVAL<T> class.

    Use:    
    Data value types which are to be used as limits in the DV_INTERVAL<T> class
    must inherit from this class, and implement the function
    is_strictly_comparable_to to ensure that instances compare meaningfully. For
    example, instances of DV_QUANTITY can only be compared if they measure the
    same kind of physical quantity.
    """

    implements(IDvOrdered)
    
    def __init__(self, normalRange, otherReferenceRanges, normalStatus):
        self.normalRange = normalRange
        self.otherReferenceRanges = otherReferenceRanges
        self.normalStatus = normalStatus
                
    def __cmp__(self,other):
        isStrictlyComparableTo(other)
        
                
    def __lt__(self, other):
        if isinstance(other,self.__class__):
            return self.__dict__ < other.__dict__
        else:
            return False
        
    def isStrictlyComparableTo(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
        

    def isNormal(self):
        """ 
        Value is in the normal range, determined by comparison of the value to the normalRange 
        if present, or by the normalStatus marker if present.

        isNormal: Boolean
        require
        normalRange /= Void or normalStatus /= Void
        ensure
        normalRange /= Void implies Result = normalRange.has(Current)
        normalStatus /= Void implies normal_status.code_string.is_equal("N")
        """
        
        if self.normalStatus.codeString == "N":
            return True
        else:
            return self.value in self.normalRange # but we don't have a value in this abstract class in the specs
        
        
    def isSimple(self):
        """
        is_simple: Boolean 
        True if this quantity has no reference ranges.
        """
        if (self.normalRange is None or self.normalRange is []) and (self.otherReferenceRanges is None or self.otherReferenceRanges is []):
            return True
        else:
            return False
                  
