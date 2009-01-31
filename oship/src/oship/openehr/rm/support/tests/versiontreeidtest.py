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

from oship.openehr.rm.support.identification.versiontreeid import VersionTreeId
import unittest

class VersionTreeIdTest(unittest.TestCase):

    
    def tearDown(self):
        self.instance = None
        
    def testInitializer(self):
        values = [ '1.1.2', '2', '1.3.24', '10', '3.0.0' ]
        intS = [ ['1', '1', '2'], ['2', None, None], ['1', '3', '24'], ['10', None, None], ['3', None, None] ]
        isB = [ True, False, True, False, False ]

        for i, value in enumerate(values):
            vt = VersionTreeId(value)
            bN = intS[i][1]
            bV = intS[i][2]
            self.assertEqual(intS[i][0], vt.trunkVersion())
            self.assertEqual(bN, vt.branchNumber())
            self.assertEqual(bV, vt.branchVersion())
            self.assertEqual(isB[i], vt.isBranch())
    
    def testInitializerFail(self):
        values = [ '1.0.2', '0', '0.3.24', '1.1.0', '0.0.0', '1.1' ]
        for value in values:
            self.assertRaises(ValueError, VersionTreeId, value)
       
    def testIsFirst(self):
        values = ['1', '1.0.0', '1.1.1', '2']
        iF = [True, True, False, False];
        for i, value in enumerate(values):
            self.assertEquals(iF[i], VersionTreeId(value).isFirst())
   
if __name__ == '__main__':
    unittest.main()
