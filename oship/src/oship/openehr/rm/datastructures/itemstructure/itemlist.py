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
from zope.schema import List

from openehr.rm.datastructures.itemstructure import ItemStructure,IItemStructure
_ = MessageFactory('oship')
    
class IItemList(IItemStructure):
    u"""
    Logical list data structure, where each item has a value and can be referred to by a name 
    and a positional index in the list. The list may be empty.
    """
    
    items = List(
        title=_(u"items"),
        description=_(u"""Physical representation of the list."""),
        required=False
    )
    
    
    def itemCount():
        u"""Count of all items."""
        
    def names():
        u"""Return the names of all items."""
        
    def namedItem(str):
        u"""Return the named 'str'"""
        
    def ithItem(n):
        u"""Return the 'n' ith item."""
        
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""
    
class ItemList(ItemStructure):
    u"""
    Logical list data structure, where each item has a value and can be referred to by a name 
    and a positional index in the list. The list may be empty.
    """
    implements(IItemList)
    
    def __init__(self,items,**kw):
        self.item=items
        for n,v in kw.items():
            setattr(self,n,v)
       
    
    def itemCount():
        u"""Count of all items."""
        
    def names():
        u"""Return the names of all items."""
        
    def namedItem(str):
        u"""Return the named 'str'"""
        
    def ithItem(n):
        u"""Return the 'n' ith item."""
        
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""
