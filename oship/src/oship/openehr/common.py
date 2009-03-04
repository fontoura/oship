# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import Interface,implements
from zope.schema import TextLine,Object,Field,List,Set,Bool,Dict,URI
from zope.schema.interfaces import IContainer
from zope.i18nmessageid import MessageFactory
import grok

from support import IUidBasedId,IObjectRef,IPartyRef,IArchetypeId,ITemplateId ,IHierObjectId,IObjectVersionId
from datatypes import IDvText,IDvIdentifier,IDvDateTime,IDvEncapsulated,IDvEhrUri,IDvCodedText,IDvMultimedia,IDvInterval, ICodePhrase

_ = MessageFactory('oship')
        
class ILink(Interface):
    """
    The LINK type defines a logical relationship between two items, such as two
    ENTRYs or an ENTRY and a COMPOSITION. Links can be used across composi-
    tions, and across EHRs. Links can potentially be used between interior (i.e. non
    archetype root) nodes, although this probably should be prevented in archetypes.
    Multiple LINKs can be attached to the root object of any archetyped structure to
    give the effect of a 1->N link 1:1 and 1:N relationships between archetyped content 
    elements (e.g. ENTRYs) can be expressed by using one, or more than one, respectively, DV_LINKs.
    Chains of links can be used to see "problem threads" or other logical groupings of items.
    Links should be between archetyped structures only, i.e. between objects representing 
    complete domain concepts because relationships between sub-elements
    of whole concepts are not necessarily meaningful, and may be downright confusing. Sensible 
    links only exist between whole ENTRYs, SECTIONs, COMPOSITIONs and so on.
    """
    
    meaning = Object(
        schema=IDvText,
        title=_(u"Meaning"),
        description=_(u"""Used to describe the relationship, usually in clinical terms, such as 
                    "in response to" (the relationship between test results and an order),
                    "follow-up to" and so on. Such relationships can represent any clinically 
                    meaningful connection between pieces of information. Values for meaning 
                    include those described in Annex C, ENV 13606 pt 2 [11] under the categories 
                    of "generic", "documenting and reporting","organisational","clinical",
                    "circumstancial", and "view management".  """),
        
        )
    
    type = Object(
        schema=IDvText,
        title=_(u"Type"),
        description=_(u"""The type attribute is used to indicate a clinical or domain-level meaning 
                    for the kind of link, for example "problem" or "issue". If type values are 
                    designed appropriately, they can be used by the requestor of EHR extracts to 
                    categorise links which must be followed and which can be broken when the extract 
                    is created. """),
        
        )
    
    target = Object(
        schema=IDvEhrUri,
        title=_(u"Target"),
        description=_(u"""The logical "to" object in the link relation, as target: 
                    per the linguistic sense of the meaning attribute."""),
        
        )
    
    def meaningValid():
        """Return meaning != None """
        
    def typeValid():
        """Return type != None """
        
    def targetValid():
        """Return target != None """


class IPartyIdentified(Interface):
    u"""
    Proxy data for an identified party other than the subject of the record, 
    minimally consisting of human-readable identifier(s), such as name, formal 
    (and possibly computable) identifiers such as NHS number, and an optional 
    link to external data. There must be at least one of name, identifier or 
    external_ref present.
        
    Used to describe parties where only identifiers may be known, and there is 
    no entry at all in the demographic system (or even no demographic system). 
    Typically for health care providers, e.g. name and provider number of an 
    institution.

    Should not be used to include patient identifying information.
    """
    
    name = TextLine(
        title=_(u'Name'),
        description=_(u"""Optional human-readable name (in String form)."""),
        required=False,
        )
    
    identifiers = List(
        value_type=Object(schema=IDvIdentifier),
        title=_(u'Identifiers'),
        description=_(u"""One or more formal identifiers (possiblycomputable).
                    List<DvIdentifier>"""),
        required=False,
        )

    def basicValid(obj):
        u"""name None or identifiers != None or external_ref != None"""            
        
    def nameValid():
        u"""name != None and name != '' """
        
    def identifiersValid():
        u"""identifiers != none and identifiers != '' """
        
class IPartyProxy(Interface):
    u"""
    Abstract concept of a proxy description of a party, including an optional 
    link to data for this party in a demographic or other identity management 
    system. Subtyped into PARTY_IDENTIFIED and PARTY_SELF.
    """
    
    externalRef = Object(
        schema=IPartyRef,
        title=_(u"External Reference"),
        description=_(u"""Optional reference to more detailed demographic or 
                    identification information for this party, in an external 
                    system. Type == PartyRef."""),
        required=False,
        )
class IAuditDetails(Interface):
    u"""
    The set of attributes required to document the committal of an information 
    item to a repository.
    """
    
    systemId = TextLine(
        title=_(u"""System Id"""),
        description=_(u"""Identity of the system where the change was committed.
                    Ideally this is a machine- and human-processable identifier,
                    but it may not be."""),
        
        )
    
    committer = Object(
        schema=IPartyProxy,
        title=_(u"""Committer"""),
        description=_(u"""Identity and optional reference into identity management
                    service, of user who committed the item."""),
        
        )
    
    timeCommitted = Object(
        schema=IDvDateTime,
        title=_(u"""Time Committed"""),
        description=_(u"""Time of committal of the item."""),
        
        )
    
    changeType = Object(
        schema=IDvCodedText,
        title=_(u"""Change Type"""),
        description=_(u"""Type of change. Coded using the openEHR Terminology 
                    "audit change type" group. Type==DvCodedText"""),
        
        )
    
    description = Object(
        schema=IDvText,
        title=_(u"""Description"""),
        description=_(u"""Reason for committal. Type==DvText"""),
        required=False,
        )
    
    def systemIdValid():
        u"""systemId != None and systemId != '' """
        
    def committerValid():
        u"""committer!= None"""
        
    def timeCommittedValid():
        u"""timeCommitted != None"""
    
    def changeTypeValid():
        u"""changeType != None and then terminology(Terminology_id_openehr).
        has_code_for_group_id(Group_id_audit_change_type, change_type.defining_code)"""


