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
from zope.schema import TextLine

from openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from openehr.rm.datatypes.encapsulated.dvparsable import DvParasable


_ = MessageFactory('oship')

class IActivity(ILocatable):
    """
    A single activity within an instruction.
    """
    
    description=ItemStructure(
        title=_("Description"),
        description=_("Description of the activity."),
        required=True,
    )
    
    timing=DvParsable(
        title=_("Timing"),
        description=_("Timing of the activity in a format such as ISO8601."),
        required=True,
    )
    
    actionArchetypeId=TextLine(
        title=_("Action ArchetypeId"),
        description=_("re pattern enclosed in '//' delimiters."),
        required=True,
        default="/.*/",
    )
   