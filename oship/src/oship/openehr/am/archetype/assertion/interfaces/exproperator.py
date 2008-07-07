# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
These are the interfaces for the assertion package defined in 
The Archetype Object model Rev 2.0.2 
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema import Bool,Object
from zope.i18nmessageid.message import MessageFactory

from expritem import IExprItem
from openehr.am.archetype.assertion.interfaces.operatorkind import IOperatorKind

_ = MessageFactory('oship')


class IExprOperator(IExprItem):
    """
    Abstract parent of operator types.
    """
    
    operator=Object(
        schema=IOperatorKind,
        title=_(u"Operator"),
        description=_(u"Code of the operator."),
        required=True,
    )

    precedenceOverridden=Bool(
        title=_(u"Precedence Overridden"),
        description=_(u"True if natural precedence of operators is overridden in the expression."),
        required=True,
    )

