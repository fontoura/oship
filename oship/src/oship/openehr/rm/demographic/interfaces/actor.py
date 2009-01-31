# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

From the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__Contributors__ = u'Roberto Cunha <roliveiracunha@yahoo.com.br>'

from zope.schema import Set,List,TextLine,Object
from zope.i18nmessageid import MessageFactory
from oship.openehr.rm.datatypes.text.interfaces.dvtext import IDvText
from oship.openehr.rm.support.identification.interfaces.partyref import IPartyRef

from oship.openehr.rm.demographic.interfaces.party import IParty

_ = MessageFactory('oship')

class IActor(IParty):
    """
    Ancestor of all real world types.
    """
    
    roles=Set(
        title=_(u"Roles"),
        description=_(u"Identifiers of the Version container for each Role played by this party."),
        required=False,
        value_type = Object(schema = IPartyRef)
    )
    
    languages=List(
        title=_(u"Languages"),
        description=_(u"A list of languages to be used to communicate with this actor."),
        required=False,
        value_type = Object(schema = IDvText)
    )
    def hasLegalIdentity():
        """
        Return True/False regarding a legal identiry of this Actor.
        """

  