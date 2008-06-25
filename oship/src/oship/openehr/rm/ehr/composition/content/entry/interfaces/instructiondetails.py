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
from zope.schema import TextLine

from openehr.rm.support.identification.locatableref import LocatableRef
from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure

_ = MessageFactory('oship')

class IInstructionDetails(IPathable):
    """
    Used to record the details of an Instruction causing an Action.
    """
    
    instructionId=LocatableRef(
        title=_("Instruction Id"),
        description=_("Reference to causing Instruction."),
        required=True,
    )
    
    activityId=TextLine(
        title=_("Activity Id"),
        description=_("Indentifier of Activity within Instruction."),
        required=True,
    )
    
    wfDetails=ItemStructure(
        title=_("WF Details"),
        description=_("Various workflow engine state details."),
        required=False,
    )
 