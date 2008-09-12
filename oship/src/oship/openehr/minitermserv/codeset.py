# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

This class represents CodeSet.

"""

__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'

from zope.schema import Object
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class CodeSet(Object):
    """
    a CodeSet
    """

        def __init__(self, issuer, openehrId, externalId)
            self.issuer =  issuer
            self.openehrId = openehrId
            self.externalId = externalId
            self.codes = []

    def addCode(self, code):
        if code not in codes:
            codes.append(code)