# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The Archetype Profile basic package. 
From the openEHR Archetype Profile specifications Rev. 1.0.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import Interface
from zope.schema import TextLine
from zope.schema.interfaces import IField
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.am.openehrprofile.datatypes.basic.interfaces.state import IState

_ = MessageFactory('oship')


class ITransition(IField):
    """
    Definition of a state machine transition.
    """
    
    event = TextLine(
        title=_(u"Event"),
        description=_(u"""Event which fires this transition."""),
        required=True,
        )

    guard = TextLine(
        title=_(u"Guard"),
        description=_(u"""Guard condition which must be true for this transition to fire."""),
        required=False,
        )

    action = TextLine(
        title=_(u"Action"),
        description=_(u"""Side-effect action to execute during the firing of this transition."""),
        required=False,
        )

    nextState = Object(
        schema=IState,
        title=_(u"Next State"),
        description=_(u"""Target state of next transition. """),
        required=True,
        )
