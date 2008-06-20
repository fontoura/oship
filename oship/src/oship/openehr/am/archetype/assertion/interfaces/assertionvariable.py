# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
From the assertion package defined in 
The Archetype Object model Rev 2.0.2 
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements
from zope.schema import TextLine, Field
from zope.schema.interfaces import IField


class IAssertionVariable(IField):
    """
    Definition of named variable.
    """
    
    name=TextLine(
        title_(u"Name"),
        description=_(u"Name of variable."),
        required=True,
    )

    definition=TextLine(
        title_(u"Definition"),
        description=_(u"Formal definition of variable."),
        required=True,
    )

class AssertionVariable(Field):
    """
    Definition of named variable.
    """
    
    implements(IAssertionVariable)
    
    def __init__(self,name,defin,**kw):
        self.name=name
        self.definition=defin
        for n,v in kw.items():
            setattr(self,n,v)
