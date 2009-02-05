# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

The basic openEHR data types. From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contribuitors__= u'Otavio Silva otavio_uff104@yahoo.com.br'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.datatypes.basic.interfaces.datavalue import IDataValue

_ = MessageFactory('oship')

class DataValue(object):
    u""" 
    Abstract class. 
    Serves as a common ancestor of all data value types in openEHR models.
    """
    
    implements(IDataValue)

    pass
