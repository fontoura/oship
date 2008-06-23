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

from zope.interface import Interface
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.text.dvtext import DvText
from openehr.rm.datatypes.quantity.datetm.dvdatetime import DvDateTime
from openehr.rm.datatypes.text.dvcodedtext import DvCodedText
from openehr.rm.common.generic.partyproxy import PartyProxy

_ = MessageFactory('oship')

        
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