class IFeederAuditDetails(Interface):
    u"""
    Audit details for any system in a feeder system chain. Audit details here means
    the general notion of who/where/when the information item to which the audit is
    attached was created. None of the attributes is defined as mandatory, however, in
    different scenarios, various combinations of attributes will usually be mandatory.
    This can be controlled by specifying feeder audit details in legacy archetypes.
    """

    systemId = TextLine(
        title=_(u'System Id'),
        description=_(u"""Identifier of the system which handled the information item."""),
        
        )
    
    provider = Object(
        schema=IPartyIdentified,
        title=_(u'Provider'),
        description=_(u"""Optional provider(s) who created, committed, forwarded or otherwise 
        handled the item. Type == PARTY_IDENTIFIED"""),
        required=False,
        )
    
    location = Object(
        schema=IPartyIdentified,
        title=_(u'Location'),
        description=_(u"""Identifier of the particular site/facility within an organisation 
                    which handled the item. For computability, this identifier needs to be 
                    e.g. a PKI identifier which can be included in the identifier list of 
                    the PARTY_IDENTIFIED object."""),
        required=False,
        )
    
    time = Object(
        schema=IDvDateTime,
        title=_(u'Time'),
        description=_(u"""Time of handling the item. For an originating time: DV_DATE_TIME system, 
                    this will be time of creation, for an intermediate feeder system, this will 
                    be a time of accession or other time of handling, where available."""),
        required=False,
        )
    
    subject = Object(
        schema=IPartyProxy,
        title=_(u'Subject'),
        description=_(u"""Identifiers for subject of the received information item."""),
        required=False,
        )
    
    versionId = TextLine(
        title=_(u'Version Id'),
        description=_(u"""Any identifier used in the system such as "interim", "final", 
                      or numeric versions if available."""),
        required=False,
        )
    
    def systemIdValid():
        u"""systemId != None and  systemId != '' """
        


class IFeederAudit(Interface):
    """
    Audit and other meta-data for systems in the feeder chain.
    """
    
    originatingSystemAudit = Object(
        schema=IFeederAuditDetails,
        title=_(u"Originating System Audit"),
        description=_(u"""Any audit information for the information item from the originating system."""),
        
        )
    
    originatingSystemItemIds = List(
        value_type=Object(schema=IDvIdentifier),
        title=_(u"Originating System Item IDs"),
        description=_(u"""Identifiers used for the item in the originating system, e.g. filler and placer ids."""),
        required=False,
        )
    
    
    feederSystemAudit = Object(
        schema=IFeederAuditDetails,
        title=_(u"Feeder System Audit"),
        description=_(u"""Any audit information for the information item from the feeder system, 
                    if different from the originating system."""),
        required=False,
        )
    
    feederSystemItemIds = List(
        value_type=Object(schema=IDvIdentifier),
        title=_(u"Feeder System Item IDs"),
        description=_(u"""Identifiers used for the item in the feeder system, where the feeder 
                    system is distinct from the originating system. The List contents are restricted to
                    type == DvIdentifiers"""),
        required=False,
        )
    
    originalContent=Object(
        schema=IDvEncapsulated,
        title=_(u"Original Content"),
        description=_(u""" """),
        required=False,
        )
    
    def originatingSystemAuditValid():
        """ originatingSystemAudit != None """

        
class IPathable(Interface):
    """
    Abstract parent of all classes whose instances are reachable by paths, and which
    know how to locate child object by paths. The parent feature may be implemented 
    as a function or attribute.
    
    The two attributes required for locatable in ZCA is __parent__ and __name__.  
    We inherit those from IContained.
    
    The functionality to get paths and find children is contained in the traversal mechanism.
    """
    
        
    def pathOfItem(an_item):
        """
        The path to an item relative to the root of this archetyped structure.
        
        getPath is from the Traversal API.
        """
                
        
        
    def itemAtPath(a_path):
        """
        The item at a path (relative to this item);only valid for unique paths, i.e. paths
        that resolve to a single item.
        a_path is a string.
        Return a_path != None and pathUnique(a_path)
        
        If the path is not unique or not found then a TraversalError is raised.
        """       
        
        
    def itemsAtPath(a_path):
        """
        List of items corresponding to a non-unique path.
        a_path is a List
        Return a_path != None and pathUnique(a_path)
        """
        
 
    def pathExists(a_path):
        """
        True if the path exists in the data with respect to the current item.
        Return a_path != None and a_path != '' 
        """
        
        
    def pathUnique(a_path):
        """
        True if the path corresponds to a single item in the data.
        Return a_path != None and pathExists(a_path)
        """

class Pathable(grok.Model):
    """
    Abstract parent of all classes whose instances are reachable by paths, and which
    know how to locate child object by paths. The parent feature may be implemented 
    as a function or attribute.
    
    The two attributes required for locatable in ZCA is __parent__ and __name__.  
    We inherit those from Location.
    
    The functionality to get paths and find children is contained in the traversal mechanism.
    """
    
    implements(IPathable)
    
    pass
    
    def pathOfItem(an_item):
        """
        The path to an item relative to the root of this archetyped structure.
        
        getPath is from the Traversal API.
        """
                       
    def itemAtPath(a_path):
        """
        The item at a path (relative to this item);only valid for unique paths, i.e. paths
        that resolve to a single item.
        a_path is a string.
        Return a_path != None and pathUnique(a_path)
        
        If the path is not unique or not found then a TraversalError is raised.
        """       
        
        
    def itemsAtPath(a_path):
        """
        List of items corresponding to a non-unique path.
        a_path is a List
        Return a_path != None and pathUnique(a_path)
        """
        
 
    def pathExists(a_path):
        """
        True if the path exists in the data with respect to the current item.
        Return a_path != None and a_path != '' 
        """
        
        
    def pathUnique(a_path):
        """
        True if the path corresponds to a single item in the data.
        Return a_path != None and pathExists(a_path)
        """
        
        

class ILocatable(Interface):
    u"""
    Root class of all information model classes that can be archetyped.
    """
    

    uid = Object(
        schema=IUidBasedId,
        title=_(u"UID"),
        description=_(u"Optional globally unique object identifier for root points of archetyped structures. A UidBasedId "),
        required=False,
        )
    
   
    archetypeNodeId = TextLine(
        title=_(u"Node ID"),
        description=_(u"""Design-time archetype id of this node taken from its generating archetype;
                     used to build archetype paths. Always in the form of an "at" code, e.g. "at0005".
                     This value enables a "standardised" name for this node to be generated, by
                     referring to the generating archetype local ontology.
                     
                     At an archetype root point, the value of this attribute is always the stringified
                     form of the archetype_id found in the archetype_details object."""),
        
        )
    
    name = Object(
        schema=IDvText,
        title=_(u"Name"),
        description=_(u"""DvText type - Runtime name of this fragment, used to build runtime paths. 
                     This is the term provided via a clinical application or batch
                     process to name this EHR construct: its retention in the EHR 
                     faithfully preserves the original label by which this entry
                     was known to end. """),
        
        )

    
    archetypeDetails = Object(
        schema=IObjectRef,
        title=_(u"Archetype Details"),
        description=_(u"Details of archetyping used on this node."),
        required=False,
        )
   
    feederAudit = Object(
        schema=IFeederAudit,
        title=_(u"Feeder Audit"),
        description=_(u"""Audit trail from non-openEHR system of original commit of information 
                    forming the content of this node, or from a conversion gateway which has 
                    synthesised this node."""),
        required=False,
        )
    
    
    links = List(
        value_type=Object(schema=ILink),
        title=_(u"Links"),
        description=_(u"""Audit trail from non-openEHR system of original commit of information 
                    forming the content of this node, or from a conversion gateway which has 
                    synthesised this node."""),
        required=False,
        )
    
    
    def isArchetypeRoot():
        u"""True if this node is the root of an archetyped structure."""
        
    def concept():
        u"""
        Clinical concept of the archetype as a whole (= derived from the
       'archetype_node_id' of the root node) isArchetypeRoot must be True.
       """
        
    def nameValid():
        u""" name != None"""
          
    def linksValid():
        u""" links != None and links != []"""
 
    def archetypedValid():
        u""" isArchetypeRoot xor archetypeDetails = None """
        
    def archetypeNodeIdValid():
        u""" archetypeNodeId != None and archetypeNodeId != '' """
        
