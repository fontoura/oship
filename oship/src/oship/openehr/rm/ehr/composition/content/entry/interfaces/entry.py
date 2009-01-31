# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

The interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = u'Renato Pesca <rpesca@gmail.com>'


from zope.i18nmessageid import MessageFactory
from zope.schema import List,Object

from oship.openehr.rm.common.generic.interfaces.partyproxy import IPartyProxy
from oship.openehr.rm.datatypes.text.interfaces.codephrase import ICodePhrase
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef
from oship.openehr.rm.ehr.composition.content.interfaces.contentitem import IContentItem

from oship.openehr.rm.common.generic.interfaces.participation import IParticipation

_ = MessageFactory('oship')


class IEntry(IContentItem):
    u"""
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

    language = Object(
        schema=ICodePhrase,
        title = _(u"language"),
        description = _(u"""Mandatory indicator of the localised language in which this Entry 
                      is written. Coded from openEHR Code Set "languages"."""),
        required = True
        )
    
    encoding = Object(
        schema=ICodePhrase,
        title = _(u"encoding"),
        description = _(u"""Name of character set in which text values in this Entry are encoded. 
                      Coded from openEHR Code Set "character sets"."""),
        required = True
        )

        
    subject = Object(
        schema=IPartyProxy,
        title = _(u"subject"),
        description = _(u"""Id of human subject of this ENTRY, e.g.
                           organ donor, foetus, a family member
                           another clinically relevant person."""),
        required = True
        )
    
    provider = Object(
        schema=IPartyProxy,
        title = _(u"provider"),
        description = _(u"""Optional identification of provider of the informatoin in this ENTRY, which might be:
                        the patient
                        a patient agent, e.g. parent, guardian
                        the clinician
                        a device or software
                       Generally only used when the recorder needs to make it explicit. Otherwise, Composition
                       composer and other participants are assumed. """),
        required = False
        )
    
    otherParticipations = List(
        title = _(u"otherParticipations"),
        description = _(u"""Other participations at ENTRY level."""),
	value_type=Object(schema=IParticipation),
        required = False
        )
    
    workflowId = Object(
        schema=IObjectRef,
        title = _(u"workflowId"),
        description = _(u"""Identifier of externally held workflow engine data for this 
                      workflow execution, for this subject of care."""),
        required = False
        )
    
    
    def subectIsSelf():
        u"""Returns True if this Entry is about the subject of the EHR, in which case the 
        subject attribute is of type PARTY_SELF. """
    
   
