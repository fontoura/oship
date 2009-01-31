# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from oship.openehr.rm.datatypes.quantity.dvamount import DvAmount
from oship.openehr.rm.datatypes.quantity.interfaces.dvcount import IDvCount

_ = MessageFactory(u'oship')


class DvCount(DvAmount):
    u"""        
    Purpose: Countable quantities
         
             Used for countable types such as pregnancies and steps (taken by a physiotherapy
    Use:     patient), number of cigarettes smoked in a day.

    Misuse:  Not used for amounts of physical entities (which all have units)
    """
    
    implements(IDvCount)
    
    def __init__(self, magnitude, accuracy, accuracyIsPercent, magnitudeStatus, normalStatus, normalRange, otherReferenceRanges):
        DvAmount.__init__(accuracy, accuracyIsPercent, magnitudeStatus, normalStatus, normalRange, otherReferenceRanges)
        self.magnitude = magnitude

    def __add__(self, val):
        if type(val) != DvCount:
            raise TypeError("Argument type must be DvCount")
        else:
            return DvCount(self.magnitude + val.magnitude, self.accuracy, self.accuracyIsPercent, self.magnitudeStatus, self.normalStatus, self.normalRange, self.otherReferenceRanges)
        
        
    def __sub__(self, val):
        if type(val) != DvCount:
            raise TypeError("Argument type must be DvCount")
        else:
            return DvCount(self.magnitude - val.magnitude, self.accuracy, self.accuracyIsPercent, self.magnitudeStatus, self.normalStatus, self.normalRange, self.otherReferenceRanges)

    def negate(self):
        return DvCount(-self.magnitude, self.accuracy, self.accuracyIsPercent, self.magnitudeStatus, self.normalStatus, self.normalRange, self.otherReferenceRanges)
        