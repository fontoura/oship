# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

From the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__Contributors__ = u'Roberto Cunha <roliveiracunha@yahoo.com.br>'

from zope.interface import Interface,implements
from zope.schema import Set,List,TextLine,Field,Object
from zope.i18nmessageid import MessageFactory
import grok

from common import Locatable
from support import IHierObjectId,IPartyRef
from datatypes import IDvText,IDvCodedText,ICodePhrase,IDvInterval
from datastructure import IItemStructure


_ = MessageFactory('oship')

class IAddress(Interface):
    """
    Address of contact.
    """
    
    details=Object(
        schema=IItemStructure,
        title=_(u"Details"),
        description=_(u"The details of the address."),
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

class IPartyIdentity(Interface):
    """
    An identity owned by a party.
    """
    
    details=Object(
        schema=IItemStructure,
        title=_(u"Details"),
        description=_(u"The value of the identitiy"),
        required=False,
    )
    
    purpose=Object(
        schema=IDvText,
        title=_(u"Purpose"),
        description=_(u"Purpose fo this identitiy."),
        
    )
    
    def asString():
        """
        Indentity in the form of a string.
        """
class IContact(Interface):
    """
    Description of a means of contacting a party.
    """
    
    timeValidity=Object(
        schema=IDvInterval,
        title=_(u"Time Validity"),
        description=_(u"Valid time interval for this contact descriptor."),
        required=False,
    )
    
    addresses=List(
        value_type = Object(schema = IAddress),
        title=_(u"Addresses"),
        description=_(u"A set of addresses for this purpose and time frame."),
    )
    
    def purpose():
        """
        Purpose for which this contact is used.
        Taken from the inherited 'name' attribute.        
        """

class IPartyRelationship(Interface):
    """
    Generic description of a relationship between parties.
    """
    
    uid=Object(
        schema=IHierObjectId,
        title=_(u"UID"),
        description=_(u"Identifier of this party."),
        
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
        
    )
    
    target=Object(
        schema=IPartyRef,
        title=_(u"Target"),
        description=_(u"Target of relationship."),
        
    )
    
    def type():
        """
        Type of relationship such as employment, authority, etc.
        """
 

class IParty(Interface):
    """
    Ancestor of all party types.
    """
    
    uid=Object(
        schema=IHierObjectId,
        title=_(u"UID"),
        description=_(u"Identifier of this party."),
        
    )
    
    identities=Set(
        title=_(u"Indentities"),
        description=_(u"Identities used by the party to identify itself."),
        value_type = Object(schema = IPartyIdentity)
    )
    
    contacts=Set(
        title=_(u"Contacts"),
        description=_(u"Contacts for this party."),
        value_type = Object(schema = IContact)
    )
    
    category=Object(
        schema=IDvCodedText,
        title=_(u"Category"),
        description=_(u"Defines the broad category of this composition."),
        required=False,
    )
    
    language=Object(
        schema=ICodePhrase,
        title=_(u"Language"),
        description=_(u"Indicator of the localised language where this composition was created."),
        
    )
    
    relationships=Set(
        title=_(u"Relationships"),
        description=_(u"Relationships in which this role takes part as target."),
        required=False,
        value_type = Object(schema = IPartyRelationship)
    )
    
    details=Object(
        schema=IItemStructure,
        title=_(u"Details"),
        description=_(u"All other party details."),
        required=False,
    )
    
    def type():
        """
        Return the type of party from the inherited 'name' attribute.
        """

        
class Party(Locatable):
    """
    Ancestor of all party types.
    """
    
    implements(IParty)
    
    def __init__(self,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links):
        Locatable.__init__(self,uid,archetypeNodeId,name,archetypeDetails,feederAudit,links)
        
        self.identities=identities
        self.contacts=contacts
        self.category=category
        self.language=language
        self.relationships=relationships
        self.details=details
        
        
        
        
    def type():
        """
        Return the type of party from the inherited 'name' attribute.
        """

class IActor(Interface):
    """
    Ancestor of all real world types.
    """
    
    roles=Set(
        title=_(u"Roles"),
        description=_(u"Identifiers of the Version container for each Role played by this party."),
        required=False,
        value_type = Object(schema = IPartyRef)
    )
    
    languages=List(
        title=_(u"Languages"),
        description=_(u"A list of languages to be used to communicate with this actor."),
        required=False,
        value_type = Object(schema = IDvText)
    )
    def hasLegalIdentity():
        """
        Return True/False regarding a legal identiry of this Actor.
        """

  
class Actor(Party):
    """
    Ancestor of al real world types.
    """
    
    implements(IActor)
    
    
    def __init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links):
        Party.__init__(self,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links)

        self.roles=roles
        self.languages=languages
    
    def hasLegalIdentity():
        """
        Return True/False regarding a legal identiry of this Actor.
        """
        
    

