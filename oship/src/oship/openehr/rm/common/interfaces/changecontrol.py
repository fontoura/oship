# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

These are the interfaces for the change_control package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.app.container.interfaces import IContainer

from zope.schema import Field
from zope.schema import Text
from zope.schema import TextLine
from zope.schema import List

from zope.i18nmessageid import MessageFactory

from openehr.rm.support.identification import HierObjectId
from openehr.rm.support.identification import ObjectRef,ObjectVersionId
from openehr.rm.datatypes.datetm import DvDateTime
from openehr.rm.datatypes.text import DvCodedText

_ = MessageFactory('oship')


class IVersionedObject(IContainer):
    u"""
    Version control abstraction, defining semantics for versioning one 
    complex object.
    """
    
    uid = HierObjectId('',
        title=_(u"""UID"""),
        description=_(u"""Unique identifier of this version container. This id 
                    will be the same in all instances of the same container 
                    in a distributed environment, meaning that it can be 
                    understood as the uid of the “virtual version tree”."""),
        required=True,
        )
    
    ownerId = ObjectRef('','','',
        title=_(u"""Owner Id"""),
        description=_(u"""Reference to object to which this version container 
                    belongs, e.g. the id of the containing EHR or other 
                    relevant owning entity."""),
        required=True,
        )
    
    timeCreated = DvDateTime('',
        title=_(u"""Time Created"""),
        description=_(u"""Time of initial creation of this versioned object."""),
        required=True,
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
        
class IVersion(Interface):
    u"""
    Abstract model of one Version within a Version container, containing 
    data, commit audit trail, and the identifier of its Contribution.
    """

    
    
    uid = ObjectVersionId('',
        title=_(u"""UID"""),
        description=_(u"""Unique identifier of this version, containing
                    owner_id, version_tree_id and creating_system_id.
                    Type == OBJECT_VERSION_ID"""),
        required=True,
        )
    
    precedingVersionId = ObjectVersionId('',
        title=_(u"""Preceding Version Id"""),
        description=_(u"""Unique identifier of the version of which this version 
                    is a modification; Void if this is the first version.
                    Type == OBJECT_VERSION_ID"""),
        required=False,
        )
    
    data = Field(
        title=_(u"""Data"""),
        description=_(u"""Original content of this Version."""),
        required=False,
        )
    
    lifecycleState = DvCodedText('',
        title=_(u"""Lifecycle State"""),
        description=_(u"""Lifecycle state of this version; coded by openEHR 
                    vocabulary “version lifecycle state”. 
                    Type == DV_CODED_TEXT"""),
        required=True,
        )
    
    
    commitAudit = AuditDetails(
        title=_(u"""Commit Audit"""),
        description=_(u"""Audit trail corresponding to the committal of this
                    version to the VERSIONED_OBJECT. Type == AUDIT_DETAILS"""),
        required=True,
        )
    
    contribution = ObjectRef(
        title=_(u"""Contribution"""),
        description=_(u"""Contribution in which this version was added."""),
        required=True,
        )
    
    signature = TextLine(
        title=_(u"""Signature"""),
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
        
"""       Contribution_valid: contribution /= Void and contribution.type.is_equal(“CON-
          TRIBUTION”)
          Preceding_version_uid_validity: uid.version_tree_id.is_first xor
          preceding_version_uid /= Void
          Lifecycle_state_valid: lifecycle_state /= Void and then
          terminology(Term_id_openehr).
          has_code_for_group_id(Group_id_version_lifecycle_state,
          lifecycle_state.defining_code)

"""
