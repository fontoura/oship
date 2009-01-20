# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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
from interfaces.capability import ICapability


_ = MessageFactory('oship')

class Capability(Locatable):
    """
    Capability of a role such as ehr modifier, healthcare provider, etc.
    """
    
    implements(ICapability)
    
    def __init__(self,credentials,timeValidity):
        self.credentials=credentials
        self.timeValidity=timeValidity
        
