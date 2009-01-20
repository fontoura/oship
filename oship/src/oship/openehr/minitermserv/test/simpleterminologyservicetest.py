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


from oship.openehr.rm.support.terminology.openehrcodesetidentifiers import OpenehrCodeSetIdentifiers
from oship.openehr.minitermserv.simpleterminologyservice import SimpleTerminologyService
import unittest

class SimpleTerminologyServiceTest(unittest.TestCase):

    def setUp(self):
        self.instance = SimpleTerminologyService()

    def tearDown(self):
        self.instance = None

    def testGetTerminology(self):
        terminology = self.instance.terminology('openehr')
        self.assertEqual(terminology is None, False)

    def testGetCodeSetWithAllValidIds(self):
        for id in OpenehrCodeSetIdentifiers.values:
            codeSet = self.instance.codeSetForId(id);
            self.assertEqual(False, codeSet is None)

    def testHasTerminologyWithOpenEHR(self):
        name = 'openehr'
        self.assertEqual(True, self.instance.hasTerminology(name))

    def testHasCodeSet(self):
        for id in OpenehrCodeSetIdentifiers.values:
            self.assertEqual(True, self.instance.hasCodeSet(id))		

    def testGetTerminologyIdentifiers(self):
        ids = self.instance.terminologyIdentifiers()
        self.assertEqual(False, ids is None)
        self.assertEqual(True, len(ids) > 0)

    def testGetCodeSetIdentifiers(self):
        ids = self.instance.codeSetIdentifiers()
        self.assertEqual(False, ids is None)
        self.assertEqual(True, len(ids) > 0)

    def testGetOpenehrCodeSets(self):
        codeSets = self.instance.openehrCodeSets()
        self.assertEqual(False, codeSets is None)
        self.assertEqual(True, len(codeSets) > 0)

    def testGetCountryCodeSetByExternalName(self):
        externalNames = [
            'ISO_3166-1', 'IANA_character-sets', 
            'openehr_compression_algorithms', 
            'openehr_integrity_check_algorithms',
            'ISO_639-1', 'IANA_media-types',
            'openehr_normal_statuses' ]

        for name in externalNames:
            codeSet = self.instance.codeSet(name)
            self.assertEqual(False, codeSet is None)

if __name__ == "__main__":
    unittest.main()
