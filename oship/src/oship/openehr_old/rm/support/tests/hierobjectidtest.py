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

from oship.openehr.rm.support.identification.hierobjectid import HierObjectId
import unittest

class HierObjectIdTest(unittest.TestCase):

    SECTIONS = [ ['1.2.840.113554.1.2.2', '345'],
                 ['1-2-840-113554-1', '789'],
                 ['w123.com', '123'],
                 ['1.2.840.113554.1.2.2', ''],
                 ['1-2-840-113554-1', ''],
                 ['w123.com', ''] ]

    STRING_VALUES = [ '1.2.840.113554.1.2.2::345', \
                      '1-2-840-113554-1::789', \
                      'w123.com::123', \
                      '1.2.840.113554.1.2.2', \
                      '1-2-840-113554-1', \
                      'w123.com' ]
    HAS_EXTENSION_VALUES = [ True, True, True, False, False, False ]
    
    def tearDown(self):
        self.instance = None
        
    def testInitializer(self):
        for i, str in enumerate(self.STRING_VALUES):
            self.assertHOID(HierObjectId(str), i)

    def assertHOID(self, hoid, i):
        self.assertEqual(self.STRING_VALUES[i], hoid.value)      
        self.assertEquals(self.SECTIONS[i][0], hoid.root().value);
        self.assertEquals(self.SECTIONS[i][1], hoid.extension());
        self.assertEquals(self.HAS_EXTENSION_VALUES[i], hoid.hasExtension());        
    
if __name__ == '__main__':
    unittest.main()
