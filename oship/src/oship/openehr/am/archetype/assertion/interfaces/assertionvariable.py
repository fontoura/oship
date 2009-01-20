# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
From the assertion package defined in 
The Archetype Object model Rev 2.0.2 
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema import TextLine, Field
from zope.interface import Interface
from zope.i18nmessageid.message import MessageFactory

_ = MessageFactory('oship')


class IAssertionVariable(Interface):
    """
    Definition of named variable.
    """
    
    name=TextLine(
        title=_(u"Name"),
        description=_(u"Name of variable."),
        required=True,
    )

    definition=TextLine(
        title=_(u"Definition"),
        description=_(u"Formal definition of variable."),
        required=True,
    )

