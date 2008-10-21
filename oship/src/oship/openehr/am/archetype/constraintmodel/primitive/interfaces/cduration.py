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

from zope.schema import Bool
from zope.i18nmessageid.message import MessageFactory

#from oship.openehr.am.archetype.constraintmodel.primitive.cduration import CDuration
from oship.openehr.am.archetype.constraintmodel.primitive.interfaces.cprimitive import ICPrimitive
from oship.openehr.rm.support.interval import Interval

_ = MessageFactory('oship')

class ICDuration(ICPrimitive):
    """
    Constraints on durations.  openEHR allows the 'W' indicator to be mixed in.
    """
    
    yearsAllowed=Bool(
        title=_(u"Years Allowed"),
        description=_(u"True if years are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    monthsAllowed=Bool(
        title=_(u"Months Allowed"),
        description=_(u"True if months are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    weeksAllowed=Bool(
        title=_(u"Weeks Allowed"),
        description=_(u"True if weeks are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    daysAllowed=Bool(
        title=_(u"Days Allowed"),
        description=_(u"True if days are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    hoursAllowed=Bool(
        title=_(u"Hours Allowed"),
        description=_(u"True if hours are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    minutesAllowed=Bool(
        title=_(u"Minutes Allowed"),
        description=_(u"True if minutes are allowed in the constrained duration."),
        required=False,
        default=True,
    )

    secondsAllowed=Bool(
        title=_(u"Seconds Allowed"),
        description=_(u"True if seconds are allowed in the constrained duration."),
        required=False,
        default=True,
    )
    
    fractionalSecondsAllowed=Bool(
        title=_(u"Fractional Seconds Allowed"),
        description=_(u"True if fractional seconds are allowed in the constrained duration."),
        required=False,
        default=True,
    )
    """
    range=Interval(
        title=_(u"Range"),
        description=_(u"Interval of duration."),
        required=False,
    )
    """
    
    """ causes a circular import
    assumedValue=Duration(
        title=_(u"Assumed Value"),
        description=_(u" "),
        required=True,
    )
    """    
