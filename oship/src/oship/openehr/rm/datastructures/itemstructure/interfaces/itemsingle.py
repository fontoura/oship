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

from itemstructure import IItemStructure
from openehr.rm.datastructures.history.event import Event

_ = MessageFactory('oship')

class IItemSingle(IItemStructure):
    u"""
    Logical single value data structure.
    Used to represent any data which is logically a single value, such as a person’s height or weight.   
    """
    
    item = Element(
        title=_(u"item"),
        description=_(u"""Single item."""),
        required=True
    )
    
    def asHierarchy():
        u"""
        Generate a CEN EN13606-compatible hierarchy consisting of a single ELEMENT.
        """
