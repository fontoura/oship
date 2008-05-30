# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
The text data types. From the data types specification Rev 2.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.icodephrase import ICodePhrase

class CodePhrase(Field):
    """
    A fully coordinated (i.e. all “coordination” has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    """
    
    implements(ICodePhrase)
    
    def __init__(self, terminologyId, codeString,**kw):
    #def __init__(self, terminologyId, codeString):
        self.terminologyId=terminologyId
        self.codeString=codeString
        super(CodePhrase, self).__init__(**kw)
