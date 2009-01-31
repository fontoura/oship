# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

These are the interface specifications from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.changecontrol.versionedobject import VersionedObject
from interfaces.versionedehrstatus import IVersionedEhrStatus

_ = MessageFactory('oship')

class VersionedEhrStatus(VersionedObject):
    """
    Version container for the EHR status instance.
    """
    
    implements(IVersionedEhrStatus)
    
    pass

    
