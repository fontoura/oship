# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import Set,Object

from openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from openehr.rm.support.identification.interfaces.hierobjectid import IHierObjectId
from openehr.rm.datatypes.text.interfaces.codephrase import ICodePhrase
from openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText
from openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure

_ = MessageFactory('oship')

class IParty(ILocatable):
    """
    Ancestor of all party types.
    """
    
    uid=Object(
        schema=IHeirObjectId,
        title=_(u"UID"),
        description=_(u"Identifier of this party."),
        required=True,
    )
    
    identities=Set(
        title=_(u"Indentities"),
        description=_(u"Identities used by the party to identify itself."),
        required=True,
    )
    
    contacts=Set(
        title=_(u"Contacts"),
        description=_(u"Contacts for this party."),
        required=True,
    )
    
    category=Object(
        schema=IDvCodedText,
        title=_(u"Category"),
        description=_(u"Defines the broad category of this composition."),
        required=False,
    )
    
    language=Object(
        schema=ICodePhrase,
        title=_(u"Language"),
        description=_(u"Indicator of the localised language where this composition was created."),
        required=True,
    )
    
    relationships=Set(
        title=_(u"Relationships"),
        description=_(u"Relationships in which this role takes part as target."),
        required=False,
    )
    
    details=Object(
        schema=IItemStructure,
        title=_(u"Details"),
        description=_(u"All other party details."),
        required=False,
    )
    
    def type():
        """
        Return the type of party from the inherited 'name' attribute.
        """
