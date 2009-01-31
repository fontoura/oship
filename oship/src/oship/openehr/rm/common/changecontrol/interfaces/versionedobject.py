# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the change_control package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
 
from zope.i18nmessageid import MessageFactory
from zope.schema import Field,TextLine,Object
from zope.schema.interfaces import IContainer

from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef
from oship.openehr.rm.support.identification.interfaces.hierobjectid import IHierObjectId
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime


_ = MessageFactory('oship')

class IVersionedObject(IContainer):
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
        required=True,
        )
    
    ownerId = Object(
        schema=IObjectRef,
        title=_(u'Owner Id'),
        description=_(u"""Reference to object to which this version container 
                    belongs, e.g. the id of the containing EHR or other 
                    relevant owning entity."""),
        required=True,
        )
    
    timeCreated = Object(
        schema=IDvDateTime,
        title=_(u'Time Created'),
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
