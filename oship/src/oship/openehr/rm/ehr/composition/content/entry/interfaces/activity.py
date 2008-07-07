# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

The interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import TextLine,Object,Field
from zope.interface import Attribute

from openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from openehr.rm.datatypes.encapsulated.dvparsable import DvParsable


_ = MessageFactory('oship')

class IActivity(ILocatable):
    """
    A single activity within an instruction.
    """
    
    
    description=Object(
        schema=IItemStructure,
        title=_(u"Description"),
        description=_(u"Description of the activity."),
        required=True,
    )
    
    
    timing=DvParsable(0,'','',
        title=_(u"Timing"),
        description=_(u"Timing of the activity in a format such as ISO8601."),
        required=True,
    )
    
    actionArchetypeId=TextLine(
        title=_(u"Action ArchetypeId"),
        description=_(u"re pattern enclosed in '//' delimiters."),
        required=True,
        default=u"/.*/",
    )
   