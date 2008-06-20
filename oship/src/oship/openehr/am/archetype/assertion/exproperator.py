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

from zope.interface import Interface
from zope.schema import Text, TextLine, Field


class IExprOperator(IExprItem):
    """
    Abstract parent of operator types.
    """
    
    operator=OperatorKind(
        title_("Operator"),
        description=_("Code of the operator"),
        required=True,
    )

    precedenceOverridden=Bool(
        title_("Precedence Overridden"),
        description=_("True if natural precedence of operators is overrriden in teh expression."),
        required=True,
    )

class ExprOperator(ExprItem):
    """
    Abstract parent of operator types.
    """
    
    implements(IExprOperator)
    
