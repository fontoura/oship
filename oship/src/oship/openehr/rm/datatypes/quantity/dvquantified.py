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
from zope.interface import implements 

from dvordered import DvOrdered
from interfaces.dvquantified import IDvQuantified

_ = MessageFactory('oship')
              
class DvQuantified(DvOrdered):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """

    def __init__(self,magnitude,magnitudeStatus):
        self.magnitude=magnitude
        self.magnitudeStatus=magnitudeStatus
           
        magnitudeExists = self.magnitude!=None
        
        magnitudeStatusValid = val in self.magnitudeStatus
        
    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """

