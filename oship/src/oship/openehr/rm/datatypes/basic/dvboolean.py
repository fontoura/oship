# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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
from zope.schema import Bool 
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.datatypes.basic.interfaces.dvboolean import IDvBoolean

_ = MessageFactory('oship')


class DvBoolean(Bool):
    """ 
    Items which are truly boolean data, such as true/false or yes/no answers.
    For such data, it is important to devise the meanings (usually questions in subjec-
    tive data) carefully, so that the only allowed results are in fact true or false.
    The DV_BOOLEAN class should not be used as a replacement for naively modelled
    enumerated types such as male/female etc. Such values should be coded, and in
    any case the enumeration often has more than two values.  

    You cannot subclass bool() in Python.  The solution is to assign a private variable 
    with the bool() result of the value passed at instantiation.
    
    Example:
    
    >>>obj = DvBoolean(0)
    >>>obj.value
    >>>False
    
    """

    implements(IDvBoolean)

    def __init__(self, value):
        self.value=bool(value)
        