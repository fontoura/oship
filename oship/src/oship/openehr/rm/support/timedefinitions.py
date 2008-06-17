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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements
from zope.schema import Int,Float,Field 
from zope.schema.interfaces import IField
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class ITimeDefinitions(IField):
    u"""
    Definitions for date/time classes. Note that the timezone limits are set by where
    the international dateline is. Thus, time in New Zealand is quoted using +12:00, not -12:00.
    """

    secondsInMinute = Int(
        title=_(u"Seconds in minute."),
        readonly=True,
        required=True,
        default=60,
        )
        
    minutesInHour = Int(
        title=_(u"Minutes in hour"),
        readonly=True,
        required=True,
        default=60,
        )
        
    hoursInDay = Int(
        title=_(u"Hours in day"),
        readonly=True,
        required=True,
        default=24,
        )
        
    nominalDaysInMonth = Float(
        title=_(u"Nominal days in month."),
        description=_(u"Used for conversions of durations containing months to days and / or seconds."),
        readonly=True,
        required=True,
        default=30.42,
        )
        
    maxDaysInMonth = Int(
        title=_(u"Max days in month."),
        description=_(u"Used for validity checking."),
        readonly=True,
        required=True,
        default=31,
        )
        
        
    daysInYear = Int(
        title=_(u"Days in year."),
        readonly=True, 
        required=True, 
        default=365, 
        )
    
    daysInLeapYear = Int(
        title=_(u"Days in leap year."),
        readonly=True, 
        required=True, 
        default=366,
        )
        
    maxDaysInYear = Int(
        title=_(u"Max days in year."),
        readonly=True, 
        required=True,
        default=daysInLeapYear,
        )

    nominalDaysInYear = Float(
        title=_(u"Nominal days in year."),
        description=_(u"Used for conversions of durations containing years to days and / or seconds."), 
        readonly=True, 
        required=True,
        default=365.24,
        )
    
    daysInWeek = Int(
        title=_(u"Days in week."),
        readonly=True,
        required=True, 
        default=7,
        )
        
        
    monthsInYear = Int(
        title=_(u"Months in year."),
        readonly=True,
        required=True, 
        default=12,
        )
        
        
    minTimeZone = Int(
        title=_(u"Min Time Zone"),
        readonly=True,
        required=True,
        default= -12,
        )

    
    maxTimeZone = Int(
        title=_(u"Max Time Zone"),
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
        
class TimeDefinitions(Field):
    u"""
    Definitions for date/time classes. Note that the timezone limits are set by where
    the international dateline is. Thus, time in New Zealand is quoted using +12:00, not -12:00.
    """

    implements(ITimeDefinitions)
    
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
        
