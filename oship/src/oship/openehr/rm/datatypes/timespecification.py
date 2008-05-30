# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
These are the time specification data types from Data Types Information Model
Quantity Package Rev. 2.1.0.
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.timespecification import *
from openehr.rm.datatypes.basic import DataValue



class DvTimeSpecification(DataValue):
    u"""
    This is an abstract class of which all timing specifications are specialisations.
    Specifies points in time, possibly linked to the calendar, or a real world repeating
    event, such as “breakfast”.
    """
    
    implements(IDvTimeSpecification)
    
    def __init__(self,value):
        self.value=value
            
    def calendarAlignment():
        u"""Indicates what prototypical point in the calendar the specification is
        aligned to, e.g. “5th of the month”. Empty if not aligned. Extracted from 
        the ‘value’ attribute.
        """
        
    def eventAlignment():
        u"""Indicates what real-world event the specification is aligned to if any.
        Extracted from the ‘value’ attribute.
        """
        
    def institutionSpecified():
        u"""Indicates if the specification is aligned with institution schedules, 
        e.g. a hospital nursing changeover or meal serving times. Extracted from 
        the ‘value’ attribute.
        """
        
    def valueValid():
        u"""value != None"""
        
class DvPeriodicTimeSpecification(DvTimeSpecification):
    u"""
    Specifies periodic points in time, linked to the calendar (phase-linked), 
    or a real world repeating event, such as “breakfast” (event-linked). 
    Based on the HL7v3 data types PIVL<T> and EIVL<T>.
    Used in therapeutic prescriptions, expressed as INSTRUCTIONs in the openEHR model.
    """
    
    implements(IDvPeriodicTimeSpecification)

    def __init__(self,value):
        DvTimeSpecification.__init__(self,value)        
        Field.__init__(self,**kwargs)

    
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
        
class DvGeneralTimeSpecification(DvTimeSpecification):
    u"""Specifies points in time in a general syntax. Based on the HL7v3 GTS data type."""
    
    implements(IDvGeneralTimeSpecification)
    
    def __init__(self,value):
        DvTimeSpecification.__init__(self,value)        
        Field.__init__(self,**kwargs)
    
    def calendarAlignment():
        u"""Calendar alignment extracted from value. """
        
    def eventAlignment():
        u"""Event alignment extracted from value."""
        
    def institutionSpecified():
        u"""Extracted from value."""
        
    def valueValid():
        u"""value.formalism.is_equal(“HL7:GTS”)"""





        







