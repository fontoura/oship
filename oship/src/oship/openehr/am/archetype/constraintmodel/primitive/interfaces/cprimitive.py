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
from zope.schema import Field,Bool
from zope.schema.interfaces import IField
from zope.i18nmessageid.message import MessageFactory

_ = MessageFactory('oship')

class ICPrimitive(IField):
    """
    Abstract super type of all primitive types.
    """
    
    defaultValue=Field(
        title=_(u"Default Value"),
        description=_(u"A default value for this constraint object."),
        required=True,
    )
    
    hasAssumedValue=Bool(
        title=_(u"Has Assumed Value"),
        description=_(u"True if there is an assumed value."),
        required=True,
    )

    def validValue(aVal):
        """
        True if aValue is valid with respect to the expressed constraint.
        """
