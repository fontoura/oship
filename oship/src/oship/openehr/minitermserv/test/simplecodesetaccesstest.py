##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

This is a test unit for a Simple Terminology Service

"""

__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'

from oship.openehr.rm.datatypes.text.codephrase import CodePhrase
from oship.openehr.rm.support.identification.terminologyid import TerminologyId
from oship.openehr.minitermserv.simplecodesetaccess import SimpleCodeSetAccess
import unittest

class SimpleCodeSetAccessTest(unittest.TestCase):

    def setUp(self):
        self.CODESET_ID = 'test_id'
        self.TERMINOLOGY_ID = TerminologyId('test_id')
        self.CODES = ['code1', 'code2', 'code3', 'code4' ]
        self.instance = SimpleCodeSetAccess(self.CODESET_ID, self.CODES)

    def testGetId(self):
        self.assertEqual(self.CODESET_ID, self.instance.id())

    def testGetAllCodes(self):
        allCodes = []
        for c in self.CODES:
            allCodes.append(CodePhrase(self.TERMINOLOGY_ID, c))
        self.assertEqual(allCodes, self.instance.allCodes())

    def testHasCode(self):
        for c in self.CODES:
            code = CodePhrase(self.TERMINOLOGY_ID, c)
            self.assertEqual(True, self.instance.hasCode(code))

if __name__ == "__main__":
    unittest.main()

