# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementation for Data Structures Information Model
 Representation Package Rev. 2.1.0.

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from oship.openehr.rm.datastructures.interfaces.representation import *

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class Item(Locatable):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """

class Cluster(Item):
    u"""
    The grouping variant of ITEM, which may contain further instances of ITEM, in an ordered list.
    """

    implements(ICluster)
    
    def __init__(self,items,**kwargs):
        self.items=items
    
class Element(Item):
    u"""The leaf variant of ITEM, to which a DATA_VALUE instance is attached."""
 
    implements(IElement)
    
    def __init__(self,value,nullFlavor,**kwargs):
        self.value=value
        self.nullFlavor=nullFlavor

    
    def isNull():
        u"""Return True if value is unknown, etc."""
        
    def nullFlavorValid(obj):
        u"""If value is None then nullFlavor must be in the terminology code set for null flavors."""
        
          
