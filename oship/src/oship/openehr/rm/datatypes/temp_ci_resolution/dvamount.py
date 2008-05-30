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
from openehr.rm.datatypes.interfaces.idvamount import IDvAmount

_ = MessageFactory('oship')
   
class DvAmount(DvQuantified):
    """   
    Abstract class defining the concept of relative quantified ‘amounts’. For relative
    quantities, the ‘+’ and ‘-’ operators are defined (unlike descendants of
    DV_ABSOLUTE_QUANTITY, such as the date/time types).
    """
    
    implements(IDvAmount)
    
    def __init__(self,accuracy,accuracyIsPercent):
        self.accuracy=accuracy
        self.accuracyIsPercent=accuracyIsPercent

    
    def validPercentage(val):
        """
        Test whether a number is a valid percentage,i.e. between 0 and 100.
        ensure
        Result implies val >= 0.0 and val <= 100.0
        """
        
        return val>=0 and val<=100
    
    