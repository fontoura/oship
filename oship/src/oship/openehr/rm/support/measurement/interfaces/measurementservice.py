# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Interfaces for the measurement package in support_im.pdf Rev. 1.6.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import Interface
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class IMeasurementService(Interface):
    """Defines an object providing proxy access to a measurement information service."""

    
    
    def isValidUnitsString(units):
        u"""
        True if the units string 'units' is a valid string according to the HL7 UCUM specification.
        units != None                   
        """

    def unitsEquivalent(units1, units2):
        u"""
        True if two units strings correspond to the same measured property.
        isValidUnitsString(units1) and isValidUnitsString(units2)
        """
        