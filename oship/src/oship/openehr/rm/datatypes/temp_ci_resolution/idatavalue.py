# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The basic openEHR data types interfaces. From the data types specification Rev 2.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.schema.interfaces import IField
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('oship')

class IDataValue(IField):
    """
    Serves as a common ancestor of all data value types in openEHR models.
    """

    pass
