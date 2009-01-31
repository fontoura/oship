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
 
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
from zope.schema import Field,TextLine,Object

from oship.openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText
from oship.openehr.rm.support.identification.interfaces.objectversionid import IObjectVersionId
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef
from oship.openehr.rm.common.generic.interfaces.auditdetails import IAuditDetails

_ = MessageFactory('oship')

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
        required=True,
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
        required=True,
        )
    
    
    commitAudit = Object(
        schema=IAuditDetails,
        title=_(u'Commit Audit'),
        description=_(u"""Audit trail corresponding to the committal of this
                    version to the VERSIONED_OBJECT. Type == AUDIT_DETAILS"""),
        required=True,
        )
    
    contribution = Object(
        schema=IObjectRef,
        title=_(u'Contribution'),
        description=_(u"""Contribution in which this version was added."""),
        required=True,
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
