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
from zope.interface import implements 

from dvordered import DvOrdered
from interfaces.dvordinal import IDvOrdinal

_ = MessageFactory('oship')
        
class DvOrdinal(DvOrdered):
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

    implements(IDvOrdinal)
    
    def __init__(self,value,symbol):
        self.value=value
        self.symbol=symbol

    def referenceRange():
        """
        limits of the ordinal enumeration, to allow
        comparison of an ordinal value to its limits.
        Returns DvOrdinal.
        """

    def isStrictlyComparableTo(self, other):
        """        
        True if symbols come from same vocabulary,assuming the vocabulary is a 
        subset or value range, e.g. “urine:protein”.
        
        (other: like Current): Boolean 
        ensure
        symbol.is_comparable (other.symbol) implies Result
        """
