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

from partyproxy import PartyProxy
from interfaces.partyidentified import IPartyIdentified

_ = MessageFactory('oship')

   
class PartyIdentified(PartyProxy):
    u"""
    Proxy data for an identified party other than the subject of the record, 
    minimally consisting of human-readable identifier(s), such as name, formal 
    (and possibly computable) identifiers such as NHS number, and an optional 
    link to external data. There must be at least one of name, identifier or 
    external_ref present.
        
    Used to describe parties where only identifiers may be known, and there is 
    no entry at all in the demographic system (or even no demographic system). 
    Typically for health care providers, e.g. name and provider number of an 
    institution.

    Should not be used to include patient identifying information.
    """
    
    implements(IPartyIdentified)
    
    def __init__(self,name,idents):
        self.name=name
        self.identifiers=idents
        
    def basicValid(obj):
        u"""name None or identifiers != None or external_ref != None"""            
        
    def nameValid():
        u"""name != None and name != '' """
        
    def identifiersValid():
        u"""identifiers != none and identifiers != '' """
