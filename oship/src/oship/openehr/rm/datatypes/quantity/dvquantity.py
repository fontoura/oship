# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
From the quantity data types from Data Types Information Model
Quantity Package Rev. 2.1.0.
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__Contributors__ = u'Roberto Cunha <roliveiracunha@yahoo.com.br>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements

from oship.openehr.rm.datatypes.quantity.interfaces.dvquantity import IDvQuantity
from oship.openehr.rm.datatypes.quantity.dvamount import DvAmount

_ = MessageFactory('oship')       

class DvQuantity(DvAmount):
    """
    Quantitified type representing "scientific" quantities, i.e. quantities expressed as a
    magnitude and units.
    Units were inspired by the Unified Code for Units of Measure (UCUM), devel-
    oped by Gunther Schadow and Clement J. McDonald of The Regenstrief Institute.
        
    Can also be used for time durations, where it is more convenient to treat these as
    simply a number of seconds rather than days, months, years.
    """
    
    implements(IDvQuantity)
   
    def __init__(self,magnitude,units,precision):
        self.magnitude=magnitude
        self.units=units
        self.precision=precision
        
    def precisionValid():
        return precision >= -1
    
    def isIntegral():
        """True if precision = 0; quantity represents an integral number."""
        return precision==0

    
    def isStrictlyComparableTo(other):
        """
        Test if two instances are strictly comparable by ensuring that the measured 
        property is the same, achieved using the Measurement service function units_equivalent.
        """
        if(isinstance(other, self.__class__)): #
            return self.units==other.units and self.magnitude==other.magnitude
      