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

from zope.schema import List, TextLine, Object
from zope.schema.interfaces import IContainer 
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.assertion.interfaces.expritem import IExprItem
from oship.openehr.am.archetype.assertion.interfaces.assertionvariable import IAssertionVariable

_ = MessageFactory('oship')


class IAssertion(IContainer):
    """
    Structural model of a typed first order predicate logic assertion
    in the forma of an expression tree including optional variable definitions.
    """
    
    tag=TextLine(
        title=_(u"Tag"),
        description=_(u"Used for differentiating multiple assertions."),
        required=False,
    )

    expression=Object(
        schema=IExprItem,
        title=_(u"Expression"),
        description=_(u"Root of expression tree."),
        required=True,
    )

    stringExpression=TextLine(
        title=_(u"String Expression"),
        description=_(u"String form of expression."),
        required=False,
    )

    variables=List(
        title=_(u"Variables"),
        description=_(u"Variable definitions used in the assertion."),
        required=False,
        value_type=Object(schema=IAssertionVariable),
    )

