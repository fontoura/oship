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

from zope.schema import Bool,Object
from zope.i18nmessageid.message import MessageFactory 

from cdefinedobject import ICDefinedObject
from openehr.am.archetype.constraintmodel.primitive.interfaces.cprimitive import ICPrimitive
_ = MessageFactory('oship')


class ICPrimitiveObject(ICDefinedObject):
    """
    Constraint on a primitive object.
    """
    
    anyAllowed=Bool(
        title=_(u"Any Allowed"),
        description=_(u"True if any value of the type being constrained is allowed."),
        required=True,
    )
    
    item=Object(
        schema=ICPrimitive,
        title=_(u"Item"),
        description=_(u"Object actually defining the constraint."),
        required=False,
    )
   
