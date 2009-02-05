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
__contributors__= u'Sergio Miranda Freire sergio@lampada.uerj.br'
__docformat__ = u'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from oship.openehr.rm.common.archetyped.locatable import Locatable
from oship.openehr.rm.datastructures.itemstructure.representation.interfaces.item import IItem

_ = MessageFactory('oship')

class Item(Locatable):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """
    
    implements(IItem)
    
    def __init__(self, uid, archetypeNodeId, name, archetypeDetails, feederAudit, links):
        Locatable.__init__(uid, archetypeNodeId, name, archetypeDetails, feederAudit, links)