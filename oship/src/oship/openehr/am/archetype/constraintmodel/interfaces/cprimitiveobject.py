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

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

class ICPrimitiveObject(ICDefinedObject):
    """
    Constraint on a primitive object.
    """
    
    anyAllowed=Bool(
        title=_("Any Allowed"),
        description=_("True if any value of the type being constrained is allowed."),
        required=True,
    )
    
    item=CPrimitive(
        title=_("Item"),
        description=_("Object actually defining the constraint."),
        required=False,
    )
   
class CPrimitiveObject(CDefinedObject):
    """
    Constraint on a primitive object.
    """
    
    implements(ICPrimitiveObject)
