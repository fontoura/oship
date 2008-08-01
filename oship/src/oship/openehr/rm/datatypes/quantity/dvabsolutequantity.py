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
__contributors__ = u'Renato Pesca <rpesca@gmail.com>',u'Andre Goncalves <goncalves.aluiz@gmail.com'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements 

from oship.openehr.rm.datatypes.quantity.dvquantified import DvQuantified
from interfaces.dvabsolutequantity import IDvAbsoluteQuantity

_ = MessageFactory('oship')
  

class DvAbsoluteQuantity(DvQuantified):
    """
    Abstract class defining the concept of quantified entities whose values are abso-
    lute with respect to an origin. Dates and Times are the main example.
    """
    
    implements(IDvAbsoluteQuantity)
    
    
    def __init__(self,accuracy):
        DvQuantified.__init__(magnitude,magnitudeStatus)
        self.accuracy=accuracy
        
    def add():
        """(a_diff: like diff): like Current
        """
    
    def subtract():
        """(a_diff: like diff): like Current 
        """
        
    def diff():
        """(other: like Current): DV_AMOUNT
        """
    
           
 