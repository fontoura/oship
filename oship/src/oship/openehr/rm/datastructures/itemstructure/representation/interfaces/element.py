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
from zope.schema import Field,Object

from openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText
from openehr.rm.datastructures.itemstructure.representation.interfaces.item import IItem

_ = MessageFactory('oship')
    
class IElement(IItem):
    u"""The leaf variant of ITEM, to which a DATA_VALUE instance is attached."""
    
    value = Field(
        title=_(u"value"),
        description=_(u"""Data value of this leaf."""),
        required=False
    )
    
    nullFlavor = Object(
        schema=IDvCodedText,
        title=_(u"""nullFlavor"""),
        description=_(u"""Flavor of null value, e.g. 'indeterminate', 'not asked', etc."""),
        required=False
    )
    
    def isNull():
        u"""Return True if value is unknown, etc."""
        
    def nullFlavorValid(obj):
        u"""If value is None then nullFlavor must be in the terminology code set for null flavors."""
        
