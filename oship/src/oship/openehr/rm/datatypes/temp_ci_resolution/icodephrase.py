# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
The text data types interfaces. From the data types specification Rev 2.1.0
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'



from zope.schema.interfaces import IField  
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.idatavalue import IDataValue

_ = MessageFactory('oship')

class ICodePhrase(IField):
    """
    A fully coordinated (i.e. all “coordination” has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    """
    
    terminologyId = TextLine(
        title = _(u"TerminologyId"),
        description = _(u"""Identifier of the distinct terminology from
                      which the code_string (or its elements) was extracted."""),
        required = True
        )
    
    codeString = TextLine(
        title = _(u"CodeString"),
        description = _(u"""The key used by the terminology service to
                      identify a concept or coordination of concepts.
                      This string is most likely parsable inside the ter-
                      minology service, but nothing can be assumed
                      about its syntax outside that context."""),
        required = True
        )