class Locatable(Pathable):
    """
    Root class of all information model classes that can be archetyped.
    """

    implements(ILocatable)
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links):
        
        self.uid=uid
        self.archetypeNodeId=self.__name__=atnodeid
        self.name=name
        self.archetypeDetails=atdetails
        self.feederAudit=fdraudit
        self.links=links
           
    def isArchetypeRoot():
        """True if this node is the root of an archetyped structure. At specification there's a requiment for archetypeDetails in all root points in data
        """
        return self.archetypeDetails != None
        
    def concept():
        """
        Clinical concept of the archetype as a whole (= derived from the
       'archetype_node_id' of the root node) isArchetypeRoot must be True.
       """
        if (self.isArchetypeRoot()):
            return DvText(self.archetypeDetails.archetypeId.conceptName())
        raise TypeError('Not root node')
        
    def nameValid():
        """ name != None"""
        return self.name != None
          
    def linksValid():
        """ links != None and links != []"""
        if self.links != None:
            return self.links != []
        return self.links == None
 
    def archetypedValid():
        """ isArchetypeRoot xor archetypeDetails = None """
        return xor(self.isArchetypeRoot(), self.archetypeDetails == None)
        
    def archetypeNodeIdValid():
        """ archetypeNodeId != None and archetypeNodeId != '' """
        if(self.archetypeNodeId != None):
            return self.archetypeNodeId != ''
        return self.archetypeNodeId == None
        


class IArchetyped(Interface):
    """
    Archetypes act as the configuration basis for the particular structures of instances
    defined by the reference model. To enable archetypes to be used to create valid
    data, key classes in the reference model act as "root" points for archetyping;
    accordingly, these classes have the archetype_details attribute set. An instance of
    the class ARCHETYPED contains the relevant archetype identification information,
    allowing generating archetypes to be matched up with data instances
    """

    archetypeId = Object(
        schema=IArchetypeId,
        title=_(u"Archetype ID"),
        description=_(u"Globally unique archetype identifier."),
        
        )
    
    templateId = Object(
        schema=ITemplateId,
        title=_(u"Template ID"),
        description=_(u"""Globally unique template identifier, if a template was active at 
                    this point in the structure. Normally, a template would only be used 
                    at the top of a top-level structure, but the possibility exists for 
                    templates at lower levels."""),
        required=False,
        )
    
    rmVersion = TextLine(
        title=_(u"RM Version"),
        description=_(u"""Version of the openEHR reference model used to create this object.
                    Expressed in terms of the release version string, e.g. "1.0", "1.2.4". """),
        
        )
        

    def archetypeIdValid():
        """ archetypeId != None """
        
    def rmVersionValid():
        """ rmVersion != None and rmVersion != '' """


class Archetyped(Locatable):
    """
    Archetypes act as the configuration basis for the particular structures of instances
    defined by the reference model. To enable archetypes to be used to create valid
    data, key classes in the reference model act as "root" points for archetyping;
    accordingly, these classes have the archetype_details attribute set. An instance of
    the class ARCHETYPED contains the relevant archetype identification information,
    allowing generating archetypes to be matched up with data instances
    """
    
    implements(IArchetyped)
    
            
    def __init__(self,atid,tmplid,rmver):
        
        self.archetypeId=atid
        self.templateId=tmplid
        self.rmVersion=rmver
            

    def archetypeIdValid():
        """ archetypeId != None """
        
    def rmVersionValid():
        """ rmVersion != None and rmVersion != '' """


class IFeederAuditDetails(Interface):
    u"""
    Audit details for any system in a feeder system chain. Audit details here means
    the general notion of who/where/when the information item to which the audit is
    attached was created. None of the attributes is defined as mandatory, however, in
    different scenarios, various combinations of attributes will usually be mandatory.
    This can be controlled by specifying feeder audit details in legacy archetypes.
    """

    systemId = TextLine(
        title=_(u'System Id'),
        description=_(u"""Identifier of the system which handled the information item."""),
        
        )
    
    provider = Object(
        schema=IPartyIdentified,
        title=_(u'Provider'),
        description=_(u"""Optional provider(s) who created, committed, forwarded or otherwise 
        handled the item. Type == PARTY_IDENTIFIED"""),
        required=False,
        )
    
    location = Object(
        schema=IPartyIdentified,
        title=_(u'Location'),
        description=_(u"""Identifier of the particular site/facility within an organisation 
                    which handled the item. For computability, this identifier needs to be 
                    e.g. a PKI identifier which can be included in the identifier list of 
                    the PARTY_IDENTIFIED object."""),
        required=False,
        )
    
    time = Object(
        schema=IDvDateTime,
        title=_(u'Time'),
        description=_(u"""Time of handling the item. For an originating time: DV_DATE_TIME system, 
                    this will be time of creation, for an intermediate feeder system, this will 
                    be a time of accession or other time of handling, where available."""),
        required=False,
        )
    
    subject = Object(
        schema=IPartyProxy,
        title=_(u'Subject'),
        description=_(u"""Identifiers for subject of the received information item."""),
        required=False,
        )
    
    versionId = TextLine(
        title=_(u'Version Id'),
        description=_(u"""Any identifier used in the system such as "interim", "final", 
                      or numeric versions if available."""),
        required=False,
        )
    
    def systemIdValid():
        u"""systemId != None and  systemId != '' """
        
        
        
class FeederAuditDetails(grok.Model):
    u"""
    Audit details for any system in a feeder system chain. Audit details here means
    the general notion of who/where/when the information item to which the audit is
    attached was created. None of the attributes is defined as mandatory, however, in
    different scenarios, various combinations of attributes will usually be mandatory.
    This can be controlled by specifying feeder audit details in legacy archetypes.
    """

    implements(IFeederAuditDetails)
    
    def __init__(self,sysid,provider,location,time,subject,verid):
        
      
        self.systemId=sysid
        self.provider=provider
        self.location=location
        self.time=time
        self.subject=subject
        self.versionId=verid
    
    def systemIdValid():
        u"""systemId != None and  systemId != '' """
        
        
        
        
class FeederAudit(Locatable):
    """
    Audit and other meta-data for systems in the feeder chain.
    """

    implements(IFeederAudit)
    
    def __init__(self,orgsysaudit,orgsysids,fsaudit,fsauditids,orgcontent):
        
       
        self.originatingSystemAudit=orgsysaudit
        self.originatingSystemItemIds=orgsysids
        self.feederSystemAudit=fsaudit
        self.feederSystemItemIds=fsauditids
        self.originalContent=orgcontent        
     
    def originatingSystemAuditValid():
        """ originatingSystemAudit != None """
        
        

