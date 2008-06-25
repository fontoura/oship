# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the composition package from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.schema import Bool,List

from openehr.rm.common.generic.partyproxy import PartyProxy
from openehr.rm.datatypes.text.dvcodedtext import DvCodedText
from openehr.rm.datatypes.text.codephrase import CodePhrase
from composition.eventcontext import EventContext
from openehr.rm.common.archetyped.interfaces.locatable import ILocatable

_ = MessageFactory('oship')

class IComposition(ILocatable):
    """
    One version in a VersionedComposition.  A compsoition is considerred the unit of modification in an EHR.
    """
    
    content=List(
        title=_("Content"),
        description=_("Content of this composition."),
        required=False,
    )
    
    context=EventContext(
        title=_("Context"),
        description=_("The clinical session context."),
        required=False,
    )
    
    composer=PartyProxy(
        title=_("Composer"),
        description=_("The party responsible for the content. It may not be the actual person entering the data."),
        required=True,
    )
    
    category=DvCodedText(
        title=_("Category"),
        description=_("Defines the broad category of this composition."),
        required=True,
    )
    
    language=CodePhrase(
        title=_("Language"),
        description=_("Indicator of the localised language where this composition was created."),
        required=True,
    )
    
    territory=CodePhrase(
        title=_("Territory"),
        description=_("Territory where this composition was written. ISO 3166."),
        required=True,
    )
    
    isPersistent=Bool(
        title=_("Persistent"),
        description=_("Used to locate items that are of interest to most users."),
        required=True,
        default=True,
    )
