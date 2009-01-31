# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementations for specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Andre Goncalves <goncalves.aluiz@gmail.com>'


from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from interfaces.entry import IEntry
from oship.openehr.rm.ehr.composition.content.contentitem import ContentItem
from oship.openehr.rm.common.generic.partyproxy import PartyProxy

_ = MessageFactory('oship')


class Entry(ContentItem):
    """
    The abstract parent of all ENTRY subtypes. An ENTRY is the root of a logical item
    of "hard" clinical information created in the "clinical statement" context, within a
    clinical session. There can be numerous such contexts in a clinical session. Obser-
    vations and other Entry types only ever document information captured/created in
    the event documented by the enclosing Composition.
    An ENTRY is also the minimal unit of information any query should return, since a
    whole ENTRY (including subparts) records spatial structure, timing information,
    and contextual information, as well as the subject and generator of the informa-
    tion.   
    """

    implements(IEntry)
    
    def __init__(self,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        ContentItem.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
        self.language=lang
        self.encoding=encod
        self.subject=subject
        self.provider=provider
        self.otherParticipations=opart
        self.workflowId=wfid    
    
    def subectIsSelf():
        u"""Returns True if this Entry is about the subject of the EHR, in which case the 
        subject attribute is of type PARTY_SELF. """
        return (isinstance(subject, PartyProxy))
    
 