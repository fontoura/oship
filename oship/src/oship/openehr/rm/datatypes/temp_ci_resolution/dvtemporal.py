# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the date_time data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

In the specs the package is shown as data_types.quantity.date_time We have changed it 
in this implementation to datatypes.datetm

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.idvtemporal import IDvTemporal
from openehr.rm.datatypes.dvabsolutequantity import IDvAbsoluteQuantity


_ = MessageFactory('oship')


class DvTemporal(DvAbsoluteQuantity):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is
    DV_DURATION.
    """
    
    implements(IDvTemporal)
    
    def diff(other):
        return DvDuration(other,self.value)
