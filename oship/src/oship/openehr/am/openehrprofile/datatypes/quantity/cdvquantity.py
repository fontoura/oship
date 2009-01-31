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
__contributors__ = u'Fabricio Ferracioli <fabricioferracioli@gmail.com>'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.am.openehrprofile.datatypes.quantity.interfaces.cdvquantity import ICDvQuantity
from oship.openehr.am.archetype.constraintmodel.cdomaintype import CDomainType
from operator import xor

_ = MessageFactory('oship')

class CDvQuantity(CDomainType):
    """
    Constrains instances of DvQuantity.
    """
    implements(ICDvQuantity)
    
    def __init__(self,list,property):
        self.list=list
        self.property=property
        
    
    def anyAllowed():
        """True if any DVQuantity instance allowed."""
        return self.list == None and self.property == None
    
    def listValid():
        return self.list != None and self.list.__len__() == 0
    
    def overallValidity():
        return xor(self.list != None or self.property != None, self.anyAllowed())