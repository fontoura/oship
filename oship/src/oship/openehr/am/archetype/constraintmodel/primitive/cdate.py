# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
These are the interfaces for the am.archetype.primitive package defined in 
The Archetype Object model Rev 2.0.2
"""
__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.constraintmodel.cprimitive import CPrimitive
from oship.openehr.am.archetype.constraintmodel.interfaces.cdate import ICDate

_ = MessageFactory('oship')

class CDate(CPrimitive):
    """
    ISO 8601 compatible constraint on instances of Date.
    """
    
    implements(ICDate)
    
    



    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """
