# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.schema import Set,Object
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.am.openehrprofile.datatypes.basic.interfaces.state import IState
from oship.openehr.am.openehrprofile.datatypes.basic.interfaces.transition import ITransition

_ = MessageFactory('oship')

class INonTerminalState(IState):
    """
    Definition of a non-terminal state in a state machine, i.e. one that has transitions.
    """
    
    transitions = Set(
        title=_(u"Transitions"),
        description=_(u"""A Set of Transition types. """),
        required=False,
        value_type=Object(schema=ITransition),
        )
    