# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.schema import Object

from openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from openehr.rm.datatypes.quantity.interfaces.dvinterval import IDvInterval
from openehr.rm.common.archetyped.interfaces.locatable import ILocatable

_ = MessageFactory('oship')

class ICapability(ILocatable):
    """
    Capability of a role such as ehr modifier, healthcare provider, etc.
    """
    
    credentials=Object(
        schema=IItemStructure,
        title=_(u"Credentials"),
        description=_(u"Qualifications of the performer of the role."),
        require=True,
    )
    
    timeValidity=Object(
        schema=IDvInterval,
        title=_(u"Time Validity"),
        description=_(u"Valid time interval for the credentials of this capability."),
        required=False,
    )
    