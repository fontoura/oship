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

from oship.openehr.minitermserv.simpleterminologyaccess import SimpleTerminologyAccess
from oship.openehr.rm.datatypes.text.codephrase import CodePhrase
from oship.openehr.rm.support.identification.terminologyid import TerminologyId
import unittest

class SimpleTerminologyAccessTest(unittest.TestCase):

    TEST_ID = 'test_id'
    TERMINOLOGY_ID = TerminologyId('test_id')
    LANG1 = 'en'
    LANG2 = 'fr'
    GROUP1_CODES = [ 'code1', 'code2', 'code3' ]
    GROUP1_RUBRICS_EN = [ 'rubric1_en', 'rubric2_en', 'rubric3_en' ]
    GROUP2_CODES = [ 'code4', 'code5' ]
    LANG1_GROUP1_NAME = 'group1_en'
    LANG2_GROUP1_NAME = 'group1_fr'
    LANG1_GROUP2_NAME = 'group2_en'
    LANG2_GROUP2_NAME = 'group2_fr'
    GROUP1_ID = 'group 1'
    GROUP2_ID = 'group 2'

    def setUp(self):
        self.instance = SimpleTerminologyAccess(self.TEST_ID)
        names = {}
        names[self.LANG1] = self.LANG1_GROUP1_NAME
        names[self.LANG2] = self.LANG2_GROUP1_NAME		
        self.instance.addGroup(self.GROUP1_ID, self.GROUP1_CODES, names)
        names.clear()
        names[self.LANG1] = self.LANG1_GROUP2_NAME
        names[self.LANG2] = self.LANG2_GROUP2_NAME		
        self.instance.addGroup(self.GROUP2_ID, self.GROUP2_CODES, names)
        for i in range(len(self.GROUP1_CODES)):		
            self.instance.addRubric(self.LANG1, self.GROUP1_CODES[i], self.GROUP1_RUBRICS_EN[i]);

    def tearDown(self):
        self.instance = None

    def testGetId(self):
        self.assertEquals(self.TEST_ID, self.instance.id())

    def testGetAllCodes(self):
        codes = []
        for c in self.GROUP2_CODES:
            codes.append(CodePhrase(self.TERMINOLOGY_ID, c))
        for c in self.GROUP1_CODES:
            codes.append(CodePhrase(self.TERMINOLOGY_ID, c))
        self.assertEqual(codes, self.instance.allCodes())

    def testGetCodesForGroupIdWithAllValidIds(self):
        codes = []
        for c in self.GROUP1_CODES:
            codes.append(CodePhrase(self.TERMINOLOGY_ID, c))
        self.assertEqual(codes, self.instance.codesForGroupId(self.GROUP1_ID))
        codes = []
        for c in self.GROUP2_CODES:
            codes.append(CodePhrase(self.TERMINOLOGY_ID, c))
        self.assertEqual(codes, self.instance.codesForGroupId(self.GROUP2_ID))

    def testGetCodesForGroup1NameWithTwoLanguages(self):
        codes = []
        for c in self.GROUP1_CODES:
            codes.append(CodePhrase(self.TERMINOLOGY_ID, c))
        self.assertEqual(codes, self.instance.codesForGroupName(self.LANG1_GROUP1_NAME, self.LANG1))
        self.assertEqual(codes, self.instance.codesForGroupName(self.LANG2_GROUP1_NAME, self.LANG2))

    def testGetCodesForGroup2NameWithTwoLanguages(self):
        codes = []
        for c in self.GROUP2_CODES:
            codes.append(CodePhrase(self.TERMINOLOGY_ID, c))
        self.assertEqual(codes, self.instance.codesForGroupName(self.LANG1_GROUP2_NAME, self.LANG1))
        self.assertEqual(codes, self.instance.codesForGroupName(self.LANG2_GROUP2_NAME, self.LANG2))

    def testGetRubricForCodeWithExistingLangCode(self):
        code = 'code1'
        rubric = self.instance.rubricForCode(code, 'en');
        expected = 'rubric1_en'
        self.assertEqual(expected, rubric)

    def testGetRubricForCodeWithNoneExistingLang(self):
        code = 'code1'
        rubric = self.instance.rubricForCode(code, 'zh');
        expected = None
        self.assertEqual(expected, rubric)

    def testGetRubricForCodeWithNoneExistingCode(self):
        code = 'code6'
        rubric = self.instance.rubricForCode(code, 'en');
        expected = None
        self.assertEqual(expected, rubric)

    def testhasCodeForGroupId(self):
        for code in self.GROUP1_CODES:
            codePhrase = CodePhrase(self.TERMINOLOGY_ID, code)
            self.assertEqual(True, self.instance.hasCodeForGroupId(self.GROUP1_ID, codePhrase))

if __name__ == "__main__":
    unittest.main()
