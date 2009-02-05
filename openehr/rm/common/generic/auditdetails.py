# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the generic package as described in the 
Common Information Model Rev. 2.1.0 

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.generic.interfaces.auditdetails import IAuditDetails

_ = MessageFactory('oship')

class AuditDetails(object):
    u"""
    The set of attributes required to document the committal of an information 
    item to a repository.
    """
    
    implements(IAuditDetails)
    
    
    def __init__(self,systemId,committer,tcommitted,chgtype,descr):
        self.systemId=systemId
        self.committer=committer
        self.timeCommitted=tcommitted
        self.changeType=chgtype
        self.description=descr
      
    def systemIdValid():
        u"""systemId != None and systemId != '' """
        
    def committerValid():
        u"""committer!= None"""
        
    def timeCommittedValid():
        u"""timeCommitted != None"""
    
    def changeTypeValid():
        u"""changeType != None and then terminology(Terminology_id_openehr).
        has_code_for_group_id(Group_id_audit_change_type, change_type.defining_code)"""


