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
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.assertion.interfaces.operatorkind import IOperatorKind

_ = MessageFactory('oship')

class OperatorKind(object):
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
