# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the encapsulated data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.datatypes.encapsulated.dvencapsulated import DvEncapsulated
from interfaces.dvparsable import IDvParsable

_=MessageFactory('oship')
 
class DvParsable(DvEncapsulated):
    u"""
    Encapsulated data expressed as a parsable String. The internal model of the data item is not 
    described in the openEHR model in common with other encapsulated types, but in this case, the 
    form of the data is assumed to be plaintext, rather than compressed or other types of large binary data.
    Used for representing values which are formal textual representations, e.g. guidelines.
    """
    
    implements(IDvParsable)

    def __init__(self,size,value,formalism):
        self.size=len(value)
        self.value=value
        self.formalism=formalism

    def valueValid():
        u"""value != None."""
        return self.value!=None

    def formalismValidity():
        u"""formalism != None and formalism != '' """
        return formalism!=None and formalism!=''
    
        
