# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Implementation for the measurement package in support_im.pdf Rev. 1.6.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__version__ = '1.0.1a1'
__contributors__ = ''

from zope.interface import implements
from zope.schema import Text, TextLine, Field

class MeasurementService(Field):
    """Defines an object providing proxy access to a measurement information service."""

    implements(IMeasurementService)
    
    
    def isValidUnitsString(units):
        u"""
        True if the units string ‘units’ is a valid string according to the HL7 UCUM specification.
        units != None                   
        """

    def unitsEquivalent(units1, units2):
        u"""
        True if two units strings correspond to the same measured property.
        isValidUnitsString(units1) and isValidUnitsString(units2)
        """
        
