# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the generic package as described in the 
Common Information Model Rev. 2.1.0 

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__version__ = '1.0.1a1'
__contributors__ = ''

from zope.interface import Interface
from zope.schema import Field
from zope.schema import Text
from zope.schema import TextLine
from zope.schema import List
from zope.schema import Set
from zope.i18nmessageid import MessageFactory

from archetyped import ILocatable

_ = MessageFactory('oship')

class IPartyProxy(ILocatable):
    u"""
    Abstract concept of a proxy description of a party, including an optional 
    link to data for this party in a demographic or other identity management 
    system. Subtyped into PARTY_IDENTIFIED and PARTY_SELF.
    """
    
    externalRef = PartyRef(
        title=_(u"""External Reference"""),
        description=_(u"""Optional reference to more detailed demographic or 
                    identification information for this party, in an external 
                    system. Type == PartyRef."""),
        #constraint = isinstance(PartyRef),
        required=False,
        )
    
class IPartySelf(IPartyProxy):
    u"""
    Party proxy representing the subject of the record.
    Used to indicate that the party is the owner of the record. May or may 
    not have external_ref set.
    """
    
    
class IPartyIdentified(IPartyProxy):
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
        title=_(u"""Name"""),
        description=_(u"""Optional human-readable name (in String form)."""),
        required=False,
        )
    
    identifiers = List(
        title=_(u"""Identifiers"""),
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
        
class IPartyRelated(IPartyIdentified):
    u"""
    Proxy type for identifying a party and its relationship to the subject of 
    the record.

    Use where the relationship between the party and the subject of the record 
    must be known.
    """

    relationship = DvCodedText(
        title=_(u"""Relationship"""),
        description=_(u"""Relationship of subject of this ENTRY to the subject
                    of the record. May be coded. If it is the patient, coded 
                    as “self”."""),
        required=True,
        constraint = isinstance(DvCodedText),
        )
    
    def relationshipValid():
        u"""relationship != None and relationship in the relationship 
        vocabulary."""
        
class IParticipation(Interface):
    u"""
    Model of a participation of a Party (any Actor or Role) in an activity.
    
    Used to represent any participation of a Party in some activity, which is 
    not explicitly in the model, e.g. assisting nurse. Can be used to record 
    past or future participations.
        
    Should not be used in place of more permanent relationships between demographic entities.
    """
    
    performer = PartyProxy(
        title=_(u"""Performer"""),
        description=_(u"""The id and possibly demographic system link of performer: 
                    (PartyProxy) the party participating in the activity."""),
        required=True,
        constraint = isinstance(PartyProxy)
        )
    
    function = DvText(
        title=_(u"""Function"""),
        description=_(u"""The function of the Party in this participation (note 
                    that a given party might participate in more than one way 
                    in a particular activity). This attribute should be coded, 
                    but cannot be limited to the HL7v3:ParticipationFunction 
                    vocabulary, since it is too limited and hospital-oriented."""),
        required=True,
        )
    
    mode = DvCodedText(
        title=_(u"""Mode"""),
        description=_(u"""The mode of the performer / activity interaction, e.g. 
                    present, by telephone, by email etc. Type == DvCodedText"""),
        required=True,
        )
    
    time = DvInterval(
        title=_(u"""Time Interval"""),
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
        u"""function != None and then function.generating_type.is_equal(“DV_CODED_TEXT”) 
        implies terminology(Terminology_id_openehr).has_code_for_group_id(Group_id_participation_function, 
        function.defining_code)"""
        
    def modeValid(): 
        u"""mode != None and terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_participation_mode, mode.defining_code)"""
        
        
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
        required=True,
        )
    
    committer = PartyProxy(
        title=_(u"""Committer"""),
        description=_(u"""Identity and optional reference into identity management
                    service, of user who committed the item."""),
        required=True,
        )
    
    timeCommitted = DvDateTime(
        title=_(u"""Time Committed"""),
        description=_(u"""Time of committal of the item."""),
        required=True,
        )
    
    changeType = DvCodedText(
        title=_(u"""Change Type"""),
        description=_(u"""Type of change. Coded using the openEHR Terminology 
                    “audit change type” group. Type==DvCodedText"""),
        required=True,
        )
    
    description = DvText(
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



class IAttestation(IAuditDetails):
    u"""
    Record an attestation of a party (the committer) to item(s) of record content. 
    The type of attestation is
    """
    
    attestedView = DvMultimedia(
        title=_(u"""Attested View"""),
        description=_(u"""Optional visual representation of content attested e.g. 
                    screen image. Type==DvMultimedia"""),
        required=False,
        )
    
    proof = TextLine(
        title=_(u"""Proof"""),
        description=_(u"""Proof of attestation."""),
        required=False,
        )
    
    items = Set(
        title=_(u"""Items"""),
        description=_(u"""Items attested, expressed as fully qualified runtime 
                    paths to the items in question. Although not recommended, 
                    these may include fine-grained items which have been 
                    attested in some other system. Otherwise it is assumed to
                    be for the entire VERSION with which it is associated. 
                    Set <DV_EHR_URI>"""),
        required=False,
        )
 
    
    reason = DvText(
        title=_(u"""Reason"""),
        description=_(u"""Reason of this attestation. Optionally coded by the 
                    openEHR Terminology group “attestation reason”; includes 
                    values like “authorisation”, “witness” etc."""),
        required=True,
        )
    
    isPending = Bool(
        title=_(u"""Pending?"""),
        description=_(u"""True if this attestation is outstanding; 
                    False means it has been completed."""),
        required=True,
        )
    
    def itemsValid():
        u"""items != None items != '' """
        
    def reasonValid():
        u"""reason != None and then(reason.generating_type.is_equal(“DV_CODED_TEXT”) 
        implies terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_attestation_reason, reason.defining_code))"""
        
        
class IRevisionHistory(Interface):
    u"""
    Defines the notion of a revision history of audit items, each associated 
    with the version for which that audit was committed. The list is in 
    most-recent-first order.
    """

    items = List(
        title=_(u"""Items"""),
        description=_(u"""The items in this history in most-recent-last order."""),
        required=True,
        )

    def mostRecentVersion():
        u"""The version id of the most recent item, as a String. 
        Ensure Result.is_equal(items.last.version_id.value)"""
        
    def mostRecentVersionTimeCommitted():
         u"""The commit date/time of the most recent item, as a string.
         Ensure Result.is_equal(items.last.audits.first.time_committed.value)"""
         
    def itemsValid():
        u"""items != None """
        

class IRevisionHistoryItem(Interface):
    u"""
    An entry in a revision history, corresponding to a version from a versioned 
    container. Consists of AUDIT_DETAILS instances with revision identifier of 
    the revision to which the AUDIT_DETAILS intance belongs.
    """

    audits = List(
        title=_(u"""Audits"""),
        description=_(u"""The audits for this revision; there will always be at 
                    least one commit audit (which may itself be an ATTESTATION), 
                    there may also be further attestations."""),
        required=True,
        )
    
    versionId = ObjectVersionId(
        title=_(u"""Version Id"""),
        description=_(u"""Version identifier for this revision."""),
        required=True,
        )
    
    def auditValid():
        u"""audits != None and audits != ' """

    def versionIdValid():
        u"""versionId != None"""
        