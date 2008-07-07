# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.basic.interfaces.datavalue import IDataValue
from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.rm.datatypes.text.dvcodedtext import DvCodedText

_ = MessageFactory('oship')

class ITermMapping(IDataValue):
    """
    Represents a coded term mapped to a DV_TEXT, and the relative match of the tar-
    get term with respect to the mapped item. Plain or coded text items may appear in
    the EHR for which one or mappings in alternative terminologies are required.
    Mappings are only used to enable computer processing, so they can only be
    instances of DV_CODED_TEXT.
    
    Used for adding classification terms (e.g. adding ICD classifiers to SNOMED
    descriptive terms), or mapping into equivalents in other terminologies (e.g.
    across nursing vocabularies).
    """
    
    target = CodePhrase('','',
        title = _(u"Target"),
        description = _(u"""The target term of the mapping as a CodePhrase."""),
        required = True,
        )
    
    match = TextLine(
        title = _(u"Match"),
        description = _(u"""The relative match of the target term with respect to the 
                      mapped text item. 
                      Result meanings:
                          '>': the mapping is to a broader term
                          e.g. orginal text = "arbovirus infection", 
                          target = "viral infection"
                          
                          '=': the mapping is to a (supposedly)
                          equivalent to the original item

                          '<': the mapping is to a narrower term.
                          e.g. original text = "diabetes", mapping
                          = "diabetes mellitus".
                          '?': the kind of mapping is unknown.

                      The first three values are taken from the
                      ISO standards 2788 ("Guide to Establish-
                      ment and development of monolingual the-
                      sauri") and 5964 ("Guide to Establishment
                      and development of multilingual thesauri")."""),
        required = True
        )
    
    purpose = DvCodedText(
        title = _(u"Purpose"),
        description = _(u"""Purpose of the mapping e.g. "automated
                      data mining", "billing", "interoperability"""),
        required = True
        )
    
    def narrower():
        u"""The mapping is to a narrower term."""
        
    def equivalent():
        u"""The mapping is to an equivalent term."""
        
    def broader():
        u"""The mapping is to a broader term."""
        
    def unknown():
        u"""The kind of mapping is unknown."""
        
    def isValidMatchCode():
        u"""True if match valid."""

