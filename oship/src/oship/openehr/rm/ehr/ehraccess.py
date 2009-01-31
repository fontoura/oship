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
from zope.schema import Object,TextLine

from oship.openehr.rm.common.archetyped.locatable import Locatable
from interfaces.ehraccess import IEhrAccess

_ = MessageFactory('oship')

    
class EhrAccess(Locatable):
    """
    EHR-wide access control object. Contains all policies and rules for access to data in this EHR.
    """
        
    implements(IEhrAccess)
    
    def __init__(self,settings,scheme):
        self.settings=settings
        self.scheme=scheme
        
