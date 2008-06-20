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

class IConstraintRef(ICReferenceObject):
    """
    Reference to a constraint described in the same archetype.
    """
    
    reference=TextLine(
        title=_("Reference"),
        description=_("Reference to a constraint in the archetype ontology."),
        required=True,
    )
    
class ConstraintRef(CReferenceObject):
    """
    Reference to a constraint described in the same archetype.
    """
    
    implements(IConstraintRef)
