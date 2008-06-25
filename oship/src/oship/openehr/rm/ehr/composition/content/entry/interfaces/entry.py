# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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


from zope.i18nmessageid import MessageFactory
from zope.schema import List

from openehr.rm.common.generic.partyproxy import PartyProxy
from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.rm.support.identification.objectref import ObjectRef

_ = MessageFactory('oship')


class IEntry(IContentItem):
    u"""
        The abstract parent of all ENTRY subtypes. An ENTRY is the root of a logical item
        of “hard” clinical information created in the “clinical statement” context, within a
        clinical session. There can be numerous such contexts in a clinical session. Obser-
        vations and other Entry types only ever document information captured/created in
        the event documented by the enclosing Composition.
        An ENTRY is also the minimal unit of information any query should return, since a
        whole ENTRY (including subparts) records spatial structure, timing information,
        and contextual information, as well as the subject and generator of the informa-
        tion.

    """

    language = CodePhrase(
        title = u"""language""",
        description = u"""Mandatory indicator of the localised language in which this Entry 
                      is written. Coded from openEHR Code Set “languages”.""",
        required = True
        )
    
    encoding = CodePhrase(
        title = u"""encoding""",
        description = u"""Name of character set in which text values in this Entry are encoded. 
                      Coded from openEHR Code Set “character sets”.""",
        required = True
        )

        
    subject = PartyProxy(
        title = u"""subject""",
        description = u"""Id of human subject of this ENTRY, e.g.
                          • organ donor
                          • foetus
                          • a family member
                          • another clinically relevant person.""",
        required = True
        )
    
    provider = PartyProxy(
        title = u"""provider""",
        description = u"""Optional identification of provider of the informatoin in this ENTRY, which might be:
                       • the patient
                       • a patient agent, e.g. parent, guardian
                       • the clinician
                       • a device or software
                       Generally only used when the recorder needs to make it explicit. Otherwise, Composition
                       composer and other participants are assumed. """,
        required = False
        )
    
    otherParticipations = List(
        title = u"""otherParticipations""",
        description = u"""Other participations at ENTRY level.""",
        required = False
        )
    
    workflowId = ObjectRef(
        title = u"""workflowId""",
        description = u"""Identifier of externally held workflow engine data for this 
                      workflow execution, for this subject of care.""",
        required = False
        )
    
    
    def subectIsSelf():
        u"""Returns True if this Entry is about the subject of the EHR, in which case the 
        subject attribute is of type PARTY_SELF. """
    
   
