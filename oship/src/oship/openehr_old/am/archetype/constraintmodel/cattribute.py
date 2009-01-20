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

from archetypeconstraint import ArchetypeConstraint
from interfaces.cattribute import ICAttribute
from operator import xor

_ = MessageFactory('oship')

class CAttribute(ArchetypeConstraint):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    implements(ICAttribute)
    
    def __init__(self, rmAttributeName, existence, children,**kw):
        self.rmAttributeName = rmAttributeName
        self.existence = existence
        self.children = children
        for n,v in kw.items():
            setattr(self,n,v)
        
    def rmAttributeNameValid():
        if (self.rmAttributeName != None):
            return self.rmAttributeName != ''
        return self.rmAttributeName == None
    
    def existenceSet():
        if (self.existence != None):
            return self.existence.lower >= 0 and self.existence.upper <= 1
        return self.existence == None
    
    def childrenValidity():
        return xor(issubclass(type(self.children), CObject), self.children != None)