class Link(Locatable):
    """
    The LINK type defines a logical relationship between two items, such as two
    ENTRYs or an ENTRY and a COMPOSITION. Links can be used across composi-
    tions, and across EHRs. Links can potentially be used between interior (i.e. non
    archetype root) nodes, although this probably should be prevented in archetypes.
    Multiple LINKs can be attached to the root object of any archetyped structure to
    give the effect of a 1->N link 1:1 and 1:N relationships between archetyped content 
    elements (e.g. ENTRYs) can be expressed by using one, or more than one, respectively, DV_LINKs.
    Chains of links can be used to see "problem threads" or other logical groupings of items.
    Links should be between archetyped structures only, i.e. between objects representing 
    complete domain concepts because relationships between sub-elements
    of whole concepts are not necessarily meaningful, and may be downright confusing. Sensible 
    links only exist between whole ENTRYs, SECTIONs, COMPOSITIONs and so on.
    """
    
    implements(ILink)
    
    def __init__(self,meaning,type,target):
        
        
        self.meaning=meaning
        self.type=type
        self.target=target
     
    def meaningValid():
        """Return meaning != None """
        
    def typeValid():
        """Return type != None """
        
    def targetValid():
        """Return target != None """





#Begin the Change Control package
class IContribution(Interface):
    u"""
    Documents a contribution of one or more versions added to a change-controlled repository.
    """
    
    uid=Object(
        schema=IHierObjectId,
        title=_(u'UID'),
        description=_(u"""Unique identifier for this contribution."""),
        required=True
    )
    
    versions=Set(
        value_type=TextLine(),
        title=_(u'Versions'),
        description=_(u"""Set of references to versions causing changes to
                      this EHR. Each contribution contains a list of versions
                      which may include paths pointing to any number of 
                      VERSIONABLE items, i.e. items of type COMPOSITION and FOLDER."""),
        required=True
    )
   
    audit=Object(
        schema=IAuditDetails,
        title=_(u'Audit'),
        description=_(u"""Audit trail corresponding to the committal of this Contribution."""),
        required=True
    )
    
    
    
class Contribution(grok.Container):
    u"""
    Documents a contribution of one or more versions added to a change-controlled repository.
    """
    
    implements(IContribution)
    
    def __init__(self,uid,versions,audit):
        self.uid=uid
        self.versions=versions
        self.audit=audit
        
class IVersion(Interface):
    u"""
    Abstract model of one Version within a Version container, containing 
    data, commit audit trail, and the identifier of its Contribution.
    """

    
    
    uid = Object(
        schema=IObjectVersionId,
        title=_(u'UID'),
        description=_(u"""Unique identifier of this version, containing
                    owner_id, version_tree_id and creating_system_id.
                    Type == OBJECT_VERSION_ID"""),
        
        )
    
    precedingVersionId = Object(
        schema=IObjectVersionId,
        title=_(u'Preceding Version Id'),
        description=_(u"""Unique identifier of the version of which this version 
                    is a modification; Void if this is the first version.
                    Type == OBJECT_VERSION_ID"""),
        required=False,
        )
    
    data = Field(
        title=_(u'Data'),
        description=_(u"""Original content of this Version."""),
        required=False,
        )
    
    lifecycleState = Object(
        schema=IDvCodedText,
        title=_(u'Lifecycle State'),
        description=_(u"""Lifecycle state of this version; coded by openEHR 
                    vocabulary "version lifecycle state". 
                    Type == DV_CODED_TEXT"""),
        
        )
    
    
    commitAudit = Object(
        schema=IAuditDetails,
        title=_(u'Commit Audit'),
        description=_(u"""Audit trail corresponding to the committal of this
                    version to the VERSIONED_OBJECT. Type == AUDIT_DETAILS"""),
        
        )
    
    contribution = Object(
        schema=IObjectRef,
        title=_(u'Contribution'),
        description=_(u"""Contribution in which this version was added."""),
        
        )
    
    signature = TextLine(
        title=_(u'Signature'),
        description=_(u"""OpenPGP digital signature or digest of content 
                    committed in this Version."""),
        required=False,
        )
    
                        
    def ownerId():
        u"""Unique identifier of the owning VERSIONED_OBJECT.
        Type == HIER_OBJECT_ID"""
        
    def isBranch():
        u"""True if this Version represents a branch. 
        Derived from uid attribute."""
        
    def canonicalForm():
        u"""Canonical form of Version object, created by serialising all 
        attributes except signature."""
    
    def uidValid():
        u"""uid != None"""
        
    def ownerIdValid():
        u"""ownerId != None and owner_id.value.is_equal(uid.object_id.value)"""
        
    def CommitAuditValid():
        u"""commitAudit != None"""
        
"""       Contribution_valid: contribution /= Void and contribution.type.is_equal("CON-
          TRIBUTION")
          Preceding_version_uid_validity: uid.version_tree_id.is_first xor
          preceding_version_uid /= Void
          Lifecycle_state_valid: lifecycle_state /= Void and then
          terminology(Term_id_openehr).
          has_code_for_group_id(Group_id_version_lifecycle_state,
          lifecycle_state.defining_code)

"""


class Version(grok.Model):
    u"""
    Abstract model of one Version within a Version container, containing 
    data, commit audit trail, and the identifier of its Contribution.
    """

    implements(IVersion)
    
    def __init__(self,uid,preVid,data,lcstate,caudit,contr,sig):
        
        
        self.uid=uid
        self.precedingVersionId=preVid
        self.data=data
        self.lifecycleState=lcstate
        self.commitAudit=caudit
        self.signature=sig
                        
    def ownerId():
        u"""Unique identifier of the owning VERSIONED_OBJECT.
        Type == HIER_OBJECT_ID"""
        
    def isBranch():
        u"""True if this Version represents a branch. 
        Derived from uid attribute."""
        
    def canonicalForm():
        u"""Canonical form of Version object, created by serialising all 
        attributes except signature."""
    
    def uidValid():
        u"""uid != None"""
        
    def ownerIdValid():
        u"""ownerId != None and owner_id.value.is_equal(uid.object_id.value)"""
        
    def CommitAuditValid():
        u"""commitAudit != None"""
        
"""       Contribution_valid: contribution /= Void and contribution.type.is_equal("CON-
          TRIBUTION")
          Preceding_version_uid_validity: uid.version_tree_id.is_first xor
          preceding_version_uid /= Void
          Lifecycle_state_valid: lifecycle_state /= Void and then
          terminology(Term_id_openehr).
          has_code_for_group_id(Group_id_version_lifecycle_state,
          lifecycle_state.defining_code)

"""

