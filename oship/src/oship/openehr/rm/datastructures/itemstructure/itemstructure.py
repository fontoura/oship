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
from zope.interface import implements,classProvides 
from openehr.rm.datastructures.datastructure import DataStructure
from openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure

_ = MessageFactory('oship')

class ItemStructure(DataStructure):
    u"""
    Abstract parent class of all spatial data types.
    """
    
    implements(IItemStructure)
    classProvides(IItemStructure)
    
    