# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementations for specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.interface import implements,classProvides

from interfaces.ismtransition import IIsmTransition
from openehr.rm.common.archetyped.pathable import Pathable

_ = MessageFactory('oship')

    
class IsmTransition(Pathable):
    """
    Model of a transition in the Instruction state machine.
    """
    
    implements(IIsmTransition)
    classProvides(IIsmTransition)
    
    def __init__(self,cstate,trans,cfs):
        self.currentState=cstate
        self.transition=trans
        self.careflowStep=cfs
