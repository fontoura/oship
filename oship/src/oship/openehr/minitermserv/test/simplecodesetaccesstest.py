##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

This is a test unit for a Simple Terminology Service

"""

__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.minitermserv.simplecodesetaccess import SimpleCodeSetAccess
import unittest

_ = MessageFactory('oship')

class SimpleCodeSetAccessTest(unittest.TestCase):
	
	CODESET_ID = 'test_id'
	CODES = ['code1', 'code2', 'code3', 'code4' ]

	def setUp(self) {
		self.instance = SimpleCodeSetAccess(CODESET_ID, CODES)
	
	def testGetId(self):
		assertEqual(CODESET_ID, self.instance.id())
	
	def testGetAllCodes(self):
		allCodes = []
		for c in CODES):
			allCodes.append(CodePhrase(CODESET_ID, c))
		assertEqual(allCodes, self.instance.allCodes())
	
	def testHasCode(self):
		for c in CODES:
			code = CodePhrase(CODESET_ID, c)
			assertEqual(True, self.instance.hasCode(code))

if __name__ = "__main__":
	unittest.main()

