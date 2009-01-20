# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>', u'Fabricio Ferracioli <fabricioferracioli@gmail.com>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements
from zope.schema import Field

from oship.openehr.am.archetype.constraintmodel.archetypeconstraint import ArchetypeConstraint

from interfaces.cobject import ICObject

_ = MessageFactory('oship')

class CObject(ArchetypeConstraint):
    """
    Abstract model of constraint on any kind of object node.
    """
    
    implements(ICObject)
    
    def __init__(self, rmTypeName, occurrences, nodeId, parent):
        self.rmTypeName = rmTypeName
        self.occurrences = occurrences
        self.nodeId = nodeId
        self.parent = parent

    def rmTypeNameValid():
        if (self.rmTypeName != None):
            return self.rmTypeName != ''
        return self.rmTypeName == None
    
    def nodeIdValid():
        if (self.nodeId != None):
            return self.nodeId != ''
        return self.rmTypeName == None
    
    def occurrencesValidity():
        if (self.occurrences != None and self.parent != None):
            return not isinstance(parent, CMultipleAttribute) and occurrences.upper <= 1
        return True
    