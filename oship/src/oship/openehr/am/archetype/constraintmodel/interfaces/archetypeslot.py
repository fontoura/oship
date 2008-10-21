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

from zope.schema import Set,Object
from zope.i18nmessageid.message import MessageFactory

from creferenceobject import ICReferenceObject
from oship.openehr.am.archetype.assertion.interfaces.assertion import IAssertion

_ = MessageFactory('oship')

class IArchetypeSlot(ICReferenceObject):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    includes=Set(
        title=_(u"Includes"),
        description=_(u"List of constraints defining other archetypes that can be included here."),
        required=False,
        value_type=Object(schema=IAssertion),
    )

    excludes=Set(
        title=_(u"Excludes"),
        description=_(u"List of constraints defining archetypes that cannot be include here."),
        required=False,
        value_type=Object(schema=IAssertion),
    )

