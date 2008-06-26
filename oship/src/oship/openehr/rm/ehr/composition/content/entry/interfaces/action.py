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

from openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime
from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from entry.ismtransition import IsmTransition
from entry.instructiondetails import InstructionDetails


_ = MessageFactory('oship')

class IAction(ICareEntry):
    """
    Used to record a clinical action that has been performed.
    """
    
    time=DvDateTime('',
        title=_("Timing"),
        description=_("Point in time of completion of this action."),
        required=True,
    )
    
    description=ItemStructure(
        title=_("Description"),
        description=_("Description of the activity in ItemStructure form."),
        required=True,
    )
    
    ismTransition=IsmTransition(
        title=_("ISM Transition"),
        description=_("Details of the transition of the Instruction state."),
        required=True,
    )
    
    instructionDetails=InstructionDetails(
        title=_("Instruction Details"),
        description=_("Details of the Instruction causing this Action."),
        required=False,
    )
    
   
  
 