# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema import Set,Bool
from zope.i18nmessageid.message import MessageFactory 

from cdefinedobject import ICDefinedObject

_ = MessageFactory('oship')


class ICComplexObject(ICDefinedObject):
    """
    Constraint on complex objects.
    """
    
    attributes=Set(
        title=_("Attributes"),
        description=_("List of constraints on attributes of the reference model."),
        required=False,
    )

    anyAllowed=Bool(
        title=_("Any Allowed"),
        description=_("True if any value of the reference model is allowed."),
        required=True,
    )
