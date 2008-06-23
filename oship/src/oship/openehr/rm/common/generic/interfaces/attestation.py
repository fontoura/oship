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

from zope.schema import TextLine,Set,Bool
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.encapsulated.dvmultimedia import DvMultimedia
from openehr.rm.datatypes.text.dvtext import DvText

_ = MessageFactory('oship')


class IAttestation(IAuditDetails):
    u"""
    Record an attestation of a party (the committer) to item(s) of record content. 
    The type of attestation is
    """
    
    attestedView = DvMultimedia(
        title=_(u'Attested View'),
        description=_(u"""Optional visual representation of content attested e.g. 
                    screen image. Type==DvMultimedia"""),
        required=False,
        )
    
    proof = TextLine(
        title=_(u'Proof'),
        description=_(u"""Proof of attestation."""),
        required=False,
        )
    
    items = Set(
        title=_(u'Items'),
        description=_(u"""Items attested, expressed as fully qualified runtime 
                    paths to the items in question. Although not recommended, 
                    these may include fine-grained items which have been 
                    attested in some other system. Otherwise it is assumed to
                    be for the entire VERSION with which it is associated. 
                    Set <DV_EHR_URI>"""),
        required=False,
        )
 
    
    reason = DvText(
        title=_(u'Reason'),
        description=_(u"""Reason of this attestation. Optionally coded by the 
                    openEHR Terminology group “attestation reason”; includes 
                    values like “authorisation”, “witness” etc."""),
        required=True,
        )
    
    isPending = Bool(
        title=_(u'Pending?'),
        description=_(u"""True if this attestation is outstanding; 
                    False means it has been completed."""),
        required=True,
        )
    
    def itemsValid():
        u"""items != None items != '' """
        
    def reasonValid():
        u"""reason != None and then(reason.generating_type.is_equal(“DV_CODED_TEXT”) 
        implies terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_attestation_reason, reason.defining_code))"""
        
