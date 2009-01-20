# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>', u'Roberto Cunha <roliveiracunha@yahoo.com.br>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements

from oship.openehr.am.archetype.constraintmodel.cobject import CObject
from oship.openehr.am.archetype.constraintmodel.interfaces.cdefinedobject import ICDefinedObject

_ = MessageFactory('oship')

class CDefinedObject(CObject):
    """
    Abstract parent of CObject subtypes that are defined by this value.
    """
    
    implements(ICDefinedObject)
    
    def __init__(self, rmTypeName, occurence, nodeId, parent, assumedValue):
        CObject.__init__(self, rmTypeName, occurence, nodeId, parent)
        self.assumedValue = assumedValue
        
    def hasAssumedValue():
        """
        Return True if assumedValue is not equal to None.
        """
        return self.returnedValue != None
    
    def validValue(a_value):
        return a_value != None
    