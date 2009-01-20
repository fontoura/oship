# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from objectref import ObjectRef
from interfaces.partyref import IPartyRef

_ = MessageFactory('oship')
      
class PartyRef(ObjectRef):
    u"""
    Identifier for parties in a demographic or identity service. There are typically a
    number of subtypes of the PARTY class, including PERSON, ORGANISATION, etc.
        
    Abstract supertypes are allowed if the referenced object is of a type not known by
    the current implementation of this class (in other words, if the demographic model
    is changed by the addition of a new PARTY or ACTOR subtypes, valid
    PartyRefs can still be constructed to them).
    """

    implements(IPartyRef)
    
    def __init__(self,id,nameSpace,type):
        self.id=id
        self.nameSpace=nameSpace
        self.type=type     
        
    def validateType(self):
        u"""
        type is in ["PERSON","ORGANISATION","GROUP","AGENT","ROLE","PARTY","ACTOR"]
        """
        return self.type in ['PERSON','ORGANISATION','GROUP','AGENT','ROLE','PARTY','ACTOR']
        
