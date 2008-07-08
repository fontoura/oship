# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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
from zope.interface import implements,classProvides
from zope.schema import Field

from interfaces.version import IVersion

_ = MessageFactory('oship')

        
class Version(object):
    u"""
    Abstract model of one Version within a Version container, containing 
    data, commit audit trail, and the identifier of its Contribution.
    """

    implements(IVersion)
    classProvides(IVersion)
    
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
