# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
The text data types interfaces. From the data types specification Rev 2.1.0
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.interface import Interface  
from zope.schema import *
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.basic import *

_ = MessageFactory('oship')



class IDvText(IDataValue):
    """
    A text item, which may contain any amount of legal characters arranged as e.g.
    words, sentences etc (i.e. one DV_TEXT may be more than one word). Visual for-
    matting and hyperlinks may be included.
    A DV_TEXT can be “coded” by adding mappings to it.
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
    
    mappings=Dict(
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
        description = _(u"""A format string of the form “name:value; name:value...”, 
                      e.g. "font-weight : bold; font-family : Arial; font-size : 12pt;". 
                      Values taken from W3C CSS2 properties lists “background” and “font”."""),
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
                      “languages”. Only used when either the text object is 
                      in a different language from the enclosing ENTRY, or  
                      else the text object is being used outside of an ENTRY 
                      or other enclosing structure which indicates the language."""),
        required = False
        )
    
    encoding = Dict(
        title = _(u"Encoding"),
        description = _(u"""Name of character encoding scheme in which this 
                      value is encoded. Coded from openEHR Code Set 
                      “character sets”. Unicode is the default assumption in 
                      openEHR, with UTF-8 being the assumed encoding. 
                      This attribute allows for variations from these assumptions."""),
        required = False
        )         
        
   

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
    
    target = Dict(
        title = _(u"Target"),
        description = _(u"""The target term of the mapping as a CodePhrase."""),
        required = True
        )
    
    match = TextLine(
        title = _(u"Match"),
        description = _(u"""The relative match of the target term with respect to the 
                      mapped text item. 
                      Result meanings:
                          ‘>’: the mapping is to a broader term
                          e.g. orginal text = “arbovirus infection”, 
                          target = “viral infection”
                          
                          ‘=’: the mapping is to a (supposedly)
                          equivalent to the original item

                          ‘<’: the mapping is to a narrower term.
                          e.g. original text = “diabetes”, mapping
                          = “diabetes mellitus”.
                          ‘?’: the kind of mapping is unknown.

                      The first three values are taken from the
                      ISO standards 2788 (“Guide to Establish-
                      ment and development of monolingual the-
                      sauri”) and 5964 (“Guide to Establishment
                      and development of multilingual thesauri”)."""),
        required = True
        )
    
    purpose = Dict(
        title = _(u"Purpose"),
        description = _(u"""Purpose of the mapping e.g. “automated
                      data mining”, “billing”, “interoperability"""),
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
        
    
class ICodePhrase(Interface):
    """
    A fully coordinated (i.e. all “coordination” has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    """
    
    terminologyId = TextLine(
        title = _(u"TerminologyId"),
        description = _(u"""Identifier of the distinct terminology from
                      which the code_string (or its elements) was extracted."""),
        required = True
        )
    
    codeString = TextLine(
        title = _(u"CodeString"),
        description = _(u"""The key used by the terminology service to
                      identify a concept or coordination of concepts.
                      This string is most likely parsable inside the ter-
                      minology service, but nothing can be assumed
                      about its syntax outside that context."""),
        required = True
        )
    


        

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
    

        
class IDvParagraph(IDataValue):
    """
    A logical composite text value consisting of a series of DV_TEXTs, i.e. plain text
    (optionally coded) potentially with simple formatting, to form a larger tract of
    prose, which may be interpreted for display purposes as a paragraph.
    DV_PARAGRAPH is the standard way for constructing longer text items in summa-
    ries, reports and so on.
    """
    
    items = List(
        title = _(u"Items"),
        description = _(u"""Items making up the paragraph, each of which is a text item 
                      (which may have its own formatting, and/or have hyperlinks).
                      The list contents are DvText"""),
        required = True
        )
