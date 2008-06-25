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

from openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from openehr.rm.support.identification.hierobjectid import HierObjectId
from openehr.rm.support.identification.partyref import PartyRef
from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from openehr.rm.datatypes.quantity.dvinterval import DvInterval

_ = MessageFactory('oship')

    
class IPartyRelationship(ILocatable):
    """
    Generic description of a relationship between parties.
    """
    
    uid=HierObjectId(
        title=_("UID"),
        description=_("Identifier of this party."),
        required=True,
    )
        
    details=ItemStructure(
        title_("Details"),
        description=_("Description of the relationship."),
        required=False,
    )
        
    timeValidity=DvInterval(
        title=_("Time Validity"),
        description=_("Valid time interval for this relationship."),
        required=False,
    )
    
    source=PartyRef(
        title=_("Source"),
        description=_("Source of relationship."),
        required=True,
    )
    
    target=PartyRef(
        title=_("Target"),
        description=_("Target of relationship."),
        required=True,
    )
    
    def type():
        """
        Type of relationship such as employment, authority, etc.
        """
 