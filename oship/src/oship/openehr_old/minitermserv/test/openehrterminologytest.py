# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'

import sys
from oship.openehr.rm.support.terminology.openehrcodesetidentifiers import OpenehrCodeSetIdentifiers
from oship.openehr.minitermserv.simpleterminologyservice import SimpleTerminologyService
from oship.openehr.rm.datatypes.text.codephrase import CodePhrase
from oship.openehr.rm.support.identification.terminologyid import TerminologyId
import unittest

class OpenEHRTerminologyTest(unittest.TestCase):

    def setUp(self):
        self.service = SimpleTerminologyService()

    def testHasOpenEHRSettingCode(self):		
        terminology = self.service.terminologies['openehr']	
        self.assertEqual(False, terminology is None)		
        codes = terminology.codesForGroupName('setting', 'en')		
        self.assertEqual(False, codes is None)		
        home = CodePhrase(TerminologyId('openehr'), '225')		
        self.assertEqual(True, home in codes)

    def testHasCountryCodes(self):
        codeSetAccess = self.service.codeSetForId('countries')
        terminologyId = TerminologyId('ISO_3166-1')
        self.assertEqual(False, codeSetAccess is None)
        self.assertEqual(True, codeSetAccess.hasCode(CodePhrase(terminologyId, 'CN')))
        self.assertEqual(True, codeSetAccess.hasCode(CodePhrase(terminologyId, 'SE')))
        self.assertEqual(True, codeSetAccess.hasCode(CodePhrase(terminologyId, 'GB')))
        self.assertEqual(True, codeSetAccess.hasCode(CodePhrase(terminologyId, 'DK')))
        self.assertEqual(True, codeSetAccess.hasCode(CodePhrase(terminologyId, 'FR')))

if __name__ == "__main__":
    unittest.main()
