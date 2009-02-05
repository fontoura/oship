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

from zope.schema import Time,Object
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.interfaces.validitykind import IValidityKind
from oship.openehr.rm.support.interval import Interval
from oship.openehr.am.archetype.constraintmodel.primitive.interfaces.cprimitive import ICPrimitive

_ = MessageFactory('oship')

class ICTime(ICPrimitive):
    """
    ISO 8601 compatible constraint on instances of Time.
    """
    
    minuteValidity=Object(
        schema=IValidityKind,
        title=_(u"Minute Validity"),
        description=_(u" "),
        required=False,
    )
    

    secondValidity=Object(
        schema=IValidityKind,
        title=_(u"Second Validity"),
        description=_(u" "),
        required=False,
    )
    
    millisecondValidity=Object(
        schema=IValidityKind,
        title=_(u"Millisecond Validity"),
        description=_(u" "),
        required=False,
    )
    
    timezoneValidity=Object(
        schema=IValidityKind,
        title=_(u"Timezone Validity"),
        description=_(u" "),
        required=False,
    )
    """ Interval is not a zope schema field
    range=Interval(
        title=_(u"Range"),
        description=_(u"Interval of times."),
        required=False,
    )
    """
    
    assumedValue=Time(
        title=_(u"Assumed Value"),
        description=_(u" "),
        required=True,
    )

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """
