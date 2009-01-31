# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__Contributor__ = u'Roberto Cunha <roliveiracunha@yahoo.com.br>'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.datatypes.quantity.dvabsolutequantity import DvAbsoluteQuantity
from interfaces.dvtemporal import IDvTemporal

_ = MessageFactory('oship')

class DvTemporal(DvAbsoluteQuantity):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is
    DV_DURATION.
    """
    
    implements(IDvTemporal)
    
    
    def diff(other):
        return DvDuration(other,self.value)
