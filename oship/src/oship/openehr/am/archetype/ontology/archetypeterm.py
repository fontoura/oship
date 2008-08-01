# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
From the am.archetype.ontology package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements,classProvides
from zope.schema import Field

from interfaces.archetypeterm import IArchetypeTerm

class ArchetypeTerm(Field):
    """
    Representation of any coded entity in the archetype ontology.
    """
    
    implements(IArchetypeTerm)
    
    def __init__(self,code,items):
        self.code=code
        self.items=items
    
    def keys(set):
        """
        List of all keys used in this term.
        """
