# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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

from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.dvabsolutequantity import IDvAbsoluteQuantity,DvAbsoluteQuantity


_ = MessageFactory('oship')


class IDvTemporal(IDvAbsoluteQuantity):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is DvDuration.
    """

    pass

class DvTemporal(DvAbsoluteQuantity):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is
    DV_DURATION.
    """
    
    implements(IDvTemporal)
    
    def diff(other):
        return DvDuration(other,self.value)
