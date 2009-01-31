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

from item import Item
from oship.openehr.rm.datastructures.itemstructure.representation.interfaces.cluster import ICluster

_ = MessageFactory('oship')


class Cluster(Item):
    u"""
    The grouping variant of ITEM, which may contain further instances of ITEM, in an ordered list.
    """

    implements(ICluster)
    
    def __init__(self,uid, archetypeNodeId, name, archetypeDetails, feederAudit, links, items):
        Locatable.__init__(uid, archetypeNodeId, name, archetypeDetails, feederAudit, links)
        self.items=items
          
