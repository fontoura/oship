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

from zope.schema import TextLine,Text,List,Dict,URI
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.basic.interfaces.datavalue import IDataValue

_ = MessageFactory('oship')

class IDvText(IDataValue):
    """
    A text item, which may contain any amount of legal characters arranged as e.g.
    words, sentences etc (i.e. one DV_TEXT may be more than one word). Visual for-
    matting and hyperlinks may be included.
    A DV_TEXT can be "coded" by adding mappings to it.
    Fragments of text, whether coded or not are used on their own as values, or to
    make up larger tracts of text which may be marked up in some way, eventually
    going to make up paragraphs.
    """
    
    value = TextLine(
        title = _(u"Value"),
        description = _(u"""Displayable rendition of the item, regardless of its 
                      underlying structure. For DV_CODED_TEXT, this is the 
                      rubric of the complete term as provided by the termi- 
                      nology service. No carriage returns, line feeds, or 
                      other non-printing characters permitted."""),
        required=True
    )
    
    mappings=List(
        title = _(u"Mappings"),
        description = _(u"""A list of MappingTerm,terms from other terminologies most closely matching 
                      this term, typically used where the originator (e.g.  
                      pathology lab) of information uses a local terminology 
                      but also supplies one or more equivalents from well- 
                      known terminologies (e.g. LOINC). The list contents should be of the type TermMapping"""),
        required = False
        )
    
    formatting = Text(
        title = _(u"Formatting"),
        description = _(u"""A format string of the form "name:value; name:value...", 
                      e.g. "font-weight : bold; font-family : Arial; font-size : 12pt;". 
                      Values taken from W3C CSS2 properties lists "background" and "font"."""),
        required = False
        )
    
    hyperlink = URI(
        title = _(u"Hyperlink"),
        description = _(u"""Optional link sitting behind a section of plain text or 
                      coded term item as type DvUri."""),
        required = False
        )
    
    language = Dict(
        title = _(u"Language"),
        description = _(u"""Optional indicator of the localised language in which 
                      the value is written. Coded from openEHR Code Set 
                      "languages". Only used when either the text object is 
                      in a different language from the enclosing ENTRY, or  
                      else the text object is being used outside of an ENTRY 
                      or other enclosing structure which indicates the language."""),
        required = False
        )
    
    encoding = Dict(
        title = _(u"Encoding"),
        description = _(u"""Name of character encoding scheme in which this 
                      value is encoded. Coded from openEHR Code Set 
                      "character sets". Unicode is the default assumption in 
                      openEHR, with UTF-8 being the assumed encoding. 
                      This attribute allows for variations from these assumptions."""),
        required = False
        )         
        