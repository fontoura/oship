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
from zope.interface import implements 

from openehr.rm.common.locatable import ILocatable,Locatable

_ = MessageFactory('oship')

class IItem(ILocatable):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """

class Item(Locatable):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """