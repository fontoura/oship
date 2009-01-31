# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__contributors__= u'Otavio Silva otavio_uff104@yahoo.com.br', u'Sergio Miranda Freire sergio@lampada.uerj.br'
__docformat__ = u'plaintext'

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Int,Bool
from dvquantified import IDvQuantified

_ = MessageFactory('oship')
 

class IDvAmount(IDvQuantified):
    """   
    Abstract class defining the concept of relative quantified amounts. For relative
    quantities, the + and - operators are defined (unlike descendants of
    DV_ABSOLUTE_QUANTITY, such as the date/time types).
    """

    accuracy = Int(
        title=_(u"accuracy"),
        description=_(u"""Accuracy of measurement, expressed either as a half-range 
                         percent value (accuracyIsPercent = True) or a half-range
                         quantity. A value of 0 means that accuracy was not recorded."""),
        required=False
    )

  
    accuracyIsPercent = Bool(
        title=_(u"accuracyIsPercent"),
        description=_(u"""If True, indicates that when this object was created, accuracy was recorded 
                    as a percent value; if False, as an absolute quantity value."""),
        required=False
    )

    
    def validPercentage(val):
        """
        Test whether a number is a valid percentage,i.e. between 0 and 100.
        ensure
        Result implies val >= 0.0 and val <= 100.0
        """

    def __add__(val):
        """
        Sum of this quantity and another whose formal type must be the 
        difference type of this quantity
        """
        
    def __sub__(val):
        """
        Difference of this quantity and another whose formal type must be the 
        difference type of this quantity
        """

    def negate():
        """
        Negated version of current object, such as used for representing a
        difference type of this quantity
        """

        