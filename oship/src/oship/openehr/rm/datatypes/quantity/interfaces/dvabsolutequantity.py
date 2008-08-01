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

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Float

from dvquantified import IDvQuantified

_ = MessageFactory('oship')
  
class IDvAbsoluteQuantity(IDvQuantified):
    """
    Abstract class defining the concept of quantified entities whose values are absolute with respect to an origin. Dates and Times are the main example.
    """
    
    accuracy = Float(
        title=_(u"Accuracy"),
        description=_(u"""Accuracy of measurement, expressed as a half-range value of the diff type for this quantity (i.e. an accuracy of x means +/- x)."""),
        required=False,
        )
    
    def __add__():
        """Addition of a diffential amount to this quantity"""
        
    def __sub__():
        """Result of a subtracting a differential amount from this quantity"""
        
    def diff():
        """Difference two quantities"""
