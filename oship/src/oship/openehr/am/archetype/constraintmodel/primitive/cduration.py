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

from zope.interface import Interface
from zope.schema import *

class ICDuration(ICPrimitive):
    """
    Constraints on durations.  openEHR allows the 'W' indicator to be mixed in.
    """
    
    yearsAllowed=Bool(
        title_("Years Allowed"),
        description=_("True if years are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    monthsAllowed=Bool(
        title_("Months Allowed"),
        description=_("True if months are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    weeksAllowed=Bool(
        title_("Weeks Allowed"),
        description=_("True if weeks are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    daysAllowed=Bool(
        title_("Days Allowed"),
        description=_("True if days are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    hoursAllowed=Bool(
        title_("Hours Allowed"),
        description=_("True if hours are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    minutesAllowed=Bool(
        title_("Minutes Allowed"),
        description=_("True if minutes are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    secondsAllowed=Bool(
        title_("Seconds Allowed"),
        description=_("True if seconds are allowed in the constrained duration."),
        required=False,
        default=True,
    )
    
    fractionalSecondsAllowed=Bool(
        title_("Fractional Seconds Allowed"),
        description=_("True if fractional seconds are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    range=Interval(
        title_("Range"),
        description=_("Interval of duration."),
        required=False,
    )

    assumedValue=Duration(
        title_("Assumed Value"),
        description=_(" "),
        required=True,
    )
    
class CDuration(CPrimitive):
    """
    Constraints on durations.  openEHR allows the 'W' indicator to be mixed in.
    """
    
    implements(ICDuration)
    
