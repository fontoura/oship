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
from zope.schema import TextLine,Object

from oship.openehr.rm.support.identification.interfaces.locatableref import ILocatableRef
from oship.openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from oship.openehr.rm.common.archetyped.interfaces.pathable import IPathable

_ = MessageFactory('oship')

class IInstructionDetails(IPathable):
    """
    Used to record the details of an Instruction causing an Action.
    """
    
    instructionId=Object(
        schema=ILocatableRef,
        title=_(u"Instruction Id"),
        description=_(u"Reference to causing Instruction."),
        required=True,
    )
    
    activityId=TextLine(
        title=_(u"Activity Id"),
        description=_(u"Indentifier of Activity within Instruction."),
        required=True,
    )
    
    wfDetails=Object(
        schema=IItemStructure,
        title=_(u"WF Details"),
        description=_(u"Various workflow engine state details."),
        required=False,
    )
 