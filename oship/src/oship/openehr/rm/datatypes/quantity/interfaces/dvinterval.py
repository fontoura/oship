# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the quantity data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Fabricio Ferracioli <fabricioferracioli@gmail.com>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Object,Bool

from oship.openehr.rm.datatypes.quantity.interfaces.dvordered import IDvOrdered
from oship.openehr.rm.datatypes.basic.interfaces.datavalue import IDataValue
from oship.openehr.rm.support.interval import *

_ = MessageFactory('oship')

          
class IDvInterval(IDataValue):
    """
    Used to define intervals of dates, times, quantities (whose units match) and so on.
    The type parameter, T, must be a descendant of the type DV_ORDERED, which is
    necessary (but not sufficient) for instances to be compared (strictly_comparable
    is also needed).
    Without the DV_INTERVAL class, quite a few more DV_ classes would be needed
    to express logical intervals, namely interval versions of all the date/time classes,
    and of quantity classes. Further, it allows the semantics of intervals to be stated in
    one place unequivocally, including the conditions for strict comparison.
    The basic semantics are derived from the class INTERVAL<T>, described in the
    support RM.
    """

    lower = Object(
        schema=IDvOrdered,
        title=_(u"lower value"),
        description=_(u"""Interval lower value."""),
        required=True
    )
    
    upper = Object(
        schema=IDvOrdered,
        title=_(u"upper value"),
        description=_(u"""Interval upper value."""),
        required=True
    )
    
    
    lower_included = Bool(
        title=_(u"Lower value included"),
        description=_(u"""Lower value included in interval."""),
        required=True
    )    
    
    upper_included = Bool(
        title=_(u"upper value"),
        description=_(u"""Interval upper value."""),
        required=True
    )
    
    lower_unbounded = Bool(
        title=_(u"lower unbounded"),
        description=_(u"""Lower value unbounded in interval."""),
        required=False
    )    
    
    upper_unbounded = Bool(
        title=_(u"upper unbounded"),
        description=_(u"""Upper value unbounded in interval."""),
        required=False
    )