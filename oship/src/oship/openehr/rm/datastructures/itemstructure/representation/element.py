# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

From the Data Structures Information Model
 Representation Package Rev. 2.1.0.

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from item import Item
from interfaces.element import IElement

_ = MessageFactory('oship')
    
class Element(Item):
    u"""The leaf variant of ITEM, to which a DATA_VALUE instance is attached."""
 
    implements(IElement)
    
    def __init__(self,value,nullFlavor,**kw):
        self.value=value
        self.nullFlavor=nullFlavor
        for n,v in kw.items():
            setattr(self,n,v)

    
    def isNull():
        u"""Return True if value is unknown, etc."""
        
    def nullFlavorValid(obj):
        u"""If value is None then nullFlavor must be in the terminology code set for null flavors."""
        
