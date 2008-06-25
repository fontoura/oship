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
from zope.interface import implements

from dvtimespecification import DvTimeSpecification
from interfaces.dvgeneraltimespecification import IDvGeneralTimeSpecification

_ = MessageFactory('oship')
        
   
class DvGeneralTimeSpecification(DvTimeSpecification):
    u"""Specifies points in time in a general syntax. Based on the HL7v3 GTS data type."""
    
    implements(IDvGeneralTimeSpecification)
    
    def __init__(self,value):
        DvTimeSpecification.__init__(self,value)        
    
    def calendarAlignment():
        u"""Calendar alignment extracted from value. """
        
    def eventAlignment():
        u"""Event alignment extracted from value."""
        
    def institutionSpecified():
        u"""Extracted from value."""
        
    def valueValid():
        u"""value.formalism.is_equal(“HL7:GTS”)"""





        







