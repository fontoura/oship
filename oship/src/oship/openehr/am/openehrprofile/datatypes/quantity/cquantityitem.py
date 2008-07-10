# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The Archetype Profile quantity package. 
From the openEHR Archetype Profile specifications Rev. 1.0.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import Interface
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class ICQuantityItem(Interface):
    """
    Constrains instances of DvQuantity.
    """
    
    magnitude = Float(
        title=_(u"Magnitude"),
        description=_(u"""Interval constraint on magnitude."""),
        required=False,
        )
    
    precision = Int(
        title=_(u"Precision"),
        description=_(u"""Interval constraint on precision."""),
        required=False,
        )

    units = TextLine(
        title=_(u"Units"),
        description=_(u"""Constraint on units."""),
        required=True,
        )
    
    def precisionUnconstrained():       
        """
        True if no constraint on precision; True if precision = -1.
        precision = -1 implies Result
        """
    