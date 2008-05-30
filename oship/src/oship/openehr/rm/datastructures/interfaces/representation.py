# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications from Data Structures Information Model
 Representation Package Rev. 2.1.0.

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from oship.openehr.rm.common.interfaces.archetyped import ILocatable
from oship.openehr.rm.datatypes.quantity import *
from oship.openehr.rm.datatypes.text import *

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class IItem(ILocatable):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """

class ICluster(IItem):
    u"""
    The grouping variant of ITEM, which may contain further instances of ITEM, in an ordered list.
    """
    
    items = List(
        title=_(u"""items"""),
        description=_(u"""Ordered list of items - CLUSTER or ELEMENT objects - under this CLUSTER."""),
        required=True
    )
    
class IElement(IItem):
    u"""The leaf variant of ITEM, to which a DATA_VALUE instance is attached."""
    
    value = Field(
        title=_(u"""value"""),
        description=_(u"""Data value of this leaf."""),
        required=False
    )
    
    nullFlavor = DvCodedText('',
        title=_(u"""nullFlavor"""),
        description=_(u"""Flavor of null value, e.g. 'indeterminate', 'not asked', etc."""),
        required=False
    )
    
    def isNull():
        u"""Return True if value is unknown, etc."""
        
    def nullFlavorValid(obj):
        u"""If value is None then nullFlavor must be in the terminology code set for null flavors."""
        
          
