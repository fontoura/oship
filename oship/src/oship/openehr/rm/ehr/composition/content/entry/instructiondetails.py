# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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
from zope.interface import implements

from oship.openehr.rm.common.archetyped.pathable import Pathable
from interfaces.instructiondetails import IInstructionDetails

_ = MessageFactory('oship')


class InstructionDetails(Pathable):
    """
    Used to record the details of an Instruction causing an Action.
    """
    
    implements(IInstructionDetails)
    
    def __init__(self,inst,actid,wfd):
        self.instructionId=inst
        self.activityId=actid
        self.wfDetails=wfd
    
