# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The Archetype Profile basic package. 
From the openEHR Archetype Profile specifications Rev. 1.0.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements

from oship.openehr.am.archetype.constraintmodel.cdomaintype import CDomainType
from oship.openehr.am.openehrprofile.datatypes.basic.interfaces.cdvstate import ICDvState

_ = MessageFactory('oship')

class CDvState(CDomainType):
    u"""
    Constrainer type for DV_STATE instances. The attribute c_value defines a
    state/event table which constrains the allowed values of the attribute value in a
    DV_STATE instance, as well as the order of transitions between values.
    """
    
    implements(ICDvState)
    
    
    def __init__(self,value):
        self.value=value

  
    
    
    
    
    