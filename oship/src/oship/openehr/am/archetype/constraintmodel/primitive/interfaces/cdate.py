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

from zope.schema import Date

from openehr.rm.support.interval import Interval
from openehr.am.archetype.validitykind import ValidityKind
from cprimitive import ICPrimitive

class ICDate(ICPrimitive):
    """
    ISO 8601 compatible constraint on instances of Date.
    """
    
    monthValidity=ValidityKind(
        title_("Month Validity"),
        description=_(" "),
        required=False,
    )
    

    dayValidity=ValidityKind(
        title_("Day Validity"),
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
        description=_("Interval of dates."),
        required=False,
    )

    assumedValue=Date(
        title_("Assumed Value"),
        description=_(" "),
        default=Date(),
        required=True,
    )

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """

