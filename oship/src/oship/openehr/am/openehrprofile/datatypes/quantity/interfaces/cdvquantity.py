# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The Archetype Profile quantity package. 
From the openEHR Archetype Profile specifications Rev. 1.0.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import Interface
from zope.schema import List,Object
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.datatypes.text.interfaces.codephrase import ICodePhrase
from oship.openehr.am.archetype.constraintmodel.interfaces.cdomaintype import ICDomainType
from oship.openehr.am.openehrprofile.datatypes.quantity.interfaces.cquantityitem import ICQuantityItem

_ = MessageFactory('oship')

class ICDvQuantity(ICDomainType):
    """
    Constrains instances of DvQuantity.
    """
    
    list = List(
        title=_(u"List"),
        description=_(u"""List of value/unit pairs."""),
        required=False,
        value_type=Object(schema=ICQuantityItem),
        )
    
    property = Object(
        schema=ICodePhrase,
        title=_(u"Property"),
        description=_(u"""Optional constraint of units property."""),
        required=False
        )

    def anyAllowed():
        """True if any DVQuantity instance allowed"""
    