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

class ICAttribute(Interface):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    rmAttributeName=TextLine(
        title=_("RM Attribute Name"),
        description=_("Reference model attribute within the enclosed type representedby a CObject."),
        required=True,
    )
    
    existence=Interval(
        title=_("Existence"),
        description=_("Indicates whether the target object exists or not."),
        required=True,
    )

    children=List(
        title=_("Children"),
        description=_("Child constraint nodes."),
        required=False,
    )

class CAttribute(Field):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    implements(ICAttribute)