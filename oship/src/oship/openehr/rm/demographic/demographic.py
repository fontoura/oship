# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementations for specifications for the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class Party(Locatable):
    """
    Ancestor of all party types.
    """
    
    uid=HierObjectId(
        title=_("UID"),
        description=_("Identifier of this party."),
        required=True,
    )
    
    identities=Set(
        title=_("Indentities"),
        description=_("Identities used by the party to identify itself."),
        required=True,
    )
    
    contacts=Set(
        title=_("Contacts"),
        description=_("Contacts for this party."),
        required=True,
    )
    
    category=DvCodedText(
        title=_("Category"),
        description=_("Defines the broad category of this composition."),
        required=False,
    )
    
    language=CodePhrase(
        title=_("Language"),
        description=_("Indicator of the localised language where this composition was created."),
        required=True,
    )
    
    relationships=Set(
        title=_("Relationships"),
        description=_("Relationships in which this role takes part as target."),
        required=False,
    )
    
    details=ItemStructure(
        title=_("Details"),
        description=_("All other party details."),
        required=False,
    )
    
    def type():
        """
        Return the type of party from the inherited 'name' attribute.
        """
        
class PartyIdentity(Locatable):
    """
    An identity owned by a party.
    """
    
    details=ItemStructure(
        title=_("Details"),
        description=_("The value of the identitiy"),
        required=False,
    )
    
    purpose=Dvtext(
        title=_("Purpose"),
        description=_("Purpose fo this identitiy."),
        required=True,
    )
    
    def asString():
        """
        Indentity in the form of a string.
        """
        
    
class Contact(Locatable):
    """
    Description of a means of contacting a party.
    """
    
    timeValidity=DvInterval(
        title=_("Time Validity"),
        description=_("Valid time interval for this contact descriptor."),
        requires=False,
    )
    
    addresses=List(
        title=_("Addresses"),
        description=_("A set of addresses for this purpose and time frame."),
        required=True,
    )
    
    def purpose():
        """
        Purpose for which this contact is used.
        Taken from the inherited 'name' attribute.        
        """
    
class Address(Locatable):
    """
    Address of contact.
    """
    
    details=ItemStructure(
        title=_("Details"),
        description=_("The details of the address."),
        required=False,
    )
    
    
    def type():
        """
        Return the type of address from 'name'.
        """
    
    def asString():
        """
        Address in the form of a string.
        """
    
class Actor(Party):
    """
    Ancestor of al real world types.
    """
    
    roles=Set(
        title=_("Roles"),
        description=_("Identifiers of the Version container for each Role played by this party."),
        required=False,
    )
    
    languages=List(
        title=_("Languages"),
        description=_("A list of languages to be used to communicate with this actor."),
        required=False,
    )
    def hasLegalIdentity():
        """
        Return True/False regarding a legal identiry of this Actor.
        """
        
class Person(Actor):
    """
    Generic description of of persons.  Provides a dedicated type to whicih Person archetypes can be targeted."),
    """
    
    
class Organisation(Actor):
    """
    Generic descriptions of organizations.
    """
    
class Group(Actor):
    """
    A real world group of parties.
    """
    
class Agent(Actor):
    """
    Generic concept of of any kind of agent including devices.
    """
    
class Role(Party):
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
class Capability(Locatable):
    """
    Capability of a role such as ehr modifier, healthcare provider, etc.
    """
    
    credentials=ItemStructure(
        title=_("Credentials"),
        description=_("Qualifications of the performer of the role."),
        require=True,
    )
    
    timeValidity=DvInterval(
        title=_("Time Validity"),
        description=_("Valid time interval for the credentials of this capability."),
        required=False,
    )
    
class PartyRelationship(Locatable):
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
 