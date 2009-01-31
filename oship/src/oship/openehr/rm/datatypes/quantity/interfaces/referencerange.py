# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Object

from oship.openehr.rm.datatypes.quantity.interfaces.dvordered import IDvOrdered
from oship.openehr.rm.datatypes.text.interfaces.dvtext import IDvText
from oship.openehr.rm.datatypes.quantity.interfaces.dvinterval import IDvInterval


_ = MessageFactory('oship')

class IReferenceRange(IDvOrdered):
    """
    Defines a named range to be associated with any ORDERED datum. Each such
    range is particular to the patient and context, e.g. sex, age, and any other factor
    which affects ranges.
    May be used to represent normal, therapeutic, dangerous, critical etc ranges.
    """
    
    meaning=Object(
        schema=IDvText,
        title=_(u"meaning"),
        description=_(u"""Term whose value indicates the meaning of this range,  e.g. "normal", "critical", "therapeutic" etc."""),
        required=True
        )
    
    range=Object(
        schema=IDvInterval,
        title=_(u"range"),
        description=_(u"""The data range for this meaning, e.g."critical" etc."""),
        required=True
        )

    def isInRange(val):
        """
        Indicates if the value 'val' is inside the range
        """
