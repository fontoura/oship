# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
The text data types. From the data types specification Rev 2.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.idvtext import IDvText
from openehr.rm.datatypes.datavalue import DataValue

class DvText(DataValue):
    """
    A text item, which may contain any amount of legal characters arranged as e.g.
    words, sentences etc (i.e. one DV_TEXT may be more than one word). Visual for-
    matting and hyperlinks may be included.
    A DV_TEXT can be “coded” by adding mappings to it.
    Fragments of text, whether coded or not are used on their own as values, or to
    make up larger tracts of text which may be marked up in some way, eventually
    going to make up paragraphs.
    """

    implements(IDvText)
    
    def __init__(self, value, mappings, formatting, hyperlink, language, encoding):
        self.value = value
        self.mappings = mappings
        self.formatting = formatting
        self.hyperlink = hyperlink
        self.language = language
        self.encoding = encoding
