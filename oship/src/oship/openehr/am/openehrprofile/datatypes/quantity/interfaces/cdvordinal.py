# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.am.archetype.constraintmodel.interfaces.cdomaintype import ICDomainType
from oship.openehr.rm.datatypes.quantity.interfaces.dvordinal import IDvOrdinal

_ = MessageFactory('oship')

class ICDvOrdinal(ICDomainType):
    """
    Class specifying constraints on instances of DV_ORDINAL. Custom constrainer type for instances of DV_ORDINAL.
    """
    
    list = Set(
        title=_(u"List"),
        description=_(u"""Set of allowed DV_ORDINALS."""),
        required=True,
        vaue_type=Object(schema=IDvOrdinal),
        )
     
    