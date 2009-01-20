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
 Data Structure Package Rev. 2.1.0.

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = 'Andre Goncalves <goncalves.aluiz@gmail.com>'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from oship.openehr.rm.common.archetyped.locatable import Locatable 
from oship.openehr.rm.datastructures.interfaces.datastructure import IDataStructure

_ = MessageFactory('oship')


class DataStructure(Locatable):
    u"""
     Abstract parent class of all data structure types. Includes the as_hierarchy func-
    tion which can generate the equivalent CEN EN13606 single hierarchy for each
    subtype's physical representation. For example, the physical representation of an
    ITEM_LIST is List<ELEMENT>; its implementation of as_hierarchy will gener-
    ate a CLUSTER containing the set of ELEMENT nodes from the list.
    """

    implements(IDataStructure)
   
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
    
    def asHierarchy():
        u"""Hierarchical equivalent of the physical representation of each subtype, 
        compatible with CEN EN 13606 structures. Returns a List."""


