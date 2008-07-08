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

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.schema import Bool
from zope.schema.interfaces import IBool 
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class IDvBoolean(IBool):
    """
    Items which are truly boolean data, such as true/false or yes/no answers.
    The invariant defined in the spec for this class is that it is not void.  
    In Python a 'None' is defined as False.
    """
    
    value = Bool(
        title = _(u"value"),
        description = _(u"The boolean value of this item."),
        required = True,
        default = False
    )

