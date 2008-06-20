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

from zope.interface import implements
from zope.schema import Set
from zope.i18nmessageid.message import MessageFactory

from openehr.am.archetype.creferenceobject import ICReferenceObject,CReferenceObject

_ = MessageFactory('oship')

class IArchetypeSlot(ICReferenceObject):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    includes=Set(
        title=_(u"Includes"),
        description=_(u"List of constraints defining other archetypes that can occur here."),
        required=False,
    )

    excludes=Set(
        title=_(u"Excludes"),
        description=_(u"List of constraints defining archetypes that cannot be include here."),
        required=False,
    )

class ArchetypeSlot(CReferenceObject):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    implements(IArchetypeSlot)

    def __init__(self,incl,excl,**kw):
        self.includes=incl
        self.excludes=excl
        for n,v in kw.items():
            setattr(self,n,v)
