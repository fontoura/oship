# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Int,Object

from openehr.rm.datatypes.quantity.interfaces.dvordered import IDvOrdered
from openehr.rm.datatypes.text.interfaces.dvcodedtext import IDvCodedText

_ = MessageFactory('oship')

class IDvOrdinal(IDvOrdered):
    """
    Models rankings and scores, e.g. pain, Apgar values, etc, where there is a)
    implied ordering, b) no implication that the distance between each value is con-
    stant, and c) the total number of values is finite.

    Used for recording any clinical datum which is customarily recorded using sym-
    bolic values. Example: the results on a urinalysis strip, e.g. {neg, trace, +,
    ++, +++} are used for leucocytes, protein, nitrites etc; for non-haemolysed
    blood {neg, trace, moderate}; for haemolysed blood {neg, trace,
    small, moderate, large}.
    """
    
    value = Int(
        title=_(u"value"),
        description=_(u""" Ordinal position in enumeration of values. """),
        required=True
    )
    
    symbol = Object(
        schema=IDvCodedText,
        title=_(u"symbol"),
        description=_(u"""Coded textual representation of this 
                       value in the enumeration, which may be strings made from "+" symbols, 
                       or other enumerations of terms such as "mild", "moderate", "severe",
                       or even the same number series as the values,
                       e.g. "1", "2", "3". Codes come from archetype."""),
        required=True
    )


    def referenceRange():
        """
        limits of the ordinal enumeration, to allow
        comparison of an ordinal value to its limits.
        Returns DvOrdinal.
        """

    def isStrictlyComparableTo(self, other):
        """        
        True if symbols come from same vocabulary,assuming the vocabulary is a 
        subset or value range, e.g. urine:protein.
        
        (other: like Current): Boolean 
        ensure
        symbol.is_comparable (other.symbol) implies Result
        """
        
