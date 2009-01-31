# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime
from oship.openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from oship.openehr.rm.ehr.composition.content.entry.ismtransition import IIsmTransition
from oship.openehr.rm.ehr.composition.content.entry.instructiondetails import IInstructionDetails
from oship.openehr.rm.ehr.composition.content.entry.interfaces.careentry import ICareEntry

_ = MessageFactory('oship')

class IAction(ICareEntry):
    """
    Used to record a clinical action that has been performed.
    """
    
    time=Object(
        schema=IDvDateTime,
        title=_(u"Timing"),
        description=_(u"Point in time of completion of this action."),
        required=True,
    )
    
    description=Object(
        schema=IItemStructure,
        title=_(u"Description"),
        description=_(u"Description of the activity in ItemStructure form."),
        required=True,
    )
    
    ismTransition=Object(
        schema=IIsmTransition,
        title=_(u"ISM Transition"),
        description=_(u"Details of the transition of the Instruction state."),
        required=True,
    )
    
    instructionDetails=Object(
        schema=IInstructionDetails,
        title=_(u"Instruction Details"),
        description=_(u"Details of the Instruction causing this Action."),
        required=False,
    )
    
