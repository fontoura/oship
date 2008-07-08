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

from zope.interface import implements,classProvides
from zope.i18nmessageid import MessageFactory

#from openehr.rm.common.archetyped.locatable import Locatable
from interfaces.partyproxy import IPartyProxy
from openehr.rm.common.archetyped.interfaces.locatable import ILocatable

_ = MessageFactory('oship')


class PartyProxy(object):
    u"""
    Abstract concept of a proxy description of a party, including an optional 
    link to data for this party in a demographic or other identity management 
    system. Subtyped into PARTY_IDENTIFIED and PARTY_SELF.
    """
    
    implements(IPartyProxy,ILocatable)
    classProvides(IPartyProxy)
    
    def __init__(self,extref):
        self.externalRef=extref
        
