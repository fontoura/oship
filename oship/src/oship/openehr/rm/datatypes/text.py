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
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.basic import DataValue
from openehr.rm.datatypes.interfaces.text import *




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
    
    def __init__(self, value, mappings, formatting, hyperlink, language, encoding,**kwargs):
        self.value = value
        self.mappings = mappings
        self.formatting = formatting
        self.hyperlink = hyperlink
        self.language = language
        self.encoding = encoding
        Field.__init__(self,**kwargs)


class TermMapping(Field):
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

    implements(ITermMapping)
    
    def __init__(self,target,match,purpose,**kwargs):
        self.target = target       
        self.purpose = purpose
        if match in ['<','>','=','?']:
            self.match = match
        else:
            raise AttributeError, "Invalid match parameter"
        Field.__init__(self,**kwargs)

        
    def narrower():
        return self.match == '<'
    
    def equivalent():
        return self.match == '='
    
    def broader():
        return self.match == '>'
    
    def unknown():
        return self.match == '?'
    
    def isValidMatchCode():
        " I see no purpose in this function. twc"
        return match in ['<','>','=','?']

    
class CodePhrase(Field):
    """
    A fully coordinated (i.e. all “coordination” has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    """
    
    implements(ICodePhrase)
    
    def __init__(self,terminologyId,codeString,**kwargs):
        self.terminologyId=terminologyId
        self.codeString=codeString
        Field.__init__(self,**kwargs)
        

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
    
    def __init__(self, definingCode,**kwargs):
        self.definingCode = definingCode
        Field.__init__(self,**kwargs)

        
class DvParagraph(DataValue):
    """
    A logical composite text value consisting of a series of DV_TEXTs, i.e. plain text
    (optionally coded) potentially with simple formatting, to form a larger tract of
    prose, which may be interpreted for display purposes as a paragraph.
    DV_PARAGRAPH is the standard way for constructing longer text items in summa-
    ries, reports and so on.
    """

    implements(IDvParagraph)    
    
    def __init__(self,items,**kwargs):
        self.items=items                
        Field.__init__(self,**kwargs)

        
 