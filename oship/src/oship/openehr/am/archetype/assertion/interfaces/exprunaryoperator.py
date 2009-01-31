# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.i18nmessageid.message import MessageFactory
from zope.schema import Object 

from oship.openehr.am.archetype.assertion.interfaces.exproperator import IExprOperator
from oship.openehr.am.archetype.assertion.interfaces.expritem import IExprItem

_ = MessageFactory('oship')


class IExprUnaryOperator(IExprOperator):
    """
    Unary expression node operator.
    """
    
    operand=Object(
        schema=IExprItem,
        title=_(u"Operand"),
        description=_(u"Operand node."),
        required=True,
    )