class IOriginalVersion(Interface):
    u"""
    A Version containing locally created content and optional attestations.
    """
    
    uid=Object(
        schema=IObjectVersionId,
        title=_(u"UID"),
        description=_(u"""Stored version of inheritence precursor."""),
        required=True
    )
    
    precedingVersionUid=Object(
        schema=IObjectVersionId,
        title=_(u"Preceding Version UID"),
        description=_(u"""Stored version of inheritence precursor."""),
        required=True
    )
   
class IImportedVersion(Interface):
    u"""
    A Version containing locally created content and optional attestations.
    """
    
    item=Object(
        schema=IOriginalVersion,
        title=_(u"Item"),
        description=_(u"""Original Version object that was imported."""),
        required=True
    )
    
     
class ImportedVersion(Version):
    u"""
    A Version containing locally created content and optional attestations.
    """
    implements(IImportedVersion)
    
    def __init__(self,item):
        
        self.item = item
        
   

     
    
class OriginalVersion(grok.Container):
    u"""
    A Version containing locally created content and optional attestations.
    """
    
    implements(IOriginalVersion)
    
    def __init__(self,uid,previd):
                
        self.uid=uid
        self.precedingVersionUid=previd
        
    
class IVersionedObject(Interface):
    u"""
    Version control abstraction, defining semantics for versioning one 
    complex object.
    """
    
    uid = Object(
        schema=IHierObjectId,
        title=_(u'UID'),
        description=_(u"""Unique identifier of this version container. This id 
                    will be the same in all instances of the same container 
                    in a distributed environment, meaning that it can be 
                    understood as the uid of the "virtual version tree"."""),
        
        )
    
    ownerId = Object(
        schema=IObjectRef,
        title=_(u'Owner Id'),
        description=_(u"""Reference to object to which this version container 
                    belongs, e.g. the id of the containing EHR or other 
                    relevant owning entity."""),
        
        )
    
    timeCreated = Object(
        schema=IDvDateTime,
        title=_(u'Time Created'),
        description=_(u"""Time of initial creation of this versioned object."""),
        
        )
    
    def allVersions():
        u"""Return a list of all versionsin this object. List <VERSION<T>>"""
        
    def allVersionIds():
        u"""Return a list of ids of all versions in this object.
        List <OBJECT_VERSION_ID>"""
        
    def versionCount():
        u"""Return the total number of versions in this object as an Integer."""
        
    def hasVersionId(an_id):
        u"""Return True if an_id exists. Require an_id != None 
        and an_id != '' """ 

    def isOriginalVersion(an_id):
        u"""True if version with an_id is an ORIGINAL_VERSION.
        Require an_id != None and hasVersionId(an_id)"""
        
    def hasVersionAtTime(a_time):
        u"""Return True if a version for time; 'a_time' exists. 
        Require isinstance(a_time, datetime)."""

    def versionWithId(an_id):
        u"""Return the version with id of 'an_id'. 
        Require hasVersionId(an_id)"""
        
    def versionAtTime(a_time):
        u"""Return the version for time 'a_time'. 
        Require hasVersionAtTime(a_time)."""
        
    def latestVersion():
        u"""Return the most recently added version (i.e. on trunk
        or any branch)."""
        
    def latestTrunkVersion():
        u"""Return the most recently added trunk version."""
        
    def trunkLifecycleState():
        u"""Return the lifecycle state from the latest trunk version. 
        Useful for determining if the version container is logically deleted.
        """
    
    def revisionHistory():
        u"""History of all audits and attestations in this versioned 
        repository."""
        
    def commitOriginalVersion():
        u""" 
        Add a new original version.
        (a_contribution: OBJECT_REF; a_new_version_uid, 
        a_preceding_version_uid: OBJECT_VERSION_ID; an_audit: AUDIT_DETAILS;
        a_lifecycle_state: DV_CODED_TEXT; a_data: T; signing_key: String)

        Require
        contributionValid: a_contribution /= Void
        newVersionValid: a_new_version_uid /= Void
        precedingVersionUidValid:all_version_ids.has(a_preceding_version_uid) 
        or else version_count = 0
        audit_valid: an_audit /= Void
        data_valid: a_version_data /= Void
        lifecycle_state_valid: a_lifecycle_state /= Void
        """

    def commitOriginalMergedVersion():
        u"""Add a new original merged version. This commit function adds a 
        parameter containing the ids of other versions merged into the 
        current one.
                                                  
        (a_contribution: OBJECT_REF;a_new_version_uid, a_preceding_version_uid:    
        OBJECT_VERSION_ID; an_audit: AUDIT_DETAILS; a_lifecycle_state: 
        DV_CODED_TEXT; a_data: T; an_other_input_uids:Set<OBJECT_VERSION_ID>;
        signing_key: String)
        
        Require
        Contribution_valid: a_contribution /= Void
        New_version_valid: a_new_version_uid /= Void
        Preceding_version_id_valid: all_version_ids.has(a_preceding_version_uid)
        or else version_count = 0
        audit_valid: an_audit /= Void
        data_valid: a_version_data /= Void
        lifecycle_state_valid: a_lifecycle_state /= Void
        Merge_input_ids_valid: an_other_input_uids /= Void
        """
        
    def commitImportedVersion(a_contribution, an_audit, a_version):
        u"""Add a new imported version. Details of version id etc come from the
        ORIGINAL_VERSION being committed.  
        
        (a_contribution: OBJECT_REF; an_audit: AUDIT_DETAILS; 
        a_version: ORIGINAL_VERSION<T>)
         
        Require
        Contribution_valid: a_contribution /= Void
        audit_valid: an_audit /= Void
        Version_valid: a_version /= Void
        """


    def commitAttestation(an_attestation, a_ver_id, signing_key):
        u"""Add a new attestation to a specified original version. Attestations
        can only be added to Original versions.
        
        an_attestation: ATTESTATION; a_ver_id: OBJECT_VERSION_ID; signing_key: String)
        
        Require
        Attestation_valid: an_attestation /= Void
        Version_id_valid: has_version_id(a_ver_id) and is_original_version(a_ver_id)
        """

    def uidValid():
        u"""uid != None"""
        
    def ownerIdValid():
        u"""owner_id != None"""
        
    def timeCreatedValid():
        u"""timeCreated != None"""
        
    def versionCountValid():
        u"""versionCount >= 0"""
        
    def allVersionIdsValid():
        u"""allVersionIds != None and allVersionIds.count = versionCount"""
        
    def allVersionsValid():
        u"""allVersions != None and allVersions.count = versionCount"""
        
    def latestVersionValid():
        u"""versionCount > 0 implies latestVersion != None"""
        
    def revisionHistoryValid():
        u"""revisionHistory != None"""
  
        
