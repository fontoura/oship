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

from openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from openehr.rm.support.identification.interfaces.hierobjectid import IHierObjectId
from openehr.rm.support.identification.interfaces.partyref import IPartyRef
from openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from openehr.rm.datatypes.quantity.interfaces.dvinterval import IDvInterval

_ = MessageFactory('oship')

    
class IPartyRelationship(ILocatable):
    """
    Generic description of a relationship between parties.
    """
    
    uid=Object(
        schema=IHierObjectId,
        title=_(u"UID"),
        description=_(u"Identifier of this party."),
        required=True,
    )
        
    details=Object(
        schema=IItemStructure,
        title=_(u"Details"),
        description=(u"Description of the relationship."),
        required=False,
    )
        
    timeValidity=Object(
        schema=IDvInterval,
        title=_(u"Time Validity"),
        description=_(u"Valid time interval for this relationship."),
        required=False,
    )
    
    source=Object(
        schema=IPartyRef,
        title=_(u"Source"),
        description=_(u"Source of relationship."),
        required=True,
    )
    
    target=Object(
        schema=IPartyRef,
        title=_(u"Target"),
        description=_(u"Target of relationship."),
        required=True,
    )
    
    def type():
        """
        Type of relationship such as employment, authority, etc.
        """
 