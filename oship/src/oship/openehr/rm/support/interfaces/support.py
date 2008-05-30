##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

Defines the interfaces for the support.support pkg. in support_im.pdf

"""

__author__  = u'Timothy Cook <tw_cook@comcast.net>'
__docformat__ = u'plaintext'

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

class IExternalEnvironmentAccess(IField):
    u"""A mixin class providing access to services in the external environment."""


    def eeaTerminologySvc(terminology_service):
        u""" 
        Return an interface to the terminology service or
        None if 'terminology_service' does not exist.
        isinstance(terminology_service, TerminologyService) 
        """
        
    def eeaMeasuremenSvc(measurement_service):
        u"""
        Return an interface to the measurement service or
        None if 'measurement_service' does not exist.
        isinstance(measurement_service, MeasurementService) 
        """
        
    def terminologyServiceExists():
        u""" True if eeaTerminologySvc != None """

    def measurementServiceExists():
        u""" True if eeaMeasurementSvc != None """
        
