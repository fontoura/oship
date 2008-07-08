# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements,classProvides
from zope.schema import Field

_ = MessageFactory('oship')

class CMultipleAttribute(object):
    """
    Abstract model of constraint on any kind of attribute node.
    """
    
    implements(ICMultipleAttribute)
    classProvides(ICMultipleAttribute)
    
    def members(cobj):
        """
        List of constraints representing members of the container value of this attribute.
        """
