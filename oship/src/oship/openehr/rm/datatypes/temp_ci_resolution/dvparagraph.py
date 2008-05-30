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

from openehr.rm.datatypes.interfaces.idvparagraph import IDvParagraph
from openehr.rm.datatypes.datavalue import DataValue
        
class DvParagraph(DataValue):
    """
    A logical composite text value consisting of a series of DV_TEXTs, i.e. plain text
    (optionally coded) potentially with simple formatting, to form a larger tract of
    prose, which may be interpreted for display purposes as a paragraph.
    DV_PARAGRAPH is the standard way for constructing longer text items in summa-
    ries, reports and so on.
    """

    implements(IDvParagraph)    
    
    def __init__(self,items):
        self.items=items                
    
        