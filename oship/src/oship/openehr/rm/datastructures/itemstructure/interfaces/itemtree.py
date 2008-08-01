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
__Contributors__ = u'Roberto Cunha <roliveiracunha@yahoo.com.br>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.i18nmessageid import MessageFactory
from zope.schema import List, Object

from itemstructure import IItemStructure
from oship.openehr.rm.datastructures.itemstructure.representation.interfaces.item import IItem 

_ = MessageFactory('oship')

class IItemTree(IItemStructure):
    u"""
    Logical tree data structure. 
    """
    
    # the list contents should be restricted to schema = IItem,
    items = List(
        value_type=Object(schema=IItem),
        title=_(u"items"),
        description=_(u"Physical representation of the tree."),
        required=False
    )
     
    def hasElementPath(a_path):
        u"""Return True if a_path is a valid leaf element path."""
        
    def elementAtPath(a_path):
        u"""Return the leaf element at the path; a_path."""
           
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""
    

