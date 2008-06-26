# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
These are the interfaces for the am.archetype.primitive package defined in 
The Archetype Object model Rev 2.0.2
"""
__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema import Time
from zope.i18nmessageid.message import MessageFactory

from openehr.am.archetype.validitykind import ValidityKind
from openehr.rm.support.interval import Interval
from cprimitive import ICPrimitive

_ = MessageFactory('oship')

class ICTime(ICPrimitive):
    """
    ISO 8601 compatible constraint on instances of Time.
    """
    
    minuteValidity=ValidityKind(
        title_("Minute Validity"),
        description=_(" "),
        required=False,
    )
    

    secondValidity=ValidityKind(
        title_("Second Validity"),
        description=_(" "),
        required=False,
    )
    
    millisecondValidity=ValidityKind(
        title_("Millisecond Validity"),
        description=_(" "),
        required=False,
    )
    
    timezoneValidity=ValidityKind(
        title_("Timezone Validity"),
        description=_(" "),
        required=False,
    )
    
    range=Interval(
        title_("Range"),
        description=_("Interval of times."),
        required=False,
    )

    assumedValue=Time(
        title_("Assumed Value"),
        description=_(" "),
        required=True,
    )

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """
