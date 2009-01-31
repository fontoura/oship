# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

From the Data Structures Information Model
 Representation Package Rev. 2.1.0.

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__contributors__= u'Sergio Miranda Freire sergio@lampada.uerj.br'
__docformat__ = u'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements 
from zope.schema import List,Object

from oship.openehr.rm.datastructures.itemstructure.representation.interfaces.item import IItem

_ = MessageFactory('oship')

class ICluster(IItem):
    u"""
    The grouping variant of ITEM, which may contain further instances of ITEM, in an ordered list.
    """
    
    # the list contents should be restricted to schema = IItem,
    items = List(
        value_type=Object(schema=IItem),
        title=_(u"items"),
        description=_(u"""Ordered list of items - CLUSTER or ELEMENT objects - under this CLUSTER."""),
        required=True
    )
