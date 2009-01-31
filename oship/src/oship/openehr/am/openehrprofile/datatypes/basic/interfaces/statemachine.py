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

from zope.interface import Interface
from zope.schema import Set,Object
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.openehrprofile.datatypes.basic.interfaces.state import IState

_ = MessageFactory('oship')


class IStateMachine(Interface):
    """        
    Definition of a state machine in terms of states, transition events and outputs, and
    next states.
    """
    
    states = Set(
        title=_(u"States"),
        description=_(u"""A Set of State types. """),
        required=True,
        value_type=Object(schema=IState),
        )
    
    
