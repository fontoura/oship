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

from openehr.minitermserv.simpleterminologyaccess import SimpleTerminologyAccess
from openehr.rm.datatypes.text.codephrase import CodePhrase
from zope.i18nmessageid import MessageFactory
import unittest

_ = MessageFactory('oship')

class SimpleTerminologyAccessTest(unittest.TestCase):
	
	TEST_ID = "test_id";
	LANG1 = "en";
	LANG2 = "fr";
	GROUP1_CODES = [ 'code1', 'code2', 'code3' ]
	GROUP1_RUBRICS_EN = [ 'rubric1_en', 'rubric2_en', 'rubric3_en' ]
	GROUP2_CODES = [ 'code4', 'code5' ]
	LANG1_GROUP1_NAME = 'group1_en'
	LANG2_GROUP1_NAME = 'group1_fr'
	LANG1_GROUP2_NAME = 'group2_en'
	LANG2_GROUP2_NAME = 'group2_fr'
	GROUP1_ID = 'group 1';
	GROUP2_ID = 'group 2';
	
	def setUp(self):
		self.instance = SimpleTerminologyAccess(TEST_ID)
		names = {}
		names[LANG1] = LANG1_GROUP1_NAME
		names[LANG2] = LANG2_GROUP1_NAME		
		self.instance.addGroup(GROUP1_ID, GROUP1_CODES, names)
		names.clear()
		names[LANG1] = LANG1_GROUP2_NAME
		names[LANG2] = LANG2_GROUP2_NAME		
		self.instance.addGroup(GROUP2_ID, GROUP2_CODES, names)
		for i in range(len(GROUP1_CODES)):		
			self.instance.addRubric(LANG1, GROUP1_CODES[i], GROUP1_RUBRICS_EN[i]);
	
	def tearDown(self):
		self.instance = None
	
	def testGetId(self):
		assertEquals(TEST_ID, instance.id())

	def testGetAllCodes(self):
		codes = []
		for c in GROUP1_CODES:
			codes.append(CodePhrase(TEST_ID, c))
		for c in GROUP2_CODES:
			codes.append(CodePhrase(TEST_ID, c))
		assertEqual(codes, self.instance.allCodes())

	def testGetCodesForGroupIdWithAllValidIds(self):
		codes = []
		for c in GROUP1_CODES:
			codes.append(CodePhrase(TEST_ID, c))
		assertEqual(codes, self.instance.codesForGroupId(GROUP1_ID))
		codes.clear()
		for c in GROUP2_CODES:
			codes.append(CodePhrase(TEST_ID, c))
		assertEqual(codes, self.instance.codesForGroupId(GROUP2_ID))

	def testGetCodesForGroup1NameWithTwoLanguages(self):
		codes = []
		for c in GROUP1_CODES:
			codes.append(CodePhrase(TEST_ID, c))
		assertEqual(codes, self.instance.codesForGroupName(LANG1_GROUP1_NAME, LANG1))
		assertEqual(codes, self.instance.codesForGroupName(LANG2_GROUP1_NAME, LANG2))
	
	def testGetCodesForGroup2NameWithTwoLanguages(self):
		codes = []
		for c in GROUP2_CODES:
			codes.append(CodePhrase(TEST_ID, c))
		assertEqual(codes, self.instance.codesForGroupName(LANG1_GROUP2_NAME, LANG1))
		assertEqual(codes, self.instance.codesForGroupName(LANG2_GROUP2_NAME, LANG2))

	def testGetRubricForCodeWithExistingLangCode(self):
		code = 'code1'
		rubric = self.instance.rubricForCode(code, 'en');
		expected = 'rubric1_en'
		assertEqual(expected, rubric)
	
	def testGetRubricForCodeWithNoneExistingLang(self):
		code = 'code1'
		rubric = self.instance.rubricForCode(code, 'zh');
		expected = None
		assertEqual(expected, rubric)
	
	def testGetRubricForCodeWithNoneExistingCode(self):
		code = 'code6'
		rubric = self.instance.rubricForCode(code, 'en');
		expected = None
		assertEqual(expected, rubric)
	
	def testhasCodeForGroupId(self):
		for code in GROUP1_CODES:
			codePhrase = CodePhrase(TEST_ID, code)
			assertEqual(True, self.instance.hasCodeForGroupId(GROUP1_ID, codePhrase))

if __name__ = "__main__":
	unittest.main()
		
