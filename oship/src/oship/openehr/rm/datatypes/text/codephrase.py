# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
 From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory
from interfaces.codephrase import ICodePhrase

_ = MessageFactory('oship')

class CodePhrase(Field):
    """
    A fully coordinated (i.e. all “coordination” has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    """
    
    implements(ICodePhrase)
    
    def __init__(self, terminologyId, codeString,**kw):
        self.terminologyId=terminologyId
        self.codeString=codeString
        for n,v in kw.items():
            setattr(self,n,v)
