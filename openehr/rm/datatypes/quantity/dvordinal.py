# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__cotribuitors__=u'Sergio Miranda Freire <serio@lampada.uerj.br>', 'Otavio Silva <otavio_uff104@yahoo.com.br>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements
from oship.openehr.rm.datatypes.quantity.dvordered import DvOrdered
from oship.openehr.rm.datatypes.quantity.interfaces.dvordinal import IDvOrdinal

_ = MessageFactory(u'oship')
        
class DvOrdinal(DvOrdered):
    u"""
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
    
    def __init__(self,value,symbol, normalRange, otherReferenceRanges, normalStatus):
        self.value=value
        self.symbol=symbol
        self.normalRange = normalRange
        self.otherReferenceRanges = otherReferenceRanges
        self.normalStatus = normalStatus
        
        index=False
        for e in otherReferenceRanges:
            if e.meaning.value=='limits':
                index=True
                limitsRange=e
                break
        
        if index==False:
            raise ValueError("No limits in otherReferenceRanges")

        if symbol is None:
            raise ValueError("No symbol")
            
    def limits():
        u"""
        
        """
        return limitsRange
    
    def compareTo(self, dvOrdinal):

        if type (dvOrdinal) != type(self):
            raise TypeError ("Not possible to compare")
        if self.value < dvOrdinal.value:
            return True
        else:
            return False
        
            
                
            
        

    def isStrictlyComparableTo(self, other):
        u"""        
        True if symbols come from same vocabulary,assuming the vocabulary is a 
        subset or value range, e.g. "urine:protein".
        
        (other: like Current): Boolean 
        ensure
        symbol.is_comparable (other.symbol) implies Result
        """
