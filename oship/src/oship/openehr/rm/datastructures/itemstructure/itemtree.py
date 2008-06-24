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

_ = MessageFactory('oship')

class ItemTree(ItemStructure):
    u"""
    Logical tree data structure. The tree may be empty. Used to represent data which are 
    logically a tree such as audiology results, microbiology results, biochemistry results.
    """
    
    implements(IItemTree)
    
    def __init__(self,items,**kw):
        self.items=items
        for n,v in kw.items():
            setattr(self,n,v)
    
    def hasElementPath(a_path):
        u"""Return True if a_path is a valid leaf element path."""
        
    def elementAtPath(a_path):
        u"""Return the leaf element at the path; a_path."""
           
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""
    
