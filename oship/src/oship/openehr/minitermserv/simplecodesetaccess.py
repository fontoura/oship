# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

This is a simple in-memory implementation of CodeSetAccess .

"""


__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements
from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.rm.support.terminology.codesetaccess import CodeSetAccess
from openehr.rm.support.identification.terminologyid import TerminologyId

_ = MessageFactory('oship')

class SimpleCodeSetAccess():
    """
    A simple in-memory implementation of CodeSetAccess.
    """

    implements(CodeSetAccess)

    def __init__(self, id, allCodes):
        self.identifier = id;
        terminologyId = TerminologyId(id)
        self.codes = []
        for code in allCodes:
            codePhrase = CodePhrase(terminologyId, code)
            self.codes.append(codePhrase)	

    def id(self):
        u"""External identifier of this Code Set"""
        return self.identifier

    def allCodes(self):
        u""" Return all codes known in this code set """
        return self.codes

    def hasLang(self, a_lang):
        u""" True if code set knows about 'a_lang'.
		  TODO: seems to be impossible to implement
	      code sets are language _independent_ by definition
		"""
        return false

    def hasCode(self, a_code):
        u""" True if code set knows about 'a_code' """
        if(a_code is None):
            raise ValueError(u'code is null')   
        if a_code.__class__ is not CodePhrase:    
            raise TypeError(u'a_code is not a Code Phrase')
        return a_code in self.codes
