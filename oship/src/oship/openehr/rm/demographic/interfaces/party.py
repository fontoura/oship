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

_ = MessageFactory('oship')

class IParty(ILocatable):
    """
    Ancestor of all party types.
    """
    
    uid=HierObjectId(
        title=_("UID"),
        description=_("Identifier of this party."),
        required=True,
    )
    
    identities=Set(
        title=_("Indentities"),
        description=_("Identities used by the party to identify itself."),
        required=True,
    )
    
    contacts=Set(
        title=_("Contacts"),
        description=_("Contacts for this party."),
        required=True,
    )
    
    category=DvCodedText(
        title=_("Category"),
        description=_("Defines the broad category of this composition."),
        required=False,
    )
    
    language=CodePhrase(
        title=_("Language"),
        description=_("Indicator of the localised language where this composition was created."),
        required=True,
    )
    
    relationships=Set(
        title=_("Relationships"),
        description=_("Relationships in which this role takes part as target."),
        required=False,
    )
    
    details=ItemStructure(
        title=_("Details"),
        description=_("All other party details."),
        required=False,
    )
    
    def type():
        """
        Return the type of party from the inherited 'name' attribute.
        """

class Party(Locatable):
    """
    Ancestor of all party types.
    """
    
    uid=HierObjectId(
        title=_("UID"),
        description=_("Identifier of this party."),
        required=True,
    )
    
    identities=Set(
        title=_("Indentities"),
        description=_("Identities used by the party to identify itself."),
        required=True,
    )
    
    contacts=Set(
        title=_("Contacts"),
        description=_("Contacts for this party."),
        required=True,
    )
    
    category=DvCodedText(
        title=_("Category"),
        description=_("Defines the broad category of this composition."),
        required=False,
    )
    
    language=CodePhrase(
        title=_("Language"),
        description=_("Indicator of the localised language where this composition was created."),
        required=True,
    )
    
    relationships=Set(
        title=_("Relationships"),
        description=_("Relationships in which this role takes part as target."),
        required=False,
    )
    
    details=ItemStructure(
        title=_("Details"),
        description=_("All other party details."),
        required=False,
    )
    
    def type():
        """
        Return the type of party from the inherited 'name' attribute.
        """
        