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

from openehr.rm.datatypes.datavalue import IDataValue,DataValue
from openehr.rm.datatypes.dvparsable import DvParasable

_ = MessageFactory('oship')


class IDvTimeSpecification(IDataValue):
    """
    This is an abstract class of which all timing specifications are specialisations.
    Specifies points in time, possibly linked to the calendar, or a real world repeating
    event, such as “breakfast”.
    """
    
    value = DvParsable(
        title=_(u"value"),
        description=_(u"""the specification, in the HL7v3 syntax for PIVL or EIVL types. 
                    See section 8.2.2.1 Phase-linked Time Specification Syntax"""),
        required=True
    )
    
    def calendarAlignment():
        """Indicates what prototypical point in the calendar the specification is
        aligned to, e.g. “5th of the month”. Empty if not aligned. Extracted from 
        the ‘value’ attribute.
        """
        
    def eventAlignment():
        """Indicates what real-world event the specification is aligned to if any.
        Extracted from the ‘value’ attribute.
        """
        
    def institutionSpecified():
        """Indicates if the specification is aligned with institution schedules, 
        e.g. a hospital nursing changeover or meal serving times. Extracted from 
        the ‘value’ attribute.
        """
        

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