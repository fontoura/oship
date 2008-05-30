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

from openehr.rm.datatypes.interfaces.idvordered import IDvOrdered 


_ = MessageFactory('oship')

class IDvQuantified(IDvOrdered):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """
    
    magnitude = Float(
        title=_(u"magnitude"),
        description=_(u"""Numeric value of the quantity in canonical (i.e. single value)
                          form. Implemented as constant, function or attribute in subtypes as
                          appropriate. The type OrdereNumeric is mapped to the available 
                          appropriate type in each implementation technology."""),
        required=True
    )
      
    magnitudeStatus = List(
        title=_(u"magnitudeStatus"),
        description=_(u"""Optional status of magnitude with values:
                                = : magnitude is a point value
                                < : value is < magnitude
                                > : value is > magnitude
                                <= : value is <= magnitude
                                >= : value is >= magnitude
                                ~ : value is approximately magnitude
                                If not present, meaning is =. """),
        required=True
    )
    
           
           
    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """


    magnitudeExists = Attribute(_(u" magnitude /= Void"))
    
    magnitudeStatusValid = Attribute(_(u"""magnitude_status /= Void implies
                                     valid_magnitude_status(magnitude_status)"""))


