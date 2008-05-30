# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################
"""

These are the quantity data types interfaces from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.interfaces.idvamount import IDvAmount 


_ = MessageFactory('oship')
    
class IProportionKind(Interface):
    """
    Class of enumeration constants defining types of proportion for the
    DV_PROPORTION class.
    """


    def validProportionKind(n):
        """
        True if n is one of the defined types.
        """
        
    
class IDvProportion(IDvAmount):
    """
              Models a ratio of values, i.e. where the numerator and denominator are both pure
    Purpose:  numbers.
    
              Used for recording titers (e.g. 1:128), concentration ratios, e.g. Na:K (unitary
      Use:    denominator), albumin:creatinine ratio, and percentages, e.g. red cell distirbution
              width (RDW).
        
              Should not be used to represent things like blood pressure which are often written
              using a / character, giving the misleading impression that the item is a ratio,
    MisUse:   when in fact it is a structured value. E.g. visual acuity 6/24 is not a ratio.
              Should not be used for formulations.
    """
    
    
    numerator = Float(
        title=_(u"numerator"),
        description=_(u"""numerator of ratio"""),
        required=True
    )
    
    denominator = Float(
        title=_(u"denominator"),
        description=_(u"""denominator of ratio"""),
        required=True
    )
    
    type = Int(
        title=_(u"type"),
        description=_(u"""Indicates semantic type of proportion, including percent, unitary etc."""),
        required=True
    )
    
    precision = Int(
        title=_(u"precision"),
        description=_(u"""Precision to which the numerator and denominator values of the proportion 
                    are expressed, in terms of number of decimal places. The value 0 implies an 
                    integral quantity. The value -1 implies no limit, i.e.any number of decimal places."""),
        required=False
    )
    
    
    def isIntegral():
        """
        True if the numerator and denominator values are integers, i.e. if the precision is 0.
        """

    def magnitude():
        """
        Effective magnitude represented by ratio.
        Result = numerator / denominator
        """  
    
 