class VersionedObject(grok.Container):
    u"""
    Version control abstraction, defining semantics for versioning one 
    complex object.
    """
    
    implements(IVersionedObject)
    
    def __init__(self,uid,ownerId,timeCreated):
               
        self.uid=uid
        self.ownerId=ownerId
        self.timeCreated=timeCreated
     
    def allVersions():
        u"""Return a list of all versionsin this object. List <VERSION<T>>"""
        
    def allVersionIds():
        u"""Return a list of ids of all versions in this object.
        List <OBJECT_VERSION_ID>"""
        
    def versionCount():
        u"""Return the total number of versions in this object as an Integer."""
        
    def hasVersionId(an_id):
        u"""Return True if an_id exists. Require an_id != None 
        and an_id != '' """ 

    def isOriginalVersion(an_id):
        u"""True if version with an_id is an ORIGINAL_VERSION.
        Require an_id != None and hasVersionId(an_id)"""
        
    def hasVersionAtTime(a_time):
        u"""Return True if a version for time; 'a_time' exists. 
        Require isinstance(a_time, datetime)."""

    def versionWithId(an_id):
        u"""Return the version with id of 'an_id'. 
        Require hasVersionId(an_id)"""
        
    def versionAtTime(a_time):
        u"""Return the version for time 'a_time'. 
        Require hasVersionAtTime(a_time)."""
        
    def latestVersion():
        u"""Return the most recently added version (i.e. on trunk
        or any branch)."""
        
    def latestTrunkVersion():
        u"""Return the most recently added trunk version."""
        
    def trunkLifecycleState():
        u"""Return the lifecycle state from the latest trunk version. 
        Useful for determining if the version container is logically deleted.
        """
    
    def revisionHistory():
        u"""History of all audits and attestations in this versioned 
        repository."""
        
    def commitOriginalVersion():
        u""" 
        Add a new original version.
        (a_contribution: OBJECT_REF; a_new_version_uid, 
        a_preceding_version_uid: OBJECT_VERSION_ID; an_audit: AUDIT_DETAILS;
        a_lifecycle_state: DV_CODED_TEXT; a_data: T; signing_key: String)

        Require
        contributionValid: a_contribution /= Void
        newVersionValid: a_new_version_uid /= Void
        precedingVersionUidValid:all_version_ids.has(a_preceding_version_uid) 
        or else version_count = 0
        audit_valid: an_audit /= Void
        data_valid: a_version_data /= Void
        lifecycle_state_valid: a_lifecycle_state /= Void
        """

    def commitOriginalMergedVersion():
        u"""Add a new original merged version. This commit function adds a 
        parameter containing the ids of other versions merged into the 
        current one.
                                                  
        (a_contribution: OBJECT_REF;a_new_version_uid, a_preceding_version_uid:    
        OBJECT_VERSION_ID; an_audit: AUDIT_DETAILS; a_lifecycle_state: 
        DV_CODED_TEXT; a_data: T; an_other_input_uids:Set<OBJECT_VERSION_ID>;
        signing_key: String)
        
        Require
        Contribution_valid: a_contribution /= Void
        New_version_valid: a_new_version_uid /= Void
        Preceding_version_id_valid: all_version_ids.has(a_preceding_version_uid)
        or else version_count = 0
        audit_valid: an_audit /= Void
        data_valid: a_version_data /= Void
        lifecycle_state_valid: a_lifecycle_state /= Void
        Merge_input_ids_valid: an_other_input_uids /= Void
        """
        
    def commitImportedVersion(a_contribution, an_audit, a_version):
        u"""Add a new imported version. Details of version id etc come from the
        ORIGINAL_VERSION being committed.  
        
        (a_contribution: OBJECT_REF; an_audit: AUDIT_DETAILS; 
        a_version: ORIGINAL_VERSION<T>)
         
        Require
        Contribution_valid: a_contribution /= Void
        audit_valid: an_audit /= Void
        Version_valid: a_version /= Void
        """


    def commitAttestation(an_attestation, a_ver_id, signing_key):
        u"""Add a new attestation to a specified original version. Attestations
        can only be added to Original versions.
        
        an_attestation: ATTESTATION; a_ver_id: OBJECT_VERSION_ID; signing_key: String)
        
        Require
        Attestation_valid: an_attestation /= Void
        Version_id_valid: has_version_id(a_ver_id) and is_original_version(a_ver_id)
        """

    def uidValid():
        u"""uid != None"""
        
    def ownerIdValid():
        u"""owner_id != None"""
        
    def timeCreatedValid():
        u"""timeCreated != None"""
        
    def versionCountValid():
        u"""versionCount >= 0"""
        
    def allVersionIdsValid():
        u"""allVersionIds != None and allVersionIds.count = versionCount"""
        
    def allVersionsValid():
        u"""allVersions != None and allVersions.count = versionCount"""
        
    def latestVersionValid():
        u"""versionCount > 0 implies latestVersion != None"""
        
    def revisionHistoryValid():
        u"""revisionHistory != None"""
        
        
        

#Begin Directory package
class IFolder(Interface):
    u"""
    The concept of a named folder.
    """

    folders = List(
        value_type=Object(schema=IObjectRef), # documented as a list of folders
        title=_(u"Folders"),
        description=_(u"""Subfolders of this folder."""),
        required=False,
        )
    
    items = List(
        value_type=Object(schema=IObjectRef),
        title=_(u"Items"),
        description=_(u"""The list of references to other (usually) versioned 
                    objects logically in this folder."""),
        required=False,
        )
    
    def foldersValid():
        u"""folders != None and folders != '' """

        
class Folder(Locatable):
    u"""
    The concept of a named folder.
    """

    implements(IFolder)
    
    def __init__(self,folders,items):
               
        self.folders=folders
        self.items=items    
    
    def foldersValid():
        u"""folders != None and folders != '' """
  
class IVersionedFolder(Interface):
    u"""
    A version-controlled hierarchy of FOLDERs giving the effect of a directory.
    """
    pass

class VersionedFolder(VersionedObject):
    u"""
    A version-controlled hierarchy of FOLDERs giving the effect of a directory.
    """
    
    implements(IVersionedFolder)
    
    def __init__(self,ownerId,timeCreated,uid):
        VersionedObject.__init__(ownerId,timeCreated,uid)
    




class AuditDetails(grok.Model):
    u"""
    The set of attributes required to document the committal of an information 
    item to a repository.
    """
    
    implements(IAuditDetails)
    
    def __init___(self,systemId,committer,timeCommited,changeType,description):
        
        self.systemId=systemId
        self.committer=committer
        self.timeCommitted=timeCommited
        self.changeType=changeType
        self.description=description
        

