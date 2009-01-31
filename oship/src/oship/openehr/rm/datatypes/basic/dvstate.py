# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

 From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__Contributors__ = u'Roberto Cunha <roliveiracunha@yahoo.com.br>'

from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.datatypes.basic.datavalue import DataValue
from oship.openehr.rm.datatypes.basic.interfaces.dvstate import IDvState

_ = MessageFactory('oship')   
    
class DvState(DataValue):
    """
    For representing state values which obey a defined state machine, such as a vari-
    able representing the states of an instruction or care process.
    """

    implements(IDvState)
    
    def __init__(self, value, isTerminal):
        if value != None and value != '' and isTerminal != None:
            self.value = unicode(value)
            self.isTerminal = bool(isTerminal)
        else:
            raise TypeError, "You must supply values for 'value' and 'isTerminal'."
    
