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
from zope.schema import List,TextLine

from openehr.rm.common.generic.partyidentified import PartyIdentified
from openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime
from openehr.rm.datatypes.text.dvcodedtext import DvCodedText
from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from openehr.rm.common.archetyped.interfaces.pathable import IPathable

_ = MessageFactory('oship')
    
class IEventContext(IPathable):
    """
    The context information of a healthcare event.
    These include patient contacts or other investigations.
    """
    
    healthCareFacility=PartyIdentified(
        title=_("Healthcare Facility"),
        description=_("Where this event took place."),
        required=False,
    )
    
    startTime=DvDateTime(
        title=_("Start Time"),
        description=_(" "),
        required=True,
    )
    
    endTime=DvDateTime(
        title=_("End Time"),
        description=_(" "),
        required=False,
    )
    
    participations=List(
        title=_("Participations"),
        description=_("List of all parties involved in the event."),
        required=False,
    )
    
    location=TextLine(
        title=_("Location"),
        description=_("Physical location of this event; ABCLab, home,etc."),
        required=False,
    )
    
    setting=DvCodedText(
        title=_("Setting"),
        description=_("The setting of the clinical event."),
        required=True,
    )
    
    otherContext=ItemStructure(
        title=_("Other Context"),
        description=_("Other optional archetyped context."),
        required=False,
    )
    
    