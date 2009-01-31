# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from dvtimespecification import IDvTimeSpecification

_ = MessageFactory('oship')
        
class IDvGeneralTimeSpecification(IDvTimeSpecification):
    """Specifies points in time in a general syntax. Based on the HL7v3 GTS data type."""
    
    def calendarAlignment():
        """Calendar alignment extracted from value. """
        
    def eventAlignment():
        """Event alignment extracted from value."""
        
    def institutionSpecified():
        """Extracted from value."""
        
    def valueValid():
        """value.formalism.is_equal("HL7:GTS")"""