class IAttestation(Interface):
    u"""
    Record an attestation of a party (the committer) to item(s) of record content. 
    The type of attestation is
    """
    
    attestedView = Object(
        schema=IDvMultimedia,
        title=_(u'Attested View'),
        description=_(u"""Optional visual representation of content attested e.g. 
                    screen image. Type==DvMultimedia"""),
        required=False,
        )
    
    proof = TextLine(
        title=_(u'Proof'),
        description=_(u"""Proof of attestation."""),
        required=False,
        )
    
    items = Set(
        value_type=Object(IDvEhrUri),
        title=_(u'Items'),
        description=_(u"""Items attested, expressed as fully qualified runtime 
                    paths to the items in question. Although not recommended, 
                    these may include fine-grained items which have been 
                    attested in some other system. Otherwise it is assumed to
                    be for the entire VERSION with which it is associated. 
                    Set <DV_EHR_URI>"""),
        required=False,
        )
 
    
    reason = Object(
        schema=IDvText,
        title=_(u'Reason'),
        description=_(u"""Reason of this attestation. Optionally coded by the 
                    openEHR Terminology group "attestation reason"; includes 
                    values like "authorisation", "witness" etc."""),
        
        )
    
    isPending = Bool(
        title=_(u'Pending?'),
        description=_(u"""True if this attestation is outstanding; 
                    False means it has been completed."""),
        
        )
    
    def itemsValid():
        u"""items != None items != '' """
        
    def reasonValid():
        u"""reason != None and then(reason.generating_type.is_equal("DV_CODED_TEXT") 
        implies terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_attestation_reason, reason.defining_code))"""
        
    
class Attestation(AuditDetails):
    u"""
    Record an attestation of a party (the committer) to item(s) of record content. 
    The type of attestation is
    """
    
    implements(IAttestation)
    
    
    def __init__(self,aview,proof,items,reason,ispend):
        
       
        self.attestedView=aview
        self.proof=proof
        self.items=items
        self.reason=reason
        self.isPending=ispend
   
    def itemsValid():
        u"""items != None items != '' """
        
    def reasonValid():
        u"""reason != None and then(reason.generating_type.is_equal("DV_CODED_TEXT") 
        implies terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_attestation_reason, reason.defining_code))"""
        
        

        
class IParticipation(Interface):
    u"""
    Model of a participation of a Party (any Actor or Role) in an activity.
    
    Used to represent any participation of a Party in some activity, which is 
    not explicitly in the model, e.g. assisting nurse. Can be used to record 
    past or future participations.
        
    Should not be used in place of more permanent relationships between demographic entities.
    """
    
    performer = Object(
        schema=IPartyProxy,
        title=_(u'Performer'),
        description=_(u"""The id and possibly demographic system link of performer: 
                    (PartyProxy) the party participating in the activity."""),
        
        )
    
    function = Object(
        schema=IDvText,
        title=_(u'Function'),
        description=_(u"""The function of the Party in this participation (note 
                    that a given party might participate in more than one way 
                    in a particular activity). This attribute should be coded, 
                    but cannot be limited to the HL7v3:ParticipationFunction 
                    vocabulary, since it is too limited and hospital-oriented."""),
        
        )
    
    mode = Object(
        schema=IDvCodedText,
        title=_(u'Mode'),
        description=_(u"""The mode of the performer / activity interaction, e.g. 
                    present, by telephone, by email etc. Type == DvCodedText"""),
        
        )
    
    time = Object(
        schema=IDvInterval,
        title=_(u'Time Interval'),
        description=_(u"""The time interval during which the participation took 
                    place, if it is used in an observational context (i.e. 
                    recording facts about the past); or the intended time 
                    interval of the participation when used in future contexts,
                    such as EHR Instructions."""),
        required=False,
        )
    
    
    def performerValid():
        u"""performer != None"""
        
    def functionValid():
        u"""function != None and then function.generating_type.is_equal("DV_CODED_TEXT") 
        implies terminology(Terminology_id_openehr).has_code_for_group_id(Group_id_participation_function, 
        function.defining_code)"""
        
    def modeValid(): 
        u"""mode != None and terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_participation_mode, mode.defining_code)"""
        
        
        
class Participation(grok.Model):
    
    implements(IParticipation)
    
    def __init__(self,performer,function,mode,time):
        self.performer=performer
        self.function=function
        self.mode=mode
        self.time=time
        
        
   
        

    
class PartyIdentified(Locatable):
    """
    An identity owned by a party.
    """
    
    implements(IPartyIdentified)
    
    def __init__(self,name,identifiers):
        self.name=name
        self.identifiers=identifiers
        
    
    def asString():
        """
        Indentity in the form of a string.
        """
    
class PartyProxy(grok.Model):
    u"""
    Abstract concept of a proxy description of a party, including an optional 
    link to data for this party in a demographic or other identity management 
    system. Subtyped into PARTY_IDENTIFIED and PARTY_SELF.
    """
    
    implements(IPartyProxy)
    
    def __init__(self,extref):
        
        
        self.externalRef=extref
        
class IPartyRelated(Interface):
    u"""
    Proxy type for identifying a party and its relationship to the subject of 
    the record.

    Use where the relationship between the party and the subject of the record 
    must be known.
    """

    relationship = Object(
        schema=IDvCodedText,
        title=_(u'Relationship'),
        description=_(u"""Relationship of subject of this ENTRY to the subject
                    of the record. May be coded. If it is the patient, coded 
                    as "self"."""),
        
        )
    
    def relationshipValid():
        u"""relationship != None and relationship in the relationship 
        vocabulary."""

class PartyRelated(PartyIdentified):
    u"""
    Proxy type for identifying a party and its relationship to the subject of 
    the record.
    
    Use where the relationship between the party and the subject of the record 
    must be known.
    """
    
    implements(IPartyRelated)
    
    def __init__(self,relationship):
        

        self.relationship=relationship
        
    
    def relationshipValid():
        u"""relationship != None and relationship in the relationship 
        vocabulary."""

        
class IPartySelf(Interface):
    u"""
    Party proxy representing the subject of the record.
    Used to indicate that the party is the owner of the record. May or may 
    not have external_ref set.
    """
    pass

    
class PartySelf(grok.Model):
    
    implements(IPartySelf)
    
    def __init__(self):
        
        pass
    
class IRevisionHistoryItem(Interface):
    u"""
    An entry in a revision history, corresponding to a version from a versioned 
    container. Consists of AUDIT_DETAILS instances with revision identifier of 
    the revision to which the AUDIT_DETAILS intance belongs.
    """

    audits = List(
        value_type=Object(IAuditDetails),
        title=_(u'Audits'),
        description=_(u"""The audits for this revision; there will always be at 
                    least one commit audit (which may itself be an ATTESTATION), 
                    there may also be further attestations."""),
        
        )
    
    versionId = Object(
        schema=IObjectVersionId,
        title=_(u'Version Id'),
        description=_(u"""Version identifier for this revision."""),
        
        )
    
    def auditValid():
        u"""audits != None and audits != ' """

    def versionIdValid():
        u"""versionId != None"""
        
        

class RevisionHistoryItem(grok.Model):
    u"""
    An entry in a revision history, corresponding to a version from a versioned 
    container. Consists of AUDIT_DETAILS instances with revision identifier of 
    the revision to which the AUDIT_DETAILS intance belongs.
    """
    
    implements(IRevisionHistoryItem)
    
    def __init__(self,audits,verid):
        self.audits=audits
        self.versionId=verid

   
    def auditValid():
        u"""audits != None and audits != ' """

    def versionIdValid():
        u"""versionId != None"""
        
        
