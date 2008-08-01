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

from oship.openehr.rm.support.interval import Interval
from oship.openehr.am.archetype.constraintmodel.interfaces.cprimitive import ICPrimitive

_ = MessageFactory('oship')


class ICInteger(ICPrimitive):
    """
    Constraint on integers.
    """
    
    list=Set(
        title=_(u"List"),
        description=_(u"Set of integers specifying constraints."),
        required=False,
        value_type=Int,
    )
    
    range=Interval(
        title=_(u"Range"),
        description=_(u"Range of integers specifying constraint."),
        required=False,
    )
    
    assumedValue=Int(
        title=_(u"Assumed Value"),
        description=_(u"The value to assume if this item is not in the data."),
        required=True,
    )
    
