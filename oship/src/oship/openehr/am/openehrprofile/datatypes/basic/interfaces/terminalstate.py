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

from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.am.openehrprofile.datatypes.basic.interfaces.state import IState

_ = MessageFactory('oship')

class ITerminalState(IState):
    """
    Definition of a terminal state in a state machine, i.e. a state with no exit transitions.
    """
    
    