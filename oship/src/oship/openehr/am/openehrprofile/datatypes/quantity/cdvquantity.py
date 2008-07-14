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

from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from openehr.am.openehrprofile.datatypes.quantity.interfaces.cdvquantity import ICDvQuantity
from openehr.am.archetype.constraintmodel.cdomaintype import CDomainType

_ = MessageFactory('oship')

class CDvQuantity(CDomainType):
    """
    Constrains instances of DvQuantity.
    """
    implements(ICDvQuantity)
    classProvides(ICDvQuantity)
    
    def __init__(self,list,property):
        self.list=list
        self.property=property
        
    

    