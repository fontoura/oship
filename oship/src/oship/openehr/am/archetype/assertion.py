# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
These are the implementations for the assertion package defined in 
The Archetype Object model Rev 2.0.2 
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from openehr.am.archetype.interfaces.assertion import *


class Assertion(Field):
    """
    Structural model of a typed first order predicate logic assertion
    in the forma of an expression tree including optional variable definitions.
    """
    
    implements(IAssertion)
    

        
class ExprItem(Field):
    """
    Abstract parent of allexpression tree items.
    """
    
    implements(IExprItem)
    

class ExprLeaf(ExprItem):
    """
    Expression tree, leaf form.
    """
    
    implements(IExprLeaf)
    

class ExprOperator(ExprItem):
    """
    Abstract parent of operator types.
    """
    
    implements(IExprOperator)
    
    
class ExprUnaryOperator(ExprOperator):
    """
    Unary expression node operator.
    """
    
    implements(IExprUnaryOperator)
    

class ExprBinaryOperator(ExprOperator):
    """
    Binary expression node.
    """
    
    implements(ExprBinaryOperator)
               

class AssertionVariable(Field):
    """
    Definition of named variable.
    """
    
    implements(IAssertionVariable)
    

class OperatorKind(Field):
    """
    Enumeration of assertion package operator types.
    """
    
    implements(IOperatorKind)
    
    constants={'opEq':2001,'opNe':2002,'opLe':2003,'opLt':2004,'opGe':2005,'opGt':2006,'opMatches':2007,\
               'opNot':2010,'opAnd':2011,'opOr':2012,'opXor':2013,'opImplies':2014,'opForAll':2015,\
               'opExists':2016,'opPlus':2020,'opMinus':2021,'opMultiply':2022,'opDivide':2023,'opExp':2024}

    def validOperator(anOp):
        """
        Return True if anOp is a valid operator.
        """
        

    
    
    