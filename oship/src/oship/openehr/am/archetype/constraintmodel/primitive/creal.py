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

class ICReal(ICPrimitive):
    """
    Constraints on instances of Real
    """
    
    list=Set(
        title_("List"),
        description=_("Set of Reals specifying constraint"),
        required=False,
    )


    range=Interval(
        title_("Range"),
        description=_(" "),
        required=False,
    )

    assumedValue=Float(
        title_("Assumed Value"),
        description=_(""),
        required=True,
    )

class CReal(CPrimitive):
    """
    Constraints on instances of Real
    """
    
    implements(ICReal)
    
