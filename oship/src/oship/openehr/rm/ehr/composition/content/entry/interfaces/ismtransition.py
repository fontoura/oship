# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

The interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import Object

from openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText
from openehr.rm.common.archetyped.interfaces.pathable import IPathable

_ = MessageFactory('oship')

class IIsmTransition(IPathable):
    """
    Model of a transition in the Instruction state machine.
    """
    
    currentState=Object(
        schema=IDvCodedText,
        title=_("Current State"),
        description=_("The ISM current state."),
        required=True,
    )
    
    transition=Object(
        schema=IDvCodedText,
        title=_("Transition"),
        description=_("The ISM transition which occured to arrive at the current state."),
        required=False,
    )
    
    careflowStep=Object(
        schema=IDvCodedText,
        title=_("Careflow Step"),
        description=_("The step in the careflow process which occured as part of this process."),
        required=False,
    )
    
    
 