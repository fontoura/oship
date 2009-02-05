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
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'


from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.am.archetype.interfaces.validitykind import IValidityKind

_ = MessageFactory('oship')


class ValidityKind(object):
    """
    An enumeration of three values which may commonly occur in constrint models.
    Use to indicate the validity of date/Time fields etc.
    
    """
    implements(IValidityKind)
     
    constants={'mandatory':1001,'optional':1002,'disallowed':1003}

    def validValidity():
        """
        Test if value is == to one of the constants.
        """
