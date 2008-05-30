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

from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.interfaces.idvamount import IDvAmount 


_ = MessageFactory('oship')

class IDvCount(IDvAmount):
    """        
    Purpose: Countable quantities
         
             Used for countable types such as pregnancies and steps (taken by a physiotherapy
    Use:     patient), number of cigarettes smoked in a day.

    Misuse:  Not used for amounts of physical entities (which all have units)
    """
    
    magnitude = Int(
        title=_(u"Magnitude"),
        description=_(u"""numeric magnitude of the quantity"""),
        required=True
        )
