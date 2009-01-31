# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.schema import Bool
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.constraintmodel.primitive.interfaces.cprimitive import ICPrimitive

_ = MessageFactory('oship')

class ICBoolean(ICPrimitive):
    """
    Boolean constraint.
    """
    
    trueValid=Bool(
        title=_(u"True Valid"),
        description=_(u"True if value True is allowed."),
        required=True,
    )
    
    falseValid=Bool(
        title=_(u"False Valid"),
        description=_(u"True if the value False is allowed."),
        required=True,
    )
    
    assumedValue=Bool(
        title=_(u"Assumed Value"),
        description=_(u"The value to assume of this item is not included in the data."),
        required=True,
    )
    
