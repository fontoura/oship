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

from openehr.rm.common.archetyped.interfaces.locatable import ILocatable

_ = MessageFactory('oship')

class IItem(ILocatable):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """
