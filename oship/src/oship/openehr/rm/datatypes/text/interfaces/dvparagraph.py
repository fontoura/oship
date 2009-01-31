# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.schema import List,Object
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.datatypes.basic.interfaces.datavalue import IDataValue
from oship.openehr.rm.datatypes.text.interfaces.dvtext import IDvText

_ = MessageFactory('oship')

class IDvParagraph(IDataValue):
    """
    A logical composite text value consisting of a series of DV_TEXTs, i.e. plain text
    (optionally coded) potentially with simple formatting, to form a larger tract of
    prose, which may be interpreted for display purposes as a paragraph.
    DV_PARAGRAPH is the standard way for constructing longer text items in summa-
    ries, reports and so on.
    """
    
    items = List(
        value_type=Object(schema=IDvText),
        title = _(u"Items"),
        description = _(u"""Items making up the paragraph, each of which is a text item 
                      (which may have its own formatting, and/or have hyperlinks).
                      The list contents are DvText"""),
        required = True
        )
        
