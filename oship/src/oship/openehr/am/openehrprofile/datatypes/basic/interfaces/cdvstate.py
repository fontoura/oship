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

from zope.schema import Object
from zope.i18nmessageid.message import MessageFactory 

from openehr.am.archetype.constraintmodel.interfaces.cdomaintype import ICDomainType
from openehr.am.openehrprofile.datatypes.basic.interfaces.statemachine import IStateMachine

_ = MessageFactory('oship')

class ICDvState(ICDomainType):
    """
    Constrainer type for DV_STATE instances. The attribute c_value defines a
    state/event table which constrains the allowed values of the attribute value in a
    DV_STATE instance, as well as the order of transitions between values.
    """
    
    value = Object(
        schema=IStateMachine,
        title=_(u"Value"),
        description=_(u""" """),
        required=True,
        )
    
    
    
    
    
    
    