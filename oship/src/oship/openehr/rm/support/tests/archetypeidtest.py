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

from oship.openehr.rm.support.identification.archetypeid import ArchetypeId
import unittest

class ArchetypeIdTest(unittest.TestCase):

    ARCHETYPEIDS = [ 'openehr-ehr_rm-section.physical_examination.v2', \
                     'openehr-ehr_rm-section.physical_examination-prenatal.v1', \
                     'hl7-rim-act.progress_note.v1', \
                     'openehr-ehr_rm-ENTRY.progress_note-naturopathy.draft' ] 

    SECTIONS = [ ['openehr', 'ehr_rm', 'section', 'physical_examination', None, 'v2'], \
                 ['openehr', 'ehr_rm', 'section', 'physical_examination', 'prenatal', 'v1'], \
                 ['hl7', 'rim', 'act', 'progress_note', None, 'v1'], \
                 ['openehr', 'ehr_rm', 'ENTRY', 'progress_note', 'naturopathy', 'draft'] ]

    AXES = [ ['openehr-ehr_rm-section', 'physical_examination', 'v2'], \
             ['openehr-ehr_rm-section', 'physical_examination-prenatal', 'v1'], \
             ['hl7-rim-act', 'progress_note', 'v1'], \
             ['openehr-ehr_rm-ENTRY', 'progress_note-naturopathy', 'draft'] ]

    def tearDown(self):
        self.instance = None

    def testConstructorTakesStringValue(self):
        for i, name in enumerate (self.ARCHETYPEIDS):
            self.assertArchetypeID(ArchetypeId(name), i);

    def testConstructorWithInvalidValue(self):
        data = [ \
            # rm entity part \
            'openehr-ehr_rm.physical_examination.v2',  # too less sections \
            'openehr-ehr_rm-section-entry.physical_examination-prenatal.v1', # to many sections \
            'openehr.ehr_rm-entry.progress_note-naturopathy.v2', # too many axes \

            # domain concept part
            'openehr-ehr_rm-section.physical+examination.v2', # illegal char \

            # version part
            'hl7-rim-act.progress_note.',  # missing version \
            'openehr-ehr_rm-entry.progress_note-naturopathy' ] # missing version

        for datum in data:            
            self.assertRaises(ValueError,ArchetypeId, datum)

    def testMultipleSpecialisation(self):
        aid = None
        try:
            aid = ArchetypeId('openEHR-EHR-CLUSTER.exam-generic-joint.v1')
            self.assertEqual('joint', aid.specialisation())
        except Exception:
            self.fail('failed to create ArchetypeID with multiple specialisation')


    def assertArchetypeID(self, aid, i):
        self.assertEqual(self.ARCHETYPEIDS[ i ], aid.value)
        self.assertEqual(self.SECTIONS[ i ][ 0 ], aid.rmOriginator())
        self.assertEqual(self.SECTIONS[ i ][ 1 ], aid.rmName())
        self.assertEqual(self.SECTIONS[ i ][ 2 ], aid.rmEntity())
        self.assertEqual(self.SECTIONS[ i ][ 3 ], aid.conceptName())
        self.assertEqual(self.SECTIONS[ i ][ 4 ], aid.specialisation())
        self.assertEqual(self.AXES[ i ][ 0 ], aid.qualifiedRmEntity())
        self.assertEqual(self.AXES[ i ][ 1 ], aid.domainConcept())
        self.assertEqual(self.AXES[ i ][ 2 ], aid.versionId())

if __name__ == '__main__':
    unittest.main()
