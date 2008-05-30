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

from zope.interface import Interface
from zope.schema import Text, TextLine, Field


class IAssertion(Interface):
    """
    Structural model of a typed first order predicate logic assertion
    in the forma of an expression tree including optional variable definitions.
    """
    
    tag=TextLine(
        title_("Tag"),
        description=_("Used for differentiating multiple assertions."),
        required=False,
    )

    expression=ExprItem(
        title_("Expression"),
        description=_("Root of expression tree."),
        required=True,
    )

    stringExpression=TextLine(
        title_("String Expression"),
        description=_("String form of expression."),
        required=False,
    )

    variables=List(
        title_("Variables"),
        description=_("Variable definitions used in the assertion."),
        required=False,
    )

        
class IExprItem(Interface):
    """
    Abstract parent of allexpression tree items.
    """
    
    type=TextLine(
        title_("Type"),
        description=_("Mathematical type name of this expression."),
        required=True,
    )

class IExprLeaf(IExprItem):
    """
    Expression tree, leaf form.
    """
    
    item=Field(
        title_("Item"),
        description=_("The value refered to."),
        required=True,
    )

    referenceType=TextLine(
        title_("Reference Type"),
        description=_("Type of reference: constant, attribute, etc."),
        required=True,
    )

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

    
class IExprUnaryOperator=IExprOperator):
    """
    Unary expression node operator.
    """
    
    operand=ExprItem(
        title_("Operand"),
        description=_("Operand node."),
        required=True,
    )

class IExprBinaryOperator(IExprOperator):
    """
    Binary expression node.
    """
    
    leftOperand=ExprItem(
        title_("Left"),
        description=_("Left operand node."),
        required=True,
    )

    rightOperand=ExprItem(
        title_("Right"),
        description=_("Right operand node."),
        required=True,
    )

class IAssertionVariable(Interface):
    """
    Definition of named variable.
    """
    
    name=TextLine(
        title_("Name"),
        description=_("Name of variable."),
        required=True,
    )

    definition=TextLine(
        title_("Definition"),
        description=_("Formal definition of variable."),
        required=True,
    )

class IOperatorKind(Interface):
    """
    Enumeration of assertion package operator types.
    
    
    #constants
    opEq=2001  #= or ==
    opNe=2002
    opLe=2003
    opLt=2004
    opGe=2005
    opGt=2006
    opMatches=2007
    
    opNot=2010
    opAnd=2011
    opOr=2012
    opXor=2013
    opImplies=2014
    opForAll=2015
    opExists=2016

    opPlus=2020
    opMinus=2021
    opMultiply=2022
    opDivide=2023
    opExp=2024
    """
    
    value=Int(
        title_("Value"),
        description=_("Actual value of this instance."),
        required=True,
    )

    def validOperator(anOp):
        """
        Return True if anOp is a valid operator.
        """
        

    
    
    