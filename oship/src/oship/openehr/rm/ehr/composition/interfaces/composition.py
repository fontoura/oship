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
__contributors__ = u'Renato Pesca <rpesca@gmail.com>'

from zope.i18nmessageid import MessageFactory
from zope.schema import Bool,List,Object

from oship.openehr.rm.common.generic.interfaces.partyproxy import IPartyProxy
from oship.openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText
from oship.openehr.rm.datatypes.text.interfaces.codephrase import ICodePhrase
from oship.openehr.rm.ehr.composition.interfaces.eventcontext import IEventContext
from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable

from oship.openehr.rm.ehr.composition.interfaces.contentitem import IContentItem

_ = MessageFactory('oship')

class IComposition(ILocatable):
    """
    One version in a VersionedComposition.  A compsoition is considerred the unit of modification in an EHR.
    """
    
    content=List(
        title=_(u"Content"),
        description=_(u"Content of this composition."),
	value_type=Object(schema=IContentItem),
        required=False,
    )
    
    context=Object(
        schema=IEventContext,
        title=_(u"Context"),
        description=_(u"The clinical session context."),
        required=False,
    )
    
    composer=Object(
        schema=IPartyProxy,
        title=_(u"Composer"),
        description=_(u"The party responsible for the content. It may not be the actual person entering the data."),
        required=True,
    )
    
    category=Object(
        schema=IDvCodedText,
        title=_(u"Category"),
        description=_(u"Defines the broad category of this composition."),
        required=True,
    )
    
    language=Object(
        schema=ICodePhrase,
        title=_(u"Language"),
        description=_(u"Indicator of the localised language where this composition was created."),
        required=True,
    )
    
    territory=Object(
        schema=ICodePhrase,
        title=_(u"Territory"),
        description=_(u"Territory where this composition was written. ISO 3166."),
        required=True,
    )
    
    isPersistent=Bool(
        title=_(u"Persistent"),
        description=_(u"Used to locate items that are of interest to most users."),
        required=True,
        default=True,
    )
