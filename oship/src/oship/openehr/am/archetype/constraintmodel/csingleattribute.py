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

class ICSingleAttribute(Interface):
    """
    Concrete model of constraint on a single valued attribute.
    """
    
    alternatives=List(
        title=_("Alternatives"),
        description=_("A list of alternative constraints for the single child of this attribute."),
        required=False,
    )

class CSingleAttribute(Field):
    """
    Concrete model of constraint on a single valued attribute.
    """
    
    implements(ICSingleAttribute)