# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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
from zope.schema import Float,TextLine,Int

from dvamount import IDvAmount

_ = MessageFactory('oship')

class IDvQuantity(IDvAmount):
    """
    Quantitified type representing scientific quantities, i.e. quantities expressed as a
    magnitude and units.
    Units were inspired by the Unified Code for Units of Measure (UCUM), devel-
    oped by Gunther Schadow and Clement J. McDonald of The Regenstrief Institute.
        
    Can also be used for time durations, where it is more convenient to treat these as
    simply a number of seconds rather than days, months, years.
    """

    magnitude = Float(
        title=_(u"Magnitude"),
        description=_(u"""Numeric magnitude of the quantity."""),
        required=True
        )
    
    units = TextLine(
        title=_(u"Units"),
        description=_(u"""Stringified units, expressed in UCUM unit syntax, 
                    e.g. "kg/m2", "mm[Hg]", "ms-1", "km/h".Implemented accordingly in subtypes."""),
        required=True,
        )

    
    precision = Int(
        title=_(u"Precision"),
        description=_(u"""Precision to which the value of the quantity is expressed, in terms of 
                    number of decimal places. The value 0 implies an integral quantity.
                    The value -1 implies no limit, i.e. any number of decimal places."""),        
        required=False,
        #constraint = precisionValid
        )
    def precisionValid():
        """Precision must be >= -1"""
            
    def isIntegral():
        """True if precision = 0; quantity represents an integral number."""

    
    def isStrictlyComparableTo(other):
        """Test if two instances are strictly comparable by ensuring that the measured 
        property is the same, achieved using the Measurement service function units_equivalent.
        
        Return selfunits == other.units
        """
        
    
