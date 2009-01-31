# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.interface import implements,classProvides
from zope.schema import Field,Container
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.assertion.interfaces.assertion import IAssertion

_ = MessageFactory('oship')

class Assertion(Container):
    """
    Structural model of a typed first order predicate logic assertion
    in the forma of an expression tree including optional variable definitions.
    """
    
    implements(IAssertion)
    

    def __init__(self,tag,expr,sexpr,var):
        self.tag=tag
        self.expression=expr
        self.stringExpression=sexpr
        self.variables=var
