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

from openehr.rm.datatypes.basic.datavalue import DataValue
from interfaces.dvtext import IDvText

_ = MessageFactory('oship')


class DvText(DataValue):
    """
    A text item, which may contain any amount of legal characters arranged as e.g.
    words, sentences etc (i.e. one DV_TEXT may be more than one word). Visual for-
    matting and hyperlinks may be included.
    A DV_TEXT can be "coded" by adding mappings to it.
    Fragments of text, whether coded or not are used on their own as values, or to
    make up larger tracts of text which may be marked up in some way, eventually
    going to make up paragraphs.
    """

    implements(IDvText)
    
    def __init__(self, value, mappings, formatting, hyperlink, language, encoding,**kw):
        self.value = value
        self.mappings = mappings
        self.formatting = formatting
        self.hyperlink = hyperlink
        self.language = language
        self.encoding = encoding
        self.__name__=''
        for n,v in kw.items():
            setattr(self,n,v)
