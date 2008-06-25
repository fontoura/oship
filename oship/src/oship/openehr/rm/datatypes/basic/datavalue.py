# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The basic openEHR data types. From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements 
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory 

from interfaces.datavalue import IDataValue

_ = MessageFactory('oship')

class DataValue(Field):
    """ 
    Abstract class. 
    Serves as a common ancestor of all data value types in openEHR models.
    """
    
    implements(IDataValue)

    pass
