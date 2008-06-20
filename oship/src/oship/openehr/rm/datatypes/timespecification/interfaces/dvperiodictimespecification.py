# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From Data Types Information Model
Time Specification Package Rev. 2.1.0.

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.dvperiodictimespecification import IDvPeriodicTimeSpecification,DvPeriodicTimeSpecification

_ = MessageFactory('oship')
        


class IDvPeriodicTimeSpecification(IDvTimeSpecification):
    """
    Specifies periodic points in time, linked to the calendar (phase-linked), 
    or a real world repeating event, such as “breakfast” (event-linked). 
    Based on the HL7v3 data types PIVL<T> and EIVL<T>.
    Used in therapeutic prescriptions, expressed as INSTRUCTIONs in the openEHR model.
    """
    
    def period():
        """The period of the repetition, computationally derived from the syntax 
        representation. Extracted from the ‘value’ attribute. Returns a DvDuration.
        """

    def calendarAlignment():
        """Calendar alignment extracted from value."""


    def eventAlignment():
        u"""Event alignment extracted from value."""
        
    def institutionSpecified():
        """Extracted from value. """
        
    def valueValid():
        """value.formalism.is_equal(“HL7:PIVL”) or value.formalism.is_equal(“HL7:EIVL”)"""

        
        
class DvPeriodicTimeSpecification(DvTimeSpecification):
    u"""
    Specifies periodic points in time, linked to the calendar (phase-linked), 
    or a real world repeating event, such as “breakfast” (event-linked). 
    Based on the HL7v3 data types PIVL<T> and EIVL<T>.
    Used in therapeutic prescriptions, expressed as INSTRUCTIONs in the openEHR model.
    """
    
    implements(IDvPeriodicTimeSpecification)

    def __init__(self,value):
        self.value=value        

    
    def period():
        u"""The period of the repetition, computationally derived from the syntax 
        representation. Extracted from the ‘value’ attribute.
        """

    def calendarAlignment():
        u"""Calendar alignment extracted from value."""


    def eventAlignment():
        u"""Event alignment extracted from value."""
        
    def institutionSpecified():
        u"""Extracted from value. """
        
    def valueValid():
        u"""value.formalism.is_equal(“HL7:PIVL”) or value.formalism.is_equal(“HL7:EIVL”)"""