class IRevisionHistory(Interface):
    u"""
    Defines the notion of a revision history of audit items, each associated 
    with the version for which that audit was committed. The list is in 
    most-recent-first order.
    """

    items = List(
        value_type=TextLine(),
        title=_(u'Items'),
        description=_(u"""The items in this history in most-recent-last order."""),
        
        )

    def mostRecentVersion():
        u"""The version id of the most recent item, as a String. 
        Ensure Result.is_equal(items.last.version_id.value)"""
        
    def mostRecentVersionTimeCommitted():
        u"""The commit date/time of the most recent item, as a string.
        Ensure Result.is_equal(items.last.audits.first.time_committed.value)"""
        
    def itemsValid():
        u"""items != None """
        
      
class RevisionHistory(grok.Model):
    u"""
    Defines the notion of a revision history of audit items, each associated 
    with the version for which that audit was committed. The list is in 
    most-recent-first order.
    """

    implements(IRevisionHistory)
    
    def __init__(self,items):
        self.items=items

    def mostRecentVersion():
        u"""The version id of the most recent item, as a String. 
        Ensure Result.is_equal(items.last.version_id.value)"""
        
    def mostRecentVersionTimeCommitted():
        u"""The commit date/time of the most recent item, as a string.
        Ensure Result.is_equal(items.last.audits.first.time_committed.value)"""
        
    def itemsValid():
        u"""items != None """
        
        
class ITranslationDetails(Interface):
    u""""""

    language=Object(
        schema=ICodePhrase,
        title=_(u'Language'),
        description=_(u""" """),
        required=True
    )

    author=Dict(
        title=_(u'Author'),
        description=_(u""" """),
        required=True
    )
    
    accreditation=TextLine(
        title=_(u'Accreditation'),
        description=_(u""""""),
        required=False
    )    
    
    otherDetails=Dict(
        title=_(u'Other Details'),
        description=_(u""""""),
        required=False
    )
    
class IResourceDescription(Interface):
    u"""Defines the descriptive meta-data of a resource."""
    
    originalAuthor=Dict(
        title=_(u'Original Author'),
        description=_(u""""""),
        required=True
    )
    
    otherContributors=List(
        value_type=TextLine(),
        title=_(u'Other Contributors'),
        description=_(u""""""),
        required=False
    )
    
    lifecycleState=TextLine(
        title=_(u'Lifecycle State'),
        description=_(u""""""),
        required=True
    )
    
    details=Dict(
        title=_(u'Details'),
        description=_(u""""""),
        required=True
    )
    
    resourcePackageUri=TextLine(
        title=_(u'Resource Package URI'),
        description=_(u""""""),
        required=False
    )
    
    otherDetails=Dict(
        title=_(u'Other Details'),
        description=_(u""""""),
        required=False
    )
    
    parentResource=Object(
        schema=IObjectRef,
        title=_(u'Parent Resource'),
        description=_(u""""""),
        required=False
    )   
    
class IAuthoredResource(Interface):
    u"""Abstract idea of an online resource created by a human author. """
    
    orignialLanguage=Object(
        schema=ICodePhrase,
        title=_(u"Original Language"),
        description=_(u"""Original Language"""),
        required=True
    )
       
    translations=Object(
        schema=ITranslationDetails,
        title=_(u"Translations"),
        description=_(u"Translations"),
        required=False
    )
    
    
    description=Object(
        schema=IResourceDescription,
        title=_(u"Description"),
        description=_(u""""""),
        required=False
    )
       
    revisionHistory=Object(
        schema=IRevisionHistory,
        title=_(u"Revision History"),
        description=_(u""""""),
        required=False
    )
    
    isControlled=Bool(
        title=_(u"Is Controlled"),
        description=_(u""""""),
        required=True
    )
    
    def currentRevision():
        u""""""
        
    def languagesAvailable():
        u""""""
        
        
        
class AuthoredResource(grok.Container):
    u"""Abstract idea of an online resource created by a human author. """
    
    implements(IAuthoredResource)
    
    
    def __init__(self, olang,trans,descr,revhist,ctrld):
        self.originalLanguage=olang
        self.translations=trans
        self.description=descr
        self.revisionHistory=revhist
        self.isControlled=ctrld

    def currentRevision():
        u""" """
         
    def languagesAvailable():
        u""" """
                                
            
class IResourceDescriptionItem(Interface):
    u"""Language-specific detail of resource description. When a resource is translated
        for use in another language environment, each RESOURCE_DESCRIPTION_ITEM
        needs to be copied and translated into the new language.
    """
    
    language=Object(
        schema=ICodePhrase,
        title=_(u'Language'),
        description=_(u""""""),
        required=True
    )
    
    purpose=TextLine(
        title=_(u'Purpose'),
        description=_(u""""""),
        required=True
    )
    
    keywords=List(
        value_type=TextLine(),
        title=_(u'Keywords'),
        description=_(u""""""),
        required=False
    )
    
    use=TextLine(
        title=_(u'Use'),
        description=_(u""""""),
        required=False
    )

    misuse=TextLine(
        title=_(u'Misuse'),
        description=_(u""""""),
        required=False
    )
    
    copyright=TextLine(
        title=_(u'Copyright'),
        description=_(u""""""),
        required=False
    )
    
    originalResourceUri=Dict(
        title=_(u'Original Resource URI'),
        description=_(u""""""),
        required=False
    )
    
    otherDetails=Dict(
        title=_(u'Other Details'),
        description=_(u""""""),
        required=False
    )
  
class ResourceDescriptionItem(grok.Model):
    u"""Language-specific detail of resource description. When a resource is translated
        for use in another language environment, each RESOURCE_DESCRIPTION_ITEM
        needs to be copied and translated into the new language.
    """

    pass

    

      
class ResourceDescription(grok.Model):
    u"""Defines the descriptive meta-data of a resource."""
    
    pass

    """
    originalAuthor=Dict(
        title=_(u'Original Author'),
        description=_(u""""""),
        required=True
    )
    
    otherContributors=List(
        title=_(u'Other Contributors'),
        description=_(u""""""),
        required=False
    )
    
    lifecycleState=TextLine(
        title=_(u'Lifecycle State'),
        description=_(u""""""),
        required=True
    )
    
    details=Dict(
        title=_(u'Details'),
        description=_(u""""""),
        required=True
    )
    
    resourcePackageUri=TextLine(
        title=_(u'Resource Package URI'),
        description=_(u""""""),
        required=False
    )
    
    otherDetails=Dict(
        title=_(u'Other Details'),
        description=_(u""""""),
        required=False
    )
    
    parentResource=AuthoredResource(
        title=_(u'Parent Resource'),
        description=_(u""""""),
        required=False
    )
    
    """
    
     

      
class TranslationDetails(grok.Model):
    u""" """
    
    implements(ITranslationDetails)
    
    def __init__(self,lang,author,accred,other):
        self.language=lang
        self.author=author
        self.accreditation=accred
        self.otherDetails=other
   


