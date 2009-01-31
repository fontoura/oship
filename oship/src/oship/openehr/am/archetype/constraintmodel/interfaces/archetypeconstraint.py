# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
From the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.i18nmessageid.message import MessageFactory 
from zope.schema.interfaces import IContainer

_ = MessageFactory('oship')


class IArchetypeConstraint(IContainer):
    """
    Archetype equivalent to Locatable class in the Common package of the reference model.
    """
    
    def isSubsetOf(other):
        u"""True if constraints are narrower than this node."""

    def isValid():
        u"""True if this node and sub-nodes are valid for its type."""

    def path():
        """
        Return a string containt the path of this node relative to the archetype root.
        """
        
    def hasPath(aPath):
        """
        Return True if the relative path (aPath) exists at this node.
        """
