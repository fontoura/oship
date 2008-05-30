# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

These are the interfaces for the archetyped package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.location.interfaces import ILocation
from zope.interface import Interface
from zope.schema import Field,Text,TextLine,List
from zope.i18nmessageid import MessageFactory

from openehr.rm.support.identification import *
from openehr.rm.datatypes.datetm import DvDateTime
from openehr.rm.datatypes.text import DvText
from openehr.rm.common.archetyped import Archetyped

_ = MessageFactory('oship')


class IPathable(ILocation):
    """
    Abstract parent of all classes whose instances are reachable by paths, and which
    know how to locate child object by paths. The parent feature may be implemented 
    as a function or attribute.
    
    The two attributes required for locatable in ZCA is __parent__ and __name__.  
    We inherit those from Location.
    
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
        
class ILocatable(IPathable):
    """
    Root class of all information model classes that can be archetyped.
    """
    

    uid = UidBasedId('',
        title=_(u"UID"),
        description=_(u"Optional globally unique object identifier for root points of archetyped structures. A UidBasedId "),
        required=False,
        )
    
    archetypeNodeId = TextLine(
        title=_("Node ID"),
        description=_(u"""Design-time archetype id of this node taken from its generating archetype;
                     used to build archetype paths. Always in the form of an “at” code, e.g. “at0005”.
                     This value enables a "standardised" name for this node to be generated, by
                     referring to the generating archetype local ontology.
                     
                     At an archetype root point, the value of this attribute is always the stringified
                     form of the archetype_id found in the archetype_details object."""),
        required=True,
        )
    
    name = DvText('','','','','','',
        title=_(u"Name"),
        description=_(u"""DvText type - Runtime name of this fragment, used to build runtime paths. 
                     This is the term provided via a clinical application or batch
                     process to name this EHR construct: its retention in the EHR 
                     faithfully preserves the original label by which this entry
                     was known to end. """),
        required=True,
        )

    archetypeDetails = Archetyped('','','',
        title=_(u"Archetype Details"),
        description=_(u"Details of archetyping used on this node."),
        required=False,
        )
    
    feederAudit = FeederAudit(
        title=_(u"Feeder Audit"),
        description=_(u"""Audit trail from non-openEHR system of original commit of information 
                    forming the content of this node, or from a conversion gateway which has 
                    synthesised this node."""),
        required=False,
        )
    
    
    links = List(
        title=_(u"Links"),
        description=_(u"""Audit trail from non-openEHR system of original commit of information 
                    forming the content of this node, or from a conversion gateway which has 
                    synthesised this node."""),
        required=False,
        )
    
    
    def isArchetypeRoot():
        """True if this node is the root of an archetyped structure."""
        
    def concept():
        """
        Clinical concept of the archetype as a whole (= derived from the
       ‘archetype_node_id’ of the root node) isArchetypeRoot must be True.
       """
        
    def nameValid():
        """ name != None"""
          
    def linksValid():
        """ links != None and links != []"""
 
    def archetypedValid():
        """ isArchetypeRoot xor archetypeDetails = None """
        
    def archetypeNodeIdValid():
        """ archetypeNodeId != None and archetypeNodeId != '' """
        
class IArchetyped(Interface):
    """
    Archetypes act as the configuration basis for the particular structures of instances
    defined by the reference model. To enable archetypes to be used to create valid
    data, key classes in the reference model act as “root” points for archetyping;
    accordingly, these classes have the archetype_details attribute set. An instance of
    the class ARCHETYPED contains the relevant archetype identification information,
    allowing generating archetypes to be matched up with data instances
    """

    archetypeId = ArchetypeId('',
        title=_(u"Archetype ID"),
        description=_(u"Globally unique archetype identifier."),
        required=True,
        )
    
    templateId = TemplatedId('',
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
                    Expressed in terms of the release version string, e.g. “1.0”, “1.2.4”. """),
        required=True,
        default=u"1.0.1",
        )
        

    def archetypeIdValid():
        """ archetypeId != None """
        
    def rmVersionValid():
        """ rmVersion != None and rmVersion != '' """
        
