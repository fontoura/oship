# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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

from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory

from creferenceobject import CReferenceObject
from interfaces.archetypeslot import IArchetypeSlot

_ = MessageFactory('oship')

class ArchetypeSlot(CReferenceObject):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    implements(IArchetypeSlot)
    

    def __init__(self,incl,excl):
        self.includes=incl
        self.excludes=excl
 