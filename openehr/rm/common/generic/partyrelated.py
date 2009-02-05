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

from oship.openehr.rm.common.generic.partyidentified import PartyIdentified
from interfaces.partyrelated import IPartyRelated

_ = MessageFactory('oship')

       
class PartyRelated(PartyIdentified):
    u"""
    Proxy type for identifying a party and its relationship to the subject of 
    the record.
    
    Use where the relationship between the party and the subject of the record 
    must be known.
    """
    
    implements(IPartyRelated)
    
    def __init__(self,relationship):
        self.relationship=relationship
        
    
    def relationshipValid():
        u"""relationship != None and relationship in the relationship 
        vocabulary."""