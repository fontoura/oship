# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from oship.openehr.rm.common.archetyped.locatable import Locatable

_ = MessageFactory('oship')

class PartyRelationship(Locatable):
    """
    Generic description of a relationship between parties.
    """
    
    pass

    def type():
        """
        Type of relationship such as employment, authority, etc.
        """
 