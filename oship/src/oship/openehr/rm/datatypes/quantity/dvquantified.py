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
__contributors__ = u'Renato Pesca <rpesca@gmail.com>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements 

from oship.openehr.rm.datatypes.quantity.dvordered import DvOrdered
from oship.openehr.rm.datatypes.quantity.interfaces.dvquantified import IDvQuantified

_ = MessageFactory('oship')
              
class DvQuantified(DvOrdered):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """

    def __init__(self,magnitude,magnitudeStatus):
        DvOrdered.__init__(normalRange,otherReferenceRanges,normalStatus)
        self.magnitude=magnitude
        self.magnitudeStatus=magnitudeStatus
           
        magnitudeExists = self.magnitude!=None
        
        magnitudeStatusValid = val in self.magnitudeStatus
        
    def magnitudeExists():
        return self.magnitude!=None
        
    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """
        if(magnitudeExists()):
            if val == "=" or val == ">=" or val == "<=" or val == ">" or val == "<" or val == "~":
                return True
        else:
            return False
        