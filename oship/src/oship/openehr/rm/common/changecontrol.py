# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

Implementations for the change_control package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.app.container.btree import *
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.interfaces.changecontrol import *

_ = MessageFactory('oship')


class VersionedObject(Container):
    u"""
    Version control abstraction, defining semantics for versioning one 
    complex object.
    """
    
    implements(IVersionedObject)
    
    def __init__(self,uid,ownerId,timeCreated):
        self.uid=uid
        self.ownerId=ownerId
        self.timeCreated=timeCreated
        Field.__init__(self,**kwargs)
    
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
        
class Version(Field):
    u"""
    Abstract model of one Version within a Version container, containing 
    data, commit audit trail, and the identifier of its Contribution.
    """

    implements(IVersion)
    
    def __init__(self,uid,preVid,data,lcstate,caudit,contr,sig,**kwargs):
        self.uid=uid
        self.precedingVersionId=preVid
        self.data=data
        self.lifecycleState=lcstate
        self.commitAudit=caudit
        self.signature=sig
        Field.__init__(self,**kwargs) 
                        
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
        
"""       Contribution_valid: contribution /= Void and contribution.type.is_equal(“CON-
          TRIBUTION”)
          Preceding_version_uid_validity: uid.version_tree_id.is_first xor
          preceding_version_uid /= Void
          Lifecycle_state_valid: lifecycle_state /= Void and then
          terminology(Term_id_openehr).
          has_code_for_group_id(Group_id_version_lifecycle_state,
          lifecycle_state.defining_code)

"""
