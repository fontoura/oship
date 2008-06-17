# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
The text data types interfaces. From the data types specification Rev 2.1.0
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'



from zope.schema.interfaces import IField  
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.idatavalue import IDataValue

_ = MessageFactory('oship')