class ILink(ILocatable):
    """
    The LINK type defines a logical relationship between two items, such as two
    ENTRYs or an ENTRY and a COMPOSITION. Links can be used across composi-
    tions, and across EHRs. Links can potentially be used between interior (i.e. non
    archetype root) nodes, although this probably should be prevented in archetypes.
    Multiple LINKs can be attached to the root object of any archetyped structure to
    give the effect of a 1->N link 1:1 and 1:N relationships between archetyped content 
    elements (e.g. ENTRYs) can be expressed by using one, or more than one, respectively, DV_LINKs.
    Chains of links can be used to see “problem threads” or other logical groupings of items.
    Links should be between archetyped structures only, i.e. between objects representing 
    complete domain concepts because relationships between sub-elements
    of whole concepts are not necessarily meaningful, and may be downright confusing. Sensible 
    links only exist between whole ENTRYs, SECTIONs, COMPOSITIONs and so on.
    """
    
    meaning = DvText(
        title=_(u"Meaning"),
        description=_(u"""Used to describe the relationship, usually in clinical terms, such as 
                    “in response to” (the relationship between test results and an order),
                    “follow-up to” and so on. Such relationships can represent any clinically 
                    meaningful connection between pieces of information. Values for meaning 
                    include those described in Annex C, ENV 13606 pt 2 [11] under the categories 
                    of “generic”, “documenting and reporting”,“organisational”,“clinical”,
                    “circumstancial”, and “view management”.  """),
        required=True,
        )
    
    type = DvText(
        title=_(u"Type"),
        description=_(u"""The type attribute is used to indicate a clinical or domain-level meaning 
                    for the kind of link, for example “problem” or “issue”. If type values are 
                    designed appropriately, they can be used by the requestor of EHR extracts to 
                    categorise links which must be followed and which can be broken when the extract 
                    is created. """),
        required=True,
        )
    
    target = DvEhrUri(
        title=_(u"Target"),
        description=_(u"""The logical “to” object in the link relation, as target: 
                    per the linguistic sense of the meaning attribute."""),
        required=True,
        )
    
    def meaningValid():
        """Return meaning != None """
        
    def typeValid():
        """Return type != None """
        
    def targetValid():
        """Return target != None """


class IFeederAudit(ILocatable):
    """
    Audit and other meta-data for systems in the feeder chain.
    """
    
    originatingSystemAudit = FeederAuditDetails(
        title=_(u"Originating System Audit"),
        description=_(u"""Any audit information for the information item from the originating system."""),
        required =True,
        )
    
    originatingSystemItemIds = List(
        title=_(u"Originating System Item IDs"),
        description=_(u"""Identifiers used for the item in the originating system, e.g. filler and placer ids."""),
        required=False,
        )
    
    
    
    feederSystemAudit = FeederAuditDetails(
        title=_(u"Feeder System Audit"),
        description=_(u"""Any audit information for the information item from the feeder system, 
                    if different from the originating system."""),
        required=False,
        )
    
    feederSystemItemIds = List(
        title=_(u"Feeder System Item IDs"),
        description=_(u"""Identifiers used for the item in the feeder system, where the feeder 
                    system is distinct from the originating system. The List contents are restricted to
                    type == DvIdentifiers"""),
        required=False,
        )
    
    originalContent=DvEncapsulated(
        title=_("Original Content"),
        description=_(""" """),
        required=False,
        )
    
    def originatingSystemAuditValid():
        """ originatingSystemAudit != None """

class IFeederAuditDetails(Interface):
    u"""
    Audit details for any system in a feeder system chain. Audit details here means
    the general notion of who/where/when the information item to which the audit is
    attached was created. None of the attributes is defined as mandatory, however, in
    different scenarios, various combinations of attributes will usually be mandatory.
    This can be controlled by specifying feeder audit details in legacy archetypes.
    """

    systemId = TextLine(
        title=_(u"""System Id"""),
        description=_(u"""Identifier of the system which handled the information item."""),
        required=True,
        )
    
    provider = PartyIdentified(
        title=_(u"""Provider"""),
        description=_(u"""Optional provider(s) who created, committed, forwarded or otherwise 
        handled the item. Type == PARTY_IDENTIFIED"""),
        required=False,
        )
    
    location = PartyIdentified(
        title=_(u"""Location"""),
        description=_(u"""Identifier of the particular site/facility within an organisation 
                    which handled the item. For computability, this identifier needs to be 
                    e.g. a PKI identifier which can be included in the identifier list of 
                    the PARTY_IDENTIFIED object."""),
        required=False,
        )
    
    time = DvDateTime('',
        title=_(u"""Time"""),
        description=_(u"""Time of handling the item. For an originating time: DV_DATE_TIME system, 
                    this will be time of creation, for an intermediate feeder system, this will 
                    be a time of accession or other time of handling, where available."""),
        required=False,
        )
    
    subject = PartyProxy(
        title=_(u"""Subject"""),
        description=_(u"""Identifiers for subject of the received information item."""),
        required=False,
        )
    
    versionId = TextLine(
        title=_(u"""Version Id"""),
        description=_(u"""Any identifier used in the system such as “interim”, “final”, 
                      or numeric versions if available."""),
        required=False,
        )
    
    def systemIdValid():
        u"""systemId != None and  systemId != '' """
        