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

from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory

from dvtext import DvText
from interfaces.dvcodedtext import IDvCodedText

_ = MessageFactory('oship')

class DvCodedText(DvText):
    """
    A text item whose value must be the rubric from a controlled terminology, the
    key (i.e. the 'code') of which is the defining_code attribute. In other words: a
    DV_CODED_TEXT is a combination of a CODE_PHRASE (effectively a code) and
    the rubric of that term, from a terminology service, in the language in which the
    data was authored.
    
    Since DV_CODED_TEXT is a subtype of DV_TEXT, it can be used in place of it,
    effectively allowing the type DV_TEXT to mean "a text item, which may option-
    ally be coded".

    If the intention is to represent a term code attached in some way to a fragment of
    plain text, DV_CODED_TEXT should not be used; instead use a DV_TEXT and a
    TERM_MAPPING to a CODE_PHRASE.
    """

    implements(IDvCodedText)
    classProvides(IDvCodedText)
    
    def __init__(self, definingCode,**kw):
        self.definingCode=definingCode
        for n,v in kw.items():
            setattr(self,n,v)
