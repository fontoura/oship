# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
The archetypes interfaces. 
From the archetype object model specification Rev 2.0.1
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.interface import Interface 
from zope.schema import Int
from zope.schema.interfaces import IField
from zope.i18nmessageid.message import MessageFactory

_ = MessageFactory('oship')

        
class IValidityKind(IField):
    """
    An enumeration of three values which may commonly occur in constrint models.
    Use to indicate the validity of date/Time fields etc.
    
    
    #constants
    mandatory=1001
    optional=1002
    disallowed=1003
    """
    value=Int(
        title=_(u"Value"),
        description=_(u"Actual value."),
        required=True,
    )

    def validValidity():
        """
        Test if value is == to one of the constants.
        """
        

        
    

    