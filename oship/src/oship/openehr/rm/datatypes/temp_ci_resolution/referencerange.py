# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the quantity data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'restructuredtext'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements 

from openehr.rm.datatypes.dvordered import DvOrdered
from openehr.rm.datatypes.interfaces.ireferencerange import IReferenceRange


_ = MessageFactory('oship')

class ReferenceRange(DvOrdered):
    """
    Defines a named range to be associated with any ORDERED datum. Each such
    range is particular to the patient and context, e.g. sex, age, and any other factor
    which affects ranges.
    May be used to represent normal, therapeutic, dangerous, critical etc ranges.
    """
    
    def __init__(self, meaning, range):
        self.meaning = meaning
        self.range = range


    def isInRange(val):
        """
        Indicates if the value ‘val’ is inside the range
        """
        