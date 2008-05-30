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
DateTime Package Rev. 2.1.0.

In the specs the package is shown as data_types.quantity.date_time We have changed it 
in this implementation to data_types.datetm 

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.interfaces.idvabsolutequantity import IDvAbsoluteQuantity



_ = MessageFactory('oship')


class IDvTemporal(IDvAbsoluteQuantity):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is DvDuration.
    """

    pass
