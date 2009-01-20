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
 Item Structure Package Rev. 2.1.0.

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from itemstructure import ItemStructure
from interfaces.itemsingle import IItemSingle

_ = MessageFactory('oship')

class ItemSingle(ItemStructure):
    u"""
    Logical single value data structure.
    Used to represent any data which is logically a single value, such as a person's height or weight.   
    """
    
    implements(IItemSingle)
    
    def __init__(self,item):
        self.item=item
        
    
    def asHierarchy():
        u"""
        Generate a CEN EN13606-compatible hierarchy consisting of a single ELEMENT.
        """
