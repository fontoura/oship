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

from zope.schema import Set,Int
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.support.interval import Interval
from cprimitive import ICPrimitive

_ = MessageFactory('oship')


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
    
