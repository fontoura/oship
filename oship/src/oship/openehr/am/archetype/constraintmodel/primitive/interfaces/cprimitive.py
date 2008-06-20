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

class ICPrimitive(Interface):
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
        
class CPrimitive(Interface):
    """
    Abstract super type of all primitive types.
    """
    
    implements(ICPrimitive)
    

    def validValue(aVal):
        """
        True if aValue is valid with respect to the expressed constraint.
        """
