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

from zope.schema import Set,Float
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.support.interval import Interval
from oship.openehr.am.archetype.constraintmodel.primitive.interfaces.cprimitive import ICPrimitive

_ = MessageFactory('oship')

class ICReal(ICPrimitive):
    """
    Constraints on instances of Real
    """
    
    list_=Set(
        title=_(u"List"),
        description=_(u"Set of Reals specifying constraint"),
        required=False,
    )

    """ Interval is no a Zope schema field
    range=Interval(
        title=_(u"Range"),
        description=_(u" "),
        required=False,
    )
    """
    
    assumedValue=Float(
        title=_(u"Assumed Value"),
        description=_(u""),
        required=True,
    )

