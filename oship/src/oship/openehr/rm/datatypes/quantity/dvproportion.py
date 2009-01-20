# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the quantity data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements

from oship.openehr.rm.datatypes.quantity.dvamount import DvAmount
from oship.openehr.rm.datatypes.quantity.interfaces.dvproportion import IDvProportion,IProportionKind

_ = MessageFactory('oship')   
 

class ProportionKind(object):
    """
    Class of enumeration constants defining types of proportion for the
    DV_PROPORTION class.
    """
    def __init__(self):
        self.pkRatio = 0
        self.pkUnitary = 1
        self.pkPercent = 2
        self.pkFraction = 3
        self.pkIntegerFraction = 4

    def validProportionKind(n):
        """
        True if n is one of the defined types.
        """
        return n in (pkRatio,pkUnitary,pkPercent,pkFraction,pkIntegerFraction)
    

class DvProportion(DvAmount,ProportionKind):
    """
              Models a ratio of values, i.e. where the numerator and denominator are both pure
    Purpose:  numbers.
    
              Used for recording titers (e.g. 1:128), concentration ratios, e.g. Na:K (unitary
      Use:    denominator), albumin:creatinine ratio, and percentages, e.g. red cell distirbution
              width (RDW).
        
              Should not be used to represent things like blood pressure which are often written
              using a '/' character, giving the misleading impression that the item is a ratio,
    MisUse:   when in fact it is a structured value. E.g. visual acuity "6/24" is not a ratio.
              Should not be used for formulations.
    """

    implements(IDvProportion)
    
    def __init__(self, numerator, denominator, type, precision):
        if isinstance(numerator, float) or isinstance(numerator, int):
            self.numerator = numerator
        else:
            raise AttributeError, "Invalid numerator value."
        
        if isinstance(denominator, float) or isinstance(denominator,int):
            self.denominator = denominator
        else:
            raise AttributeError, "Invalid denominator value."
        
        if isinstance(type, ProportionKind):
            self.type = type
        else:
            raise AttributeError, "Invalid type value."
        
        if precision != None:
            if isinstance(precision,int):
                self.precision = precision
            else:
                raise AttributeError, "Invalid precision value."
            
            
    def isIntegral():
        """
        True if the numerator and denominator values are integers, i.e. if the precision is 0.
        """
        return isinstance(self.numerator,int) and isinstance(self.denominator,int) 

    def magnitude():
        """
        Effective magnitude represented by ratio.
        Result = numerator / denominator
        """  
        return self.numerator / self.denominator
    
