# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
 From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__contributors__= u'Sergio Miranda Freire sergio@lampada.uerj.br'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.datatypes.text.interfaces.codephrase import ICodePhrase

_ = MessageFactory('oship')

class CodePhrase(object):
    """
    A fully coordinated (i.e. all "coordination" has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    """
    
    implements(ICodePhrase)
    
    def __init__(self, terminologyId, codeString):
        self.terminologyId=terminologyId
        self.codeString=codeString

        
    def __eq__(self, other):
        if  not isinstance(other, CodePhrase):
            return False
        if self.codeString != other.codeString:
            return False
        return self.terminologyId == other.terminologyId

