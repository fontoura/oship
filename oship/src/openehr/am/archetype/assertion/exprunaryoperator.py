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

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.assertion.exproperator import ExprOperator
from oship.openehr.am.archetype.assertion.interfaces.exprunaryoperator import IExprUnaryOperator

_ = MessageFactory('oship')

class ExprUnaryOperator(ExprOperator):
    """
    Unary expression node operator.
    """
    
    implements(IExprUnaryOperator)
