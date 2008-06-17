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

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory
from zope.schema import Dict

from openehr.rm.datatypes.dvtext import DvText,IDvText


class IDvCodedText(IDvText):
    """
    A text item whose value must be the rubric from a controlled terminology, the
    key (i.e. the ‘code’) of which is the defining_code attribute. In other words: a
    DV_CODED_TEXT is a combination of a CODE_PHRASE (effectively a code) and
    the rubric of that term, from a terminology service, in the language in which the
    data was authored.
    
    Since DV_CODED_TEXT is a subtype of DV_TEXT, it can be used in place of it,
    effectively allowing the type DV_TEXT to mean “a text item, which may option-
    ally be coded”.

    If the intention is to represent a term code attached in some way to a fragment of
    plain text, DV_CODED_TEXT should not be used; instead use a DV_TEXT and a
    TERM_MAPPING to a CODE_PHRASE.
    """
    
    definingCode = Dict(
        title = _(u"DefiningCode"),
        description = _(u"""The term which the ‘value’ attribute is the
                      defining_code:CODE_PHRASE textual rendition (i.e. rubric) of."""),
        required = True
        )


class DvCodedText(DvText):
    """
    A text item whose value must be the rubric from a controlled terminology, the
    key (i.e. the ‘code’) of which is the defining_code attribute. In other words: a
    DV_CODED_TEXT is a combination of a CODE_PHRASE (effectively a code) and
    the rubric of that term, from a terminology service, in the language in which the
    data was authored.
    
    Since DV_CODED_TEXT is a subtype of DV_TEXT, it can be used in place of it,
    effectively allowing the type DV_TEXT to mean “a text item, which may option-
    ally be coded”.

    If the intention is to represent a term code attached in some way to a fragment of
    plain text, DV_CODED_TEXT should not be used; instead use a DV_TEXT and a
    TERM_MAPPING to a CODE_PHRASE.
    """

    implements(IDvCodedText)
    
    def __init__(self, definingCode):
        self.definingCode=definingCode
