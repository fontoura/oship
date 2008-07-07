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
from zope.schema import List,TextLine,Object

from openehr.rm.common.generic.interfaces.partyidentified import IPartyIdentified
from openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime
from openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText
from openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from openehr.rm.common.archetyped.interfaces.pathable import IPathable

_ = MessageFactory('oship')
    
class IEventContext(IPathable):
    """
    The context information of a healthcare event.
    These include patient contacts or other investigations.
    """
    
    healthCareFacility=Object(
        schema=IPartyIdentified,
        title=_(u"Healthcare Facility"),
        description=_(u"Where this event took place."),
        required=False,
    )
    
    startTime=Object(
        schema=IDvDateTime,
        title=_(u"Start Time"),
        description=_(u"Start Time"),
        required=True,
    )
    
    endTime=Object(
        schema=IDvDateTime,
        title=_(u"End Time"),
        description=_(u"End Time"),
        required=False,
    )
    
    participations=List(
        title=_(u"Participations"),
        description=_(u"List of all parties involved in the event."),
        required=False,
    )
    
    location=TextLine(
        title=_(u"Location"),
        description=_(u"Physical location of this event; ABCLab, home,etc."),
        required=False,
    )
    
    setting=Object(
        schema=IDvCodedText,
        title=_(u"Setting"),
        description=_(u"The setting of the clinical event."),
        required=True,
    )
    
    otherContext=Object(
        schema=IItemStructure,
        title=_(u"Other Context"),
        description=_(u"Other optional archetyped context."),
        required=False,
    )
    
    