class Address(Locatable):
    """
    Address of contact as an ItemStructure.
    """
    
    implements(IAddress)
    
    def __init__(self,details,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
        
        self.details=details
        
   
       
    
    def type():
        """
        Return the type of address from 'name'.
        """
    
    def asString():
        """
        Address in the form of a string.
        """
        
        
class IAgent(Interface):
    """
    Generic concept of of any kind of agent including devices.
    """
    pass

class Agent(Actor):
    """
    Generic concept of of any kind of agent including devices.
    """    

    implements(IAgent)
    
    def __init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links):
        Actor.__init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links)
        
class ICapability(Interface):
    """
    Capability of a role such as ehr modifier, healthcare provider, etc.
    """
    
    credentials=Object(
        schema=IItemStructure,
        title=_(u"Credentials"),
        description=_(u"Qualifications of the performer of the role."),
        
    )
    
    timeValidity=Object(
        schema=IDvInterval,
        title=_(u"Time Validity"),
        description=_(u"Valid time interval for the credentials of this capability."),
        required=False,
    )
    
class Capability(Locatable):
    """
    Capability of a role such as ehr modifier, healthcare provider, etc.
    """
    
    implements(ICapability)
    
    def __init__(self,credentials,timeValidity,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
        self.credentials=credentials
        self.timeValidity=timeValidity
        

    


class Contact(Locatable):
    """
    Description of a means of contacting a party.
    """
    implements(IContact)
    
    def __init__(self,timeValidity,addresses,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
        
        
    def purpose():
        """
        Purpose for which this contact is used.
        Taken from the inherited 'name' attribute.        
        """
    
    
class IGroup(Interface):
    """
    A real world group of parties.
    """
   
    pass

class Group(Actor):
    """
    A real world group of parties.
    """

    implements(IGroup)
    def __init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links):
        Actor.__init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links)

    
class IOrganisation(Interface):
    """
    Generic descriptions of organizations.
    """

    pass
    
    
class Organisation(Actor):
    """
    Generic descriptions of organizations.
    """        

    implements(IOrganisation)
    
    def __init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links):
        Actor.__init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links)
        
      
class PartyIdentity(Locatable):
    """
    An identity owned by a party.
    """
    
    implements(IPartyIdentity)
    
    def __init__(self,details,purpose,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)

    def asString():
        """
        Indentity in the form of a string.
        """
         
        
                
        
 
        
        
class PartyRelationship(Locatable):
    """
    Generic description of a relationship between parties.
    """
    
    implements(IPartyRelationship)
    
    def __init__(self,uid,details,timeValidity,source,target,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
        self.details=details
        self.timeValidity=timeValidity
        self.source=source
        self.target=target
        

    def type():
        """
        Type of relationship such as employment, authority, etc.
        """
  
class IPerson(Interface):
    """
    Generic description of of persons.  Provides a dedicated type to whicih Person archetypes can be targeted."),
    """
    
    pass

class Person(Actor):
    """
    Generic description of of persons.  Provides a dedicated type to whicih Person archetypes can be targeted."),
    """
    
    implements(IPerson)
    def __init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links):
        Actor.__init__(self,roles,languages,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links)

class IRole(Interface):
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
        
    )

class Role(Party):
    """
    Generic role played by a party.
    """
    
    implements(IRole)
    
    def __init__(self,capabilities,timeValidity,performer,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links):
        Party.__init__(self,uid,identities,contacts,category,language,relationships,details,archetypeNodeId,name,archetypeDetails,feederAudit,links)
        self.capabilities=capabilities
        self.timeValidity=timeValidity
        self.performer=performer
        
        
      