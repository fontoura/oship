# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################
"""

These are the quantity data types interfaces from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.schema import Float
from openehr.rm.datatypes.interfaces.idvquantified import IDvQuantified 

_=MessageFactory('oship')
        
class IDvAbsoluteQuantity(IDvQuantified):
    """
    Abstract class defining the concept of quantified entities whose values are abso-
    lute with respect to an origin. Dates and Times are the main example.
    """
    
        
    accuracy = Float(
        title=_(u"Accuracy"),
        description=_(u"""Accuracy of measurement, expressed as a half-range value of the diff type 
                    for this quantity (i.e. an accuracy of x means +/−x)."""),
        required=False,
        )
    
