# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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
from zope.schema import Object
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.generic.partyidentified import IPartyIdentified
from oship.openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText

_ = MessageFactory('oship')

        
class IPartyRelated(IPartyIdentified):
    u"""
    Proxy type for identifying a party and its relationship to the subject of 
    the record.

    Use where the relationship between the party and the subject of the record 
    must be known.
    """

    relationship = Object(
        schema=IDvCodedText,
        title=_(u'Relationship'),
        description=_(u"""Relationship of subject of this ENTRY to the subject
                    of the record. May be coded. If it is the patient, coded 
                    as "self"."""),
        required=True,
        )
    
    def relationshipValid():
        u"""relationship != None and relationship in the relationship 
        vocabulary."""
