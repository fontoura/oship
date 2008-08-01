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
from zope.i18nmessageid import MessageFactory

from interfaces.attestation import IAttestation

_ = MessageFactory('oship')


class Attestation(AuditDetails):
    u"""
    Record an attestation of a party (the committer) to item(s) of record content. 
    The type of attestation is
    """
    
    implements(IAttestation)
    
    
    def __init__(self,aview,proof,items,reason,ispend):
        self.attestedView=aview
        self.proof=proof
        self.items=items
        self.reason=reason
        self.isPending=ispend
   
    def itemsValid():
        u"""items != None items != '' """
        
    def reasonValid():
        u"""reason != None and then(reason.generating_type.is_equal("DV_CODED_TEXT") 
        implies terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_attestation_reason, reason.defining_code))"""
        
