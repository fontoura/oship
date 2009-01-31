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

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.am.archetype.constraintmodel.cdomaintype import CDomainType
from oship.openehr.am.openehrprofile.datatypes.quantity.interfaces.cdvordinal import ICDvOrdinal

_ = MessageFactory('oship')

class CDvOrdinal(CDomainType):
    """
    Class specifying constraints on instances of DV_ORDINAL. Custom constrainer type for instances of DV_ORDINAL.
    """
    
    implements(ICDvOrdinal)
    
    
    def __init__(self,list):
        self.list=list
     
     
    