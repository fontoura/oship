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

from zope.i18nmessageid import MessageFactory
from zope.schema import Object

from zope.interface import Interface
from oship.openehr.rm.support.identification.interfaces.partyref import IPartyRef

_ = MessageFactory('oship')


class IPartyProxy(Interface):
    u"""
    Abstract concept of a proxy description of a party, including an optional 
    link to data for this party in a demographic or other identity management 
    system. Subtyped into PARTY_IDENTIFIED and PARTY_SELF.
    """
    
    externalRef = Object(
        schema=IPartyRef,
        title=_(u"External Reference"),
        description=_(u"""Optional reference to more detailed demographic or 
                    identification information for this party, in an external 
                    system. Type == PartyRef."""),
        required=False,
        )

    