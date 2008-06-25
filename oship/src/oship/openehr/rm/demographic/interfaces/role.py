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
from zope.schema import List

from openehr.rm.datatypes.quantity.dvinterval import DvInterval
from openehr.rm.support.identification.partyref import PartyRef
from party import IParty

_ = MessageFactory('oship')

    
class IRole(IParty):
    """
    Generic role played by a party.
    """
    
    capabilities=List(
        title=_("Capabilities"),
        description=_("Capabilities of this role."),
        required=False,
    )
    
    timeValidity=DvInterval(
        title=_("Time Validity"),
        description=_("Valid time interval for this role."),
        required=False,
    )
    
    
    performer=PartyRef(
        title=_("Performer"),
        description=_("Reference to Version container of Actor playing this role."),
        required=True,
    )
