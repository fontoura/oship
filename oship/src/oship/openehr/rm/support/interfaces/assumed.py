##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

Defines the interfaces primitive and other data types assumed by openEHR support_im.pdf

"""
__author__  = u'Timothy Cook <tw_cook@comcast.net>'
__docformat__ = u'plaintext'

from zope.interface import Interface
from zope.schema import *

class IAny(IObject):
    u"""
    Abstract supertype. Usually maps to a type like “Any” or “Object” in an object
    system. Defined here to provide the value and reference equality semantics.
    """

class IOrdered(IOrderable):
    u"""
    Abstract notional parent class of ordered, types i.e. types on which the ‘<‘ operator is defined.
    """
       
class IAggregate(ICollection):
   u"""
   Abstract parent of of the aggregate types List<T>, Set<T>, Array<T> and Hash<T,K>.
   """

   def has(value):
       u"""
       Test for membership of a value. Returns a boolean       
       """
       
   def count():
       u"""
       Number of items in container. Returns an Integer
       """
       
   def isEmpty():
      u"""
      Returns True if container is empty. 
      """

class IBoolean(IBool):
    u"""Boolean type used for two-valued mathematical logic."""
    
class INumeric(IInt):
    u""" Represents numeric types.  I'm not too sure this is correct but it's my best guess."""    
    
class IOrderedNumeric(IOrdered, INumeric):
    u"""
    Abstract notional parent class of ordered, numeric types, which are types with ‘<‘
    and arithmetic operators defined
    """
    
class IInteger(IInt):
    u"""Integer type"""
    
class IReal(IFloat):
    u"""
    Type used to represent decimal numbers. Typically corresponds to a single-precision 
    floating point value in most languages.
    """
    
class IDouble(IFloat):
    u"""
    Type used to represent decimal numbers. Typically corresponds to a double-precision 
    floating point value in most languages.
    """
    
class ICharacter(ILen):
    u"""A Field requiring its value to have a length of 1
    and to be an instance of str.
    The value needs to have a conventional __len__ method.
    """
    
class IString(IText):
    u"""A field containing a unicode string."""
    
class IArray(schema.ISequence):
    u"""Container whose storage is assumed to be contiguous"""

class IList(schema.IList):
    u"""Ordered container that may contain duplicates."""

class ISet(IAbstractSet):
    u"""Unordered container that may not contain duplicates"""

class IHash(IDict):
    u"""
    Hash <T, U: Comparable>    
    Type representing a keyed table of values. T is the value type, 
    and U the type of the keys.
    """

class IInterval(Interface):
    u"""
    Interval of ordered items.
    See oship/lib/python/oship/openehr/rm/support/interval/interval.py to
    complete this interface.
    
    interval.py is Courtesy Jacob Page; http://members.cox.net/apoco/interval/
    """


class ITimeDefinitions(IField):
    u"""
    Definitions for date/time classes. Note that the timezone limits are set by where
    the international dateline is. Thus, time in New Zealand is quoted using +12:00, not -12:00.
    """

    secondsInMinute = Int(
        title=u"""Seconds in minute.""",
        readonly=True,
        required=True,
        default=60,
        )
        
    minutesInHour = Int(
        title=u"""Minutes in hour""",
        readonly=True,
        required=True,
        default=60,
        )
        
    hoursInDay = Int(
        title=u"""Hours  in day""",
        readonly=True,
        required=True,
        default=24,
        )
        
    nominalDaysInMonth = Float(
        title=u"""Nominal days in month.""",
        description=u"""Used for conversions of durations containing months to days and / or seconds.""",
        readonly=True,
        required=True,
        default=30.42,
        )
        
    maxDaysInMonth = Int(
        title=u"""Max days in month.""",
        description=u"""Used for validity checking.""",
        readonly=True,
        required=True,
        default=31,
        )
        
        
    daysInYear = Int(
        title=u"""Days in year.""",
        readonly=True, 
        required=True, 
        default=365, 
        )
    
    daysInLeapYear = Int(
        title=u"""Days in leap year.""",
        readonly=True, 
        required=True, 
        default=366,
        )
        
    maxDaysInYear = Int(
        title=u"""Max days in year.""",
        readonly=True, 
        required=True,
        default=daysInLeapYear,
        )

    nominalDaysInYear = Float(
        title=u"""Nominal days in year.""",
        description=u"""Used for conversions of durations containing years to days and / or seconds.""", 
        readonly=True, 
        required=True,
        default=365.24,
        )
    
    daysInWeek = Int(
        title=u"""Days in week.""",
        readonly=True,
        required=True, 
        default=7,
        )
        
        
    monthsInYear = Int(
        title=u"""Months in year.""",
        readonly=True,
        required=True, 
        default=12,
        )
        
        
    minTimeZone = Int(
        title=u"""Min Time Zone""",
        readonly=True,
        required=True,
        default= -12,
        )

    
    maxTimeZone = Int(
        title=u"""Max Time Zone""",
        readonly=True,
        required=True,
        default= +13,
        )
    
    def validYear(y):
        u""" True if y >= 0)"""
        
    def validMonth(m):
        u"""True if m >= 1 and m <= monthsInYear"""
        
    def validDay(y,m,d):
        u"""True if d >= 1 and d <= daysInMonth(m,y)"""
        
    def validHour(h,m,s):
        u"""True if (h >= 0 and h < hoursInDay) or (h = hoursInDay and m = 0 and s = 0)"""
        
        
    def validMinute(m):
        u"""True if m >= 0 and m < minutesInHour"""


    def validSecond(s):
        u"""True if s >= 0 and s < secondsInMinute"""
        
    def validFractionalSecond(fs):
        u"""True if fs >= 0.0 and fs < 1.0"""
        

class IIso8601Date(IOrdered, ITimeDefinitions):
    u"""
    Represents an absolute point in time, as measured on the Gregorian calendar, and specified only to the day.
    """
      
    def asString():
        u"""Date as string ISO8601 string for date, in format YYYYMMDD or YYYY-MM-DD, or a
        partial invariant. See validIso8601Date for validity."""
        
    
    def year():
        u"""
        Returns the year as an Int
        """
    
    def month():
        u"""
        Returns the month as an Int.
        Implies monthUnknown == False
        """
    
    def day():
        u"""
        Returns the day of the month as an Int.
        Implies dayUnknown == False
        """
          
    def monthUnknown():
        u"""Indicates whether month in year is unknown. If so, the date is of the form “YYYY”."""
        
    def dayUnknown():
        u"""Indicates whether day in month is unknown. If so, and month is known, the date is 
        of the form “YYYY-MM” or “YYYYMM”."""
        
    def isPartial():
        u"""True if this date is partial, i.e. if day or more is missing."""
        
    def isExtended():
        u"""True if this date uses ‘-’ separators."""

    def validIso8601Date(s):
        u"""
        String 's' is a valid ISO 8601 date, i.e. takes the complete form: YYYYMMDD
        or the extended form: YYYY-MM-DD
        or one of the partial forms: YYYYMM; YYYY
        or the equivalent extended form:  YYYY-MM

        Where:
        YYYY is the string form of any positive number in the range “0000” - “9999”
        (zero-filled to four digits) MM is “01” - “12” (zero-filled to two digits)
        DD is “01” - “31” (zero-filled to two digits)
        
        The combinations of YYYY, MM, DD numbers must be correct with respect to the Gregorian calendar.
        """
        
    def yearValid():
        u""" Return validYear(year)"""
        
    def monthValid():
        u"""Return validMonth(month)"""
        
    def dayValid():
        u"""Return validDay(year,month,day)"""
        
    def partialValidity():
        u"""month_unknown implies day_unknown"""

        
class IIso8601Time(IOrdered,ITimeDefinitions):
    u"""
    Represents an absolute point in time from an origin usually interpreted as meaning 
    the start of the current day, specified to the second.

    A small deviation to the ISO 8601:2004 standard in this class is that the time
    24:00:00 is not allowed, for consistency with ISO8601_DATE_TIME.
    """
    
    def asString():
        u"""
        ISO8601 string for time, i.e. in form: hhmmss[,sss][Z|±hh[mm]] 
        or the extended form: hh:mm:ss[,sss][Z|±hh[mm]], 
        or a partial invariant. See valid_iso8601_time for validity.
        """
        
    def hour():
        u"""Hour in day, in 24-hour time."""
        
    def minute():
        u"""Minute in hour. Requires minuteUnknown == False"""
        
    def second():
        u"""Second in minute. Requires secondUnknown == False"""
        
    def fractionalSecond():
        u"""Fractional seconds. Requires secondUnknown == False"""
        
    def hasFractionalSecond():
        u"""Return True if the fractional_second part is signficant (i.e. even if = 0.0)."""
        
    def timezone():
        u"""Time zone; may be Void."""
        
    def minuteUnknown():
        u"""Indicates whether minute is unknown. If so, the time is of the form “hh”. """
        
    def secondUnknown():
        u"""Indicates whether second is unknown. If so and month is known, the time is 
        of the form “hh:mm” or “hhmm”. """
        
    def isPartial():
        u"""True if this time is partial, i.e. if seconds or more is missing."""
        
    def isExtended():
        u"""True if this time uses ‘:’ separators."""
        
    def isDecimalSignComma():
        u"""True if this time has a decimal part indicated by ‘,’ (comma) rather than ‘.’ (period)."""
        
    def validIso8601Time(s):
        u"""
        String 's' is a valid ISO 8601 date, i.e. takes the form: hhmmss[,sss][Z | ±hh[mm]]
        or the extended form: hh:mm:ss[,sss][Z | ±hh[mm]]
        or one of the partial forms: hhmm or hh
        or the extended form: hh:mm
        with an additional optional timezone indicator of: Z or ±hh[mm]
        
        Where:
        hh is “00” - “23” (0-filled to two digits)
        mm is “00” - “59” (0-filled to two digits)
        ss is “00” - “60” (0-filled to two digits)
        sss is any numeric string, representing an
        optional fractional second Z is a literal meaning UTC (modern replacement for GMT), 
        i.e. timezone +0000 ±hh[mm], i.e. +hhmm, +hh, -hhmm, -hh indicating the timezone.
        """

    def hourValid():
        u"""validHour(hour, minute, second)"""
        
    def minuteValid():
        u""" not minutUnknown implies validMinute(minute)"""
        
    def secondValid():
        u"""not secondUnknown implies validSecond(second)"""
        
    def fractionalSecondValid():
        u"""hasFractionalSecond implies (not seconUnknown and validFractionalSecond(fractionalSecond))"""
        
    def partialValidity():
        u"""minuteUnknown implies secondUnknown"""
        

class IIso8601DateTime(IOrdered, ITimeDefinitions):
    u"""
    Represents an absolute point in time, specified to the second.
    
    Note that this class includes 2 deviations from ISO 8601:2004:
    for partial date/times, any part of the date/time up to the month may be
    missing, not just seconds and minutes as in the standard;
 
    the time 24:00:00 is not allowed, since it would mean the date was
    really on the next day.
    """

    def asString():
        u"""
        ISO8601 string for date/time, in format YYYYMMDDThhmmss[,sss][Z | ±hh[mm]] 
        or in extended format YYYY-MM-DDThh:mm:ss[,sss][Z | ±hh[mm]] 
        or a partial variant; see valid_iso8601_date_time() below.
        """
    
    def year():
        u"""Return year as an Int >= 0"""
        
    def month():
        u"""Return month in year as an Int. Require monthUnknown==False."""
        
    def day():
        u"""Return day in month as an Int. Require dayUnknown==False."""
        
    def hour():
        u"""Return hour in day as an Int. Require hourUnknown==False."""

    def minute():
        u"""Return minute in hour as an Int. Require minuteUnknown==False."""
        
    def second():
        u"""Return second in minute as an Int. Require secondUnknown==False."""
        
    def fractionalSecond():
        u"""Return fractional seconds in minute as a Float. Require secondUnknown==False."""
    
    def hasFractionalSecond():
        u"""Return True if the fractional_second part is signficant (i.e. even if = 0.0)."""
        
    def timezone():
        u"""Time zone; may be Void."""
        
    def minuteUnknown():
        u"""Indicates whether minute is unknown. If so, the time is of the form “hh”. """
        
    def secondUnknown():
        u"""Indicates whether second is unknown. If so and month is known, the time is 
        of the form “hh:mm” or “hhmm”. """
        
    def isPartial():
        u"""True if this time is partial, i.e. if seconds or more is missing."""
        
    def isExtended():
        u"""True if this date/time uses '-', ‘:’ separators."""
        
    def isDecimalSignComma():
        u"""True if this time has a decimal part indicated by ‘,’ (comma) rather than ‘.’ (period)."""
    
    def validIso8601DateTime(s):
        u"""
        String is a valid ISO 8601 date-time, i.e.
        takes the form: YYYYMMDDThhmmss[,sss][Z | ±hh[mm]]
        or the extended form: YYYY-MM-DDThh:mm:ss[,sss][Z | ±hh[mm]]
        or one of the partial forms: YYYYMMDDThhmm,   YYYYMMDDThh
        or the equivalent extended forms: YYYY-MM-DDThh:mm,  YYYY-MM-DDThh

         (meanings as in DvDate, DvTime) and the values in each field are valid.
        """

    def yearValid():
        u""" Return validYear(year)"""
        
    def monthValid():
        u"""Return validMonth(month)"""
        
    def dayValid():
        u"""Return validDay(year,month,day)"""
        
    def hourValid():
        u"""validHour(hour, minute, second)"""
        
    def minuteValid():
        u""" not minutUnknown implies validMinute(minute)"""
        
    def secondValid():
        u"""not secondUnknown implies validSecond(second)"""
        
    def fractionalSecondValid():
        u"""hasFractionalSecond implies (not seconUnknown and validFractionalSecond(fractionalSecond))"""

    def partialValidityYear(): 
        u""" not month_unknown"""
    
    def partialValidityMonth(): 
        u"""not month_unknown"""
    
    def partialValidityDay(): 
        u"""not day_unknown"""
    
    def partialValidityHour(): 
        u"""not hour_unknown"""
    
    def partialValidityMinute(): 
        u"""minuteUnknown implies secondUnknown"""

class IIso8601Timezone(ITimeDefinitions):
    u"""
    Represents a timezone as used in ISO 8601.
    """
    
    def asString():
        u"""
        ISO8601 timezone string, in format  Z | ±hh[mm]
        where:
        hh is “00” - “23” (0-filled to two digits)
        mm is “00” - “59” (0-filled to two digits)
        Z is a literal meaning UTC (modern replacement for GMT), i.e. timezone +0000
        """
        
        
    def hour():
        u"""Hour part of timezone - in the range 00 - 12 as an Int."""
        
    def minute():
        u"""
        Minute part of timezone. Generally 00 or 30. as an Int.
        Require minuteUnknown==False
        """

    def sign():
        u"""Direction of timezone expresssed as +1 or -1."""

    def isGMT():
        u"""True if timezone is UTC, i.e. +0000"""
        
    def minuteUnknown():
        u"""Indicates whether minute part known."""
        
    def hourValid():
        u"""hour >= 0 and hour <= Max_timezone_hour"""
        
    def minuteValid():
        u"""not minuteUnknown implies validMinute(minute)"""
        
    def signValid():
        u"""sign = 1 or sign = -1"""
        
class IIso8601Duration(IOrdered,ITimeDefinitions):
    u"""
    Represents a period of time corresponding to a difference between two time-points.
    """

    def asString():
        u"""ISO8601 string for duration, in format P[nnY][nnM][nnW][nnD][T[nnH][nnM][nnS]]"""
        
    def years():
        u"""number of years of nominal 365 day length"""
        
    def months():
        u"""number of months of nominal 30 day length"""
    
    def weeks():
        u"""number of 7 day weeks"""
        
    def days():
        u"""number of 24 hour days"""
        
    def hours():
        u"""number of 60 minute hours"""
        
    def minutes():
        u"""number of 60 second minutes"""
        
    def fractionalSeconds():
        u"""fractional seconds"""
        
    def validIso8601Duration():
        u"""
        String is a valid ISO 8601 duration, i.e. takes the form: P[nnY][nnM][nnW][nnD][T[nnH][nnM][nnS]]

        Where each nn represents a number of years,months, etc. nnW represents a number of 7-day weeks.
        
        Note: allowing the W designator in the same expression as other designators is an exception to 
        the published standard, but necessary in clinical information (typically for representing 
        pregnancy duration).
        """

    def isDecimalSignComma():
        u"""
        True if this time has a decimal part indicated by ‘,’ (comma) rather than ‘.’ (period).
        """
    
    def toSeconds():
        u"""Total number of seconds equivalent (including fractional) of entire duration."""
        
    def yearsValid(): 
        u""" years >= 0"""
    
    def monthsValid(): 
        u""" months >= 0"""
    
    def weeksValid(): 
        u""" weeks >= 0"""
    
    def daysValid(): 
        u""" days >= 0"""
    
    def hoursValid(): 
        u""" hours >= 0"""
    
    def minutesValid(): 
        u""" minutes >= 0"""
    
    def secondsValid(): 
        u""" seconds >= 0"""
    
    def fractionalSecondValid(): 
        u"""fractionalSecond >= 0.0 and fractionalSecond < 1.0"""
    
