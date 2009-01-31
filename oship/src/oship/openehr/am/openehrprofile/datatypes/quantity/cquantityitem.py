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
__contributors__= u'Sergio Miranda Freire sergio@lampada.uerj.br'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Field 

from oship.openehr.am.openehrprofile.datatypes.quantity.interfaces.cquantityitem import ICQuantityItem

_ = MessageFactory('oship')


class CQuantityItem(object):
    """
    Constrains instances of DvQuantity.
    """
    implements(ICQuantityItem)
    
    def __init__(self,magnitude,precision,units):
        self.magnitude=magnitude
        self.precision=precision
        self.units=units
    
    
    def precisionUnconstrained():       
        """
        True if no constraint on precision; True if precision = -1.
        precision = -1 implies Result
        """
        return precision == -1
    