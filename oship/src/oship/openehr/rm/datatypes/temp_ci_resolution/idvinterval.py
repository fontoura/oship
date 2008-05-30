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

from openehr.rm.datatypes.interfaces.idatavalue import IDataValue 


_ = MessageFactory('oship')

          
class IDvInterval(IDataValue):
    """
    Used to define intervals of dates, times, quantities (whose units match) and so on.
    The type parameter, T, must be a descendant of the type DV_ORDERED, which is
    necessary (but not sufficient) for instances to be compared (strictly_comparable
    is also needed).
    Without the DV_INTERVAL class, quite a few more DV_ classes would be needed
    to express logical intervals, namely interval versions of all the date/time classes,
    and of quantity classes. Further, it allows the semantics of intervals to be stated in
    one place unequivocally, including the conditions for strict comparison.
    The basic semantics are derived from the class INTERVAL<T>, described in the
    support RM.
    """

    pass
