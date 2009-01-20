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

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements
from zope.schema import Field

from oship.openehr.am.openehrprofile.datatypes.basic.interfaces.statemachine import IStateMachine

_ = MessageFactory('oship')

class IStateMachine(object):
    u"""        
    Definition of a state machine in terms of states, transition events and outputs, and
    next states.
    """
    implements(IStateMachine)
    
    def __init__(self,states):
        self.states=states
    
    
    
