# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the generic package as described in the 
Common Information Model Rev. 2.1.0 

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.generic.partyproxy import PartyProxy
from interfaces.partyself import IPartySelf

_ = MessageFactory('oship')
    
    
class PartySelf(PartyProxy):
    u"""
    Party proxy representing the subject of the record.
    Used to indicate that the party is the owner of the record. May or may 
    not have external_ref set.
    """
    
    implements(IPartySelf)
    
    pass
 