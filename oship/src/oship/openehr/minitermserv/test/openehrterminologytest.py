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
from openehr.rm.support.terminology.openehrcodesetidentifiers import OpenEHRCodeSetIdentifiers
from openehr.minitermserv.simpleterminologyservice import SimpleTerminologyService
from openehr.rm.datatypes.text.codephrase import CodePhrase
import unittest



class OpenEHRTerminologyTest(unittest.TestCase):
	
	def setUp(self):
		self.service = SimpleTerminologyService()
	
	def testHasOpenEHRSettingCode(self):		
		terminology = self.service.terminology('openehr')	
		assertEqual(False, terminology is None)		
		codes = terminology.codesForGroupName('setting', 'en')		
		assertEqual(False, codes is None)		
		home = CodePhrase('openehr', '225')		
		assertEqual(True, home in codes)
	
	def testHasCountryCodes(self):
		codeSet = self.service.codeSetForId('countries')
		assertEqual(False, codeSet is None)
		assertEqual(True, CodePhrase('ISO_3166-1', 'CN') in codeSet)
		assertEqual(True, CodePhrase('ISO_3166-1', 'SE') in codeSet)
		assertEqual(True, CodePhrase('ISO_3166-1', 'GB') in codeSet)
		assertEqual(True, CodePhrase('ISO_3166-1', 'DK') in codeSet)
		assertEqual(True, CodePhrase('ISO_3166-1', 'FR') in codeSet)

	if __name__ == "__main__":
		unittest.main()
	