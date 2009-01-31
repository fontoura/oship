# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'

from oship.openehr.rm.support.identification.terminologyid import TerminologyId
import unittest

class TerminologyIdTest(unittest.TestCase):

    SECTIONS = [ ['snomed-ct', ['snomed-ct', '']], [ 'ICD9(1999)', ['ICD9', '1999']] ]
    
    def tearDown(self):
        self.instance = None


    def testConstructor(self):
        for section in self.SECTIONS:
            self.__assertTID(TerminologyId(section[0]), section)

    def  __assertTID(self, tid, section):
        self.assertEqual(section[0], tid.value)
        self.assertEqual(section[1][0], tid.name())
        self.assertEqual(section[1][1], tid.versionId())
        
if __name__ == "__main__":
    unittest.main()
