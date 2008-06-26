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

from zope.schema.interfaces import IField
from zope.schema import Field,Bool
from zope.i18nmessageid.message import MessageFactory

_ = MessageFactory('oship')

class ICPrimitive(IField):
    """
    Abstract super type of all primitive types.
    """
    
    defaultValue=Field(
        title_("Default Value"),
        description=_("A default value for this constriant object."),
        required=True,
    )
    
    hasAssumedValue=Bool(
        title_("Has Assumed Value"),
        description=_("True if thiere is an assumed value."),
        required=True,
    )

    def validValue(aVal):
        """
        True if aValue is valid with respect to the expressed constraint.
        """
