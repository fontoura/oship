# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the quantity data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'restructuredtext'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements 

from openehr.rm.datatypes.dvquantified import DvQuantified
from openehr.rm.datatypes.interfaces.idvabsolutequantity import IDvAbsoluteQuantity


_ = MessageFactory('oship')
        
class DvAbsoluteQuantity(DvQuantified):
    """
    Abstract class defining the concept of quantified entities whose values are abso-
    lute with respect to an origin. Dates and Times are the main example.
    """
    
    implements(IDvAbsoluteQuantity)
    
    def __init__(self,accuracy):
        self.accuracy=accuracy
           
 