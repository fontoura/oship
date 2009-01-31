# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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
from zope.schema import List,Object

from oship.openehr.rm.datatypes.quantity.interfaces.dvinterval import IDvInterval
from oship.openehr.rm.support.identification.interfaces.partyref import IPartyRef
from party import IParty

_ = MessageFactory('oship')

    
class IRole(IParty):
    """
    Generic role played by a party.
    """
    
    capabilities=List(
        title=_(u"Capabilities"),
        description=_(u"Capabilities of this role."),
        required=False,
    )
    
    timeValidity=Object(
        schema=IDvInterval,
        title=_(u"Time Validity"),
        description=_(u"Valid time interval for this role."),
        required=False,
    )
    
    
    performer=Object(
        schema=IPartyRef,
        title=_(u"Performer"),
        description=_(u"Reference to Version container of Actor playing this role."),
        required=True,
    )
