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

from zope.interface import Interface
from zope.schema import *

class ICPrimitive(Interface):
    """
    Abstract super type of all primitive types.
    """
    
    defaultValue=Field(
        title_("Default Value"),
        description=_("A default value for this constriant object."),
        required=True,
    )
    
    hasAssumedValue=Bool(
        title_("Has Assumed Value"),
        description=_("True if thiere is an assumed value."),
        required=True,
    )

    def validValue(aVal):
        """
        True if aValue is valid with respect to the expressed constraint.
        """
        
class ICBoolean(ICPrimitive):
    """
    Boolean constraint.
    """
    
    trueValid=Bool(
        title_("True Valid"),
        description=_("True if value True is allowed."),
        required=True,
    )
    
    falseValid=Bool(
        title_("False Valid"),
        description=_("True if the value False is allowed."),
        required=True,
    )
    
    assumedValue=Bool(
        title_("Assumed Value"),
        description=_("The value to assume of this item is not included in the data."),
        required=True,
    )
    

class ICInteger(ICPrimitive):
    """
    Constraint on integers.
    """
    
    list=Set(
        title_("List"),
        description=_("Set of integers specifying constraints."),
        required=False,
    )
    
    range=Interval(
        title_("Range"),
        description=_("Range of integers specifying constraint."),
        required=False,
    )
    
    assumedValue=Int(
        title_("Assumed Value"),
        description=_("The value to assume if this item is not in the data."),
        required=True,
    )
    

class ICReal(ICPrimitive):
    """
    Constraints on instances of Real
    """
    
    list=Set(
        title_("List"),
        description=_("Set of Reals specifying constraint"),
        required=False,
    )


    range=Interval(
        title_("Range"),
        description=_(" "),
        required=False,
    )

    assumedValue=Float(
        title_("Assumed Value"),
        description=_(""),
        required=True,
    )

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
        required=True,
    )

    def validityIsRange:
        """
        Returns True if the validity is in the form of a range.
        """


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


class ICDateTime(ICPrimitive):
    """
    ISO 8601 compatible constraint on instances of DateTime.
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
    
    hourValidity=ValidityKind(
        title_("Hour Validity"),
        description=_(" "),
        required=False,
    )

   
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

    assumedValue=Datetime(
        title_("Assumed Value"),
        description=_(" "),
        required=True,
    )

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """

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
    
    