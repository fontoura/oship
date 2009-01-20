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

from oship.openehr.rm.support.identification.uidbasedid import UidBasedId
from oship.openehr.rm.support.identification.versiontreeid import VersionTreeId
from oship.openehr.rm.support.identification.hierobjectid import HierObjectId
from oship.openehr.rm.support.identification.uuid import Uuid
from oship.openehr.rm.support.identification.internetid import InternetId
from oship.openehr.rm.support.identification.isooid import IsoOid
from oship.openehr.rm.support.identification.objectversionid import ObjectVersionId
import unittest

class ObjectVersionIdTest(unittest.TestCase):


    def tearDown(self):
        self.instance = None

    def testInitializer(self):
        ids1 = [ ['1.4.4.5', '1.2.840.114.1.2.2::123', '1'], \
                 ['1.2.4.5', '7234-235-422-4-23::2', '2.0.0'], \
                 ['1.6.1.6', 'openehr.org::0.99', '2.1.2'] ]

        for id in ids1:
            ov =  ObjectVersionId(id[0] + '::' + id[1] + '::' + id[2])
            self.assertEqual( IsoOid(id[0]), ov.objectId())
            self.assertEqual( HierObjectId(id[1]), ov.creatingSystemId())
            self.assertEqual( VersionTreeId(id[2]), ov.versionTreeId())            

        ids2 = [ ['1-4-4-5-12', '1.2.840.114.1.2.2', '1'], \
                 ['12-14-1-1-9', '7234-235-422-4-23::23', '2.0.0'], \
                 ['1123-1-4-5457-7', 'openehr.org', '2.1.2'] ]
        for id in ids2:
            ov =  ObjectVersionId(id[0] + '::' + id[1] + '::' + id[2])
            self.assertEqual(Uuid(id[0]), ov.objectId())
            self.assertEqual(HierObjectId(id[1]), ov.creatingSystemId())
            self.assertEqual(VersionTreeId(id[2]), ov.versionTreeId())            

        ids3 = [ ['openehr', '1.2.840.114.1.2.2', '1'],  \
                 ['openehrR1_0.org', '7234-235-422-4-23::23', '2.0.0'] ]
        for id in ids3:
            ov =  ObjectVersionId(id[0] + '::' + id[1] + '::' + id[2])
            self.assertEqual(InternetId(id[0]), ov.objectId())
            self.assertEqual(HierObjectId(id[1]), ov.creatingSystemId())
            self.assertEqual(VersionTreeId(id[2]), ov.versionTreeId())            

    def testCreateWithValidUIdInHexFormat(self):
        value = '939cec48-d629-4a3f-89f1-28c573387680::' + '10aec661-5458-4ff6-8e63-c2265537196d::1'
        try:
            ObjectVersionId(value)
        except ValueError:
            self.fail('exception raised by constructor: ')

if __name__ == '__main__':
    unittest.main()
