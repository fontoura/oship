# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__= u'Otavio Silva otavio_uff104@yahoo.com.br', u'Sergio Miranda Freire sergio@lampada.uerj.br'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements

from oship.openehr.rm.datatypes.quantity.dvquantified import DvQuantified
from interfaces.dvamount import IDvAmount

_ = MessageFactory(u'oship')
 
class DvAmount(DvQuantified):
    u"""   
    Abstract class defining the concept of relative quantified 'amounts'. For relative
    quantities, the '+' and '-' operators are defined (unlike descendants of
    DV_ABSOLUTE_QUANTITY, such as the date/time types).
    """
    
    implements(IDvAmount)
    
    def __init__(self,accuracy,accuracyIsPercent,magnitudeStatus, normalStatus, normalRange, otherReferenceRanges):
        DvQuantified.__init__(magnitudeStatus, normalStatus, normalRange, otherReferenceRanges)
        self.accuracy=accuracy
        self.accuracyIsPercent=accuracyIsPercent
    
    def validPercentage(val):
        u"""
        Test whether a number is a valid percentage,i.e. between 0 and 100.
        ensure
        Result implies val >= 0.0 and val <= 100.0
        """
        
        return val>=0 and val<=100
    
    