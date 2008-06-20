# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
These are the interfaces for the am.archetype.primitive package defined in 
The Archetype Object model Rev 2.0.2
"""
__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import Interface
from zope.schema import *

class ICInteger(ICPrimitive):
    """
    Constraint on integers.
    """
    
    list=Set(
        title_("List"),
        description=_("Set of integers specifying constraints."),
        required=False,
    )
    
    range=Interval(
        title_("Range"),
        description=_("Range of integers specifying constraint."),
        required=False,
    )
    
    assumedValue=Int(
        title_("Assumed Value"),
        description=_("The value to assume if this item is not in the data."),
        required=True,
    )
    
class CInteger(CPrimitive):
    """
    Constraint on integers.
    """
    
    implements(ICInteger)