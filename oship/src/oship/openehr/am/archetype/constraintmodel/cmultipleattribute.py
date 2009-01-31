# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>', u'Fabricio Ferracioli <fabricioferracioli@gmail.com>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements

from oship.openehr.am.archetype.constraintmodel.interfaces.cattribute import ICAttribute
from oship.openehr.am.archetype.constraintmodel.interfaces.cmultipleattribute import ICMultipleAttribute

_ = MessageFactory('oship')

class CMultipleAttribute(object):
    """
    Abstract model of constraint on any kind of attribute node.
    """
    
    implements(ICMultipleAttribute,ICAttribute)
    
    def __init__(self, cardinality):
        self.cardinality = cardinality
    
    def members(cobj):
        """
        List of constraints representing members of the container value of this attribute.
        """
        return self.children
    
    def cardinalityValidity():
        return self.cardinality != None
    
    def membersValid():
        if (self.children != None):
            for co in self.children:
                if (issubclass(type(co), CObject) and co.occurrences.upper >= 1):
                    return False
            return True
    