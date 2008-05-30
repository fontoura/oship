# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Implementations for the generic package as described in the 
Common Information Model Rev. 2.1.0 

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__version__ = '1.0.1a1'
__contributors__ = ''

from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.interfaces.generic import *
_ = MessageFactory('oship')

class PartyProxy(Locatable):
    u"""
    Abstract concept of a proxy description of a party, including an optional 
    link to data for this party in a demographic or other identity management 
    system. Subtyped into PARTY_IDENTIFIED and PARTY_SELF.
    """
    
    implements(IPartyProxy)
    
    def __init__(self,extref,**kwargs):
        self.externalRef=extref
        Field.__init__(self,**kwargs)
        
    
class PartySelf(PartyProxy):
    u"""
    Party proxy representing the subject of the record.
    Used to indicate that the party is the owner of the record. May or may 
    not have external_ref set.
    """
    
    implements(IPartySelf)
    
    pass
    
class PartyIdentified(PartyProxy):
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
    
    implements(IPartyIdentified)
    
    def __init__(self,name,idents,**kwargs):
        self.name=name
        self.identifiers=idents
        Field.__init__(self,**kwargs)
        
    def basicValid(obj):
        u"""name None or identifiers != None or external_ref != None"""            
        
    def nameValid():
        u"""name != None and name != '' """
        
    def identifiersValid():
        u"""identifiers != none and identifiers != '' """
        
class PartyRelated(PartyIdentified):
    u"""
    Proxy type for identifying a party and its relationship to the subject of 
    the record.
    
    Use where the relationship between the party and the subject of the record 
    must be known.
    """
    
    implements(IPartyRelated)
    
    def __init__(self,relationship,**kwargs):
        self.relationship=relationship
        
    
    def relationshipValid():
        u"""relationship != None and relationship in the relationship 
        vocabulary."""
        
class Participation(Field):
    u"""
    Model of a participation of a Party (any Actor or Role) in an activity.
    
    Used to represent any participation of a Party in some activity, which is 
    not explicitly in the model, e.g. assisting nurse. Can be used to record 
    past or future participations.
        
    Should not be used in place of more permanent relationships between demographic entities.
    """
    
    implements(IParticipation)
    
    def __init_(self,performer,function,mode,time,**kwargs):
        self.performer=performer
        self.function=function
        self.mode=mode
        self.time=time
        Field.__init__(self,**kwargs)
     
   
    def performerValid():
        u"""performer != None"""
        
    def functionValid():
        u"""function != None and then function.generating_type.is_equal(“DV_CODED_TEXT”) 
        implies terminology(Terminology_id_openehr).has_code_for_group_id(Group_id_participation_function, 
        function.defining_code)"""
        
    def modeValid(): 
        u"""mode != None and terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_participation_mode, mode.defining_code)"""
        
        
class AuditDetails(Field):
    u"""
    The set of attributes required to document the committal of an information 
    item to a repository.
    """
    
    implements(IAuditDetails)
    
    def __init__(self,systemId,committer,tcommitted,chgtype,descr,**kwargs):
        self.systemId=systemId
        self.committer=committer
        self.timeCommitted=tcommitted
        self.changeType=chgtype
        self.description=descr
        Field.__init__(self,**kwargs)
      
    def systemIdValid():
        u"""systemId != None and systemId != '' """
        
    def committerValid():
        u"""committer!= None"""
        
    def timeCommittedValid():
        u"""timeCommitted != None"""
    
    def changeTypeValid():
        u"""changeType != None and then terminology(Terminology_id_openehr).
        has_code_for_group_id(Group_id_audit_change_type, change_type.defining_code)"""



class Attestation(AuditDetails):
    u"""
    Record an attestation of a party (the committer) to item(s) of record content. 
    The type of attestation is
    """
    
    implements(IAttestation)
    
    def __init__(self,aview,proof,items,reason,ispend,**kwargs):
        self.attestedView=aview
        self.proof=proof
        self.items=items
        self.reason=reason
        self.isPending=ispend
        Field.__init__(self,**kwargs)
    
    def itemsValid():
        u"""items != None items != '' """
        
    def reasonValid():
        u"""reason != None and then(reason.generating_type.is_equal(“DV_CODED_TEXT”) 
        implies terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_attestation_reason, reason.defining_code))"""
        
        
class RevisionHistory(Field):
    u"""
    Defines the notion of a revision history of audit items, each associated 
    with the version for which that audit was committed. The list is in 
    most-recent-first order.
    """

    implements(IRevisionHistory)
    
    def __init__(self,items,**kwargs):
        self.items=items
        Field.__init__(self,**kwargs)

    def mostRecentVersion():
        u"""The version id of the most recent item, as a String. 
        Ensure Result.is_equal(items.last.version_id.value)"""
        
    def mostRecentVersionTimeCommitted():
         u"""The commit date/time of the most recent item, as a string.
         Ensure Result.is_equal(items.last.audits.first.time_committed.value)"""
         
    def itemsValid():
        u"""items != None """
        

class RevisionHistoryItem(Field):
    u"""
    An entry in a revision history, corresponding to a version from a versioned 
    container. Consists of AUDIT_DETAILS instances with revision identifier of 
    the revision to which the AUDIT_DETAILS intance belongs.
    """
    
    implements(IRevisionHistoryItem)
    
    def __init__(self,audits,verid,**kwargs):
        self.audits=audits
        self.versionId=verid
        Field.__init__(self,**kwargs)

   
    def auditValid():
        u"""audits != None and audits != ' """

    def versionIdValid():
        u"""versionId != None"""
        