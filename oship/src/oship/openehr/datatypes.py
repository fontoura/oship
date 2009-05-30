# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license. 
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The basic openEHR data types. From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import Interface,implements,providedBy
from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Text,Bool,TextLine,Int,Field,BytesLine,Float,List,URI,Orderable,Choice,Object
from zope.app.file.image import Image
import grok

from support import Interval,ITerminologyId,IObjectRef


_ = MessageFactory('oship')

class ICodePhrase(Interface):
    """
    A fully coordinated (i.e. all "coordination" has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    """
    
    terminologyId = Object(
        schema = ITerminologyId,
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

  
class IDvCodedText(Interface):
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
    
    definingCode = Object(
        schema=ICodePhrase,
        title = _(u"DefiningCode"),
        description = _(u"""The term which the 'value' attribute is the defining_code:CODE_PHRASE textual rendition (i.e. rubric) of."""),
        required = True
        )

class ITermMapping(Interface):
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
    
    target = Object(
        schema=ICodePhrase,
        title = _(u"Target"),
        description = _(u"""The target term of the mapping as a CodePhrase."""),
        required = True
        )
    
    match = TextLine(
        title = _(u"Match"),
        description = _(u"""The relative match of the target term with respect to the mapped text item. Result meanings:'>': the mapping is to a broader term e.g. orginal text = "arbovirus infection", target = "viral infection" '=': the mapping is to a (supposedly) equivalent to the original item '<': the mapping is to a narrower term. e.g. original text = "diabetes", mapping = "diabetes mellitus". '?': the kind of mapping is unknown. The first three values are taken from the ISO standards 2788 ("Guide to Establishment and development of monolingual thesauri") and 5964 ("Guide to Establishment and development of multilingual thesauri")."""),
        required = True
        )
    
    purpose = Object(
        schema=IDvCodedText,
        title = _(u"Purpose"),
        description = _(u"""Purpose of the mapping e.g. "automated data mining", "billing", "interoperability" """),
        required=False
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

class IDvText(Interface):
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
        description = _(u"""Displayable rendition of the item, regardless of its underlying structure. For DV_CODED_TEXT, this is the rubric of the complete term as provided by the terminology service. No carriage returns, line feeds, or other non-printing characters permitted."""),
        required=True
    )
    
    mappings=List(
        value_type=Object(schema=ITermMapping),
        title = _(u"Mappings"),
        description = _(u"""A list of MappingTerm,terms from other terminologies most closely matching this term, typically used where the originator (e.g.   pathology lab) of information uses a local terminology but also supplies one or more equivalents from wellknown terminologies (e.g. LOINC). The list contents should be of the type TermMapping"""),
        required = False,
    )
    
    formatting = Text(
        title = _(u"Formatting"),
        description = _(u"""A format string of the form "name:value; name:value...", e.g. "font-weight : bold; font-family : Arial; font-size : 12pt;". Values taken from W3C CSS2 properties lists "background" and "font"."""),
        required = False
        )
    
    hyperlink = Object(
        schema=IDvUri,
        title = _(u"Hyperlink"),
        description = _(u"""Optional link sitting behind a section of plain text or coded term item as type DvUri."""),
        required = False
        )
    
    language = Object(
        schema = ICodePhrase,
        title = _(u"Language"),
        description = _(u"""Optional indicator of the localised language in which the value is written. Coded from openEHR Code Set "languages". Only used when either the text object is in a different language from the enclosing ENTRY, or else the text object is being used outside of an ENTRY or other enclosing structure which indicates the language."""),
        required = False
        )
    
    encoding = Object(
        schema = ICodePhrase,
        title = _(u"Encoding"),
        description = _(u"""Name of character encoding scheme in which this value is encoded. Coded from openEHR Code Set "character sets". Unicode is the default assumption in openEHR, with UTF-8 being the assumed encoding. This attribute allows for variations from these assumptions."""),
        required = False
        )         
    
class IDvUri(Interface):
    """A reference to an object which conforms to the Universal Resource Identifier
    (URI) standard, as defined by W3C RFC 2936. See "Universal Resource Identifiers in WWW"
    by Tim Berners-Lee at http://www.ietf.org/rfc/rfc2396.txt. This is a World-Wide Web RFC 
    for global identification of resources. See http://www.w3.org/Addressing for a starting 
    point on URIs. See http://www.ietf.org/rfc/rfc2806.txt for new URI types like telephone, 
    fax and modem numbers.
    
    Enables external resources to be referenced from within the content of the EHR. A number 
    of functions return the logical subparts of the URI string."""
    
    value = URI(
        title = _(u"Value"),
        description = _(u"""The URI as a string."""),
        
        )
    
    
    def scheme():
        """A distributed information "space" in which information objects exist. The scheme 
        simultaneously specifies an information space and a mechanism for accessing objects 
        in that space. For example if scheme = "ftp", it identifies the information space in 
        which all ftpable objects exist, and also the application - ftp - which can be used 
        to access them. Values may include: "ftp", "telnet", "mailto", "gopher" and many others. 
        Refer to WWW URI RFC for a full list. New information spaces can be accommodated within 
        the URI specification."""
        
    def path():
        """A string whose format is a function of the scheme. Identifies the location in 
        <scheme>-space of an information entity. Typical values include hierarchical directory 
        paths for any machine. For example, with scheme = "ftp", path might be /pub/images/image_01. 
        The strings "." and ".." are reserved for use in the path. Paths may include internet/intranet 
        location identifiers of the form: sub_domain...domain, e.g. "info.cern.ch" """

    def fragmentId():
        """A part of, a fragment or a sub-function within an object. Allows references to sub-parts 
        of objects, such as a certain line and character position in a text object. The syntax and 
        semantics are defined by the application responsible for the object. """


    def query():
        """Query string to send to application implied by scheme and path Enables queries to 
        applications, including databases to be included in the URI Any query meaningful to the 
        server, including SQL."""
        

    def valueExists():
        """value != None and value != '' """
        

class IDataValue(Interface):
    """
    Serves as a common ancestor of all data value types in openEHR models.
    """

    pass

class DataValue(grok.Model):
    u""" 
    Abstract class. 
    Serves as a common ancestor of all data value types in openEHR models. 
    """
    
    implements(IDataValue)
    pass

class IDvBoolean(Interface):
    """
    Items which are truly boolean data, such as true/false or yes/no answers.
    The invariant defined in the spec for this class is that it is not void.  
    In Python a 'None' is defined as False.
    """
    
    value = Bool(
        title = _(u"value"),
        description = _(u"The boolean value of this item."),
        required = True,
    )
    
class DvBoolean(DataValue):
    """ 
    Items which are truly boolean data, such as true/false or yes/no answers.
    For such data, it is important to devise the meanings (usually questions in subjec-
    tive data) carefully, so that the only allowed results are in fact true or false.
    The DV_BOOLEAN class should not be used as a replacement for naively modelled
    enumerated types such as male/female etc. Such values should be coded, and in
    any case the enumeration often has more than two values.  

    >>> from oship.openehr.datatypes import DvBoolean
    >>> b = DvBoolean(0)
    >>> b.value
    False
    >>> b = DvBoolean(1)
    >>> b.value
    True
    >>> b = DvBoolean(True)
    >>> b.value
    True
    >>> b = DvBoolean(False)
    >>> b.value
    False
    >>> b = DvBoolean(-1)
    >>> b.value
    True
    
    """

    implements(IDvBoolean)

    def __init__(self,value):
        self.value=bool(value)
        if self.value != True and self.value != False:
            raise AttributeError(_("DvBoolean.value True or False."))
        
        
class IDvIdentifier(Interface):
    """
    Type for representing identifiers of real-world entities. Typical identifiers include
    drivers licence number, social security number, veterans affairs number, prescrip-
    tion id, order id, and so on.
    
    DV_IDENTIFIER is used to represent any identifier of a real thing, issued by
    some authority or agency.

    DV_IDENTIFIER is not used to express identifiers generated by the infrastruc-
    ture to refer to information items; the types OBJECT_ID and OBJECT_REF and
    subtypes are defined for this purpose.
    """
    
    issuer = Text(
        title = _(u"Issuer"),
        description = _(u"""Authority which issues the kind of id used in the id field  
                      of this object."""),
        required = True
        )
    
    assignor = Text(
        title = _(u"Assignor"),
        description = _(u"""Organisation that assigned the id to the item being identified."""),
        required = True
        )
    
    id = Text(
        title = _(u"Id"),
        description = _(u""" The identifier value. Often structured, according to the 
                      definition of the issuing authority's rules."""),
        required = True
        )
    
    type = Text(
        title = _(u"Type"),
        description = _(u"""The identifier type, such as "prescription",or "SSN". 
                      One day a controlled vocabulary might be possible for this."""),
        required = True
        )
    

class DvIdentifier(DataValue):
    """
    Type for representing identifiers of real-world entities. Typical identifiers include
    drivers licence number, social security number, vertans affairs number, prescrip-
    tion id, order id, and so on.
    DV_IDENTIFIER is used to represent any identifier of a real thing, issued by
    some authority or agency.
    DV_IDENTIFIER is not used to express identifiers generated by the infrastruc-
    ture to refer to information items; the types OBJECT_ID and OBJECT_REF and
    subtypes are defined for this purpose.
    """

    implements(IDvIdentifier)
    
    def __init__(self, issuer, assignor, id, type):
        self.issuer=issuer
        self.assignor=assignor
        self.id=id
        self.type=type
        
   
class IDvState(Interface):
    """
    For representing state values which obey a defined state machine, such as a vari-
    able representing the states of an instruction or care process.
    
    DV_STATE is expressed as a String but its values are driven by archetype-
    defined state machines. This provides a powerful way of capturing stateful com-
    plex processes in simple data.
    """
    
    value = Object(
        schema=IDvCodedText,
        title = _(u"value"),
        description = _(u"""The state name. State names are determined by a state/event 
                      table defined in archetypes, and coded using openEHR Terminology 
                      or local archetype terms, as specified by the archetype.
                      
                      A module was added to the rm.support package to parse the State 
                      values from the archetype in the current context. This function 
                      is DvStateParser() and it may be called anywhere in the application
                      that the developer needs to know the current available states.
                      It returns a DvCodedText type.
                      """)        
        )
    
    isTerminal = Bool(
        title = _(u"isTerminal"),
        description= _(u"""Indicates whether this state is a terminal
                      state, such as "aborted", "completed" etc
                      from which no further transitions are possible.
                      It is required and the default is False.
                      """),
        
        )
            
    
    
    
class DvState(DataValue):
    """
    For representing state values which obey a defined state machine, such as a vari-
    able representing the states of an instruction or care process.
    """

    implements(IDvState)
    
    def __init__(self, value, isTerminal):
        self.value=value
        self.isTerminal=isTerminal
        

class IDvEncapsulated(Interface):
    """Abstract class defining the common meta-data of all types of encapsulated data."""
    
    size = Int(
        title=_(u"Size"),
        description=_(u"""Original size in bytes of unencoded encapsulated data. I.e. encodings 
                    such as base64, hexadecimal etc do not change the value of this attribute."""),
        
        )
    
    charset = Object(
        schema=ICodePhrase,
        title=_(u"charset"),
        description=_(u"""Name of character encoding scheme in which this value is encoded. 
        Coded from openEHR Code Set "character sets". Unicode is the default assumption 
        in openEHR, with UTF-8 being the assumed encoding. This attribute allows for 
        variations from these assumptions. Type==CodePhrase"""),
        required=False,
        )
    
    language = Object(
        schema=ICodePhrase,
        title=_(u"Language"),
        description=_(u"""Optional indicator of the localised language in which the data 
                    is written, if relevant. Coded from openEHR Code Set "languages". Type==CodePhrase"""),
        required=False,
        )
    
    def asString():
        """Result = alternate_text [(uri)]"""
        
    def sizePositive():
        """size >= 0"""
        
    def languageValid():
        """language /= Void implies code_set(Code_set_id_languages).has_code(language)"""
        
    def charsetValid():
        """charset /= Void implies code_set(Code_set_id_character_sets).has_code(charset)"""
        
class DvEncapsulated(DataValue):
    """Abstract class defining the common meta-data of all types of encapsulated data."""

    implements(IDvEncapsulated)

    def __init__(self,charset,language):
        self.charset=charset
        self.language=language
        self.size=0 # set to zero here but calculated in the subclasses
        
    def asString(self):
        u"""Result = alternate_text [(uri)]"""
        
    def sizePositive(self):
        u"""size >= 0"""
        return self.size>0
        
    def languageValid(self):
        u"""language /= Void implies code_set(Code_set_id_languages).has_code(language)"""
        
    def charsetValid(self):
        u"""charset /= Void implies code_set(Code_set_id_character_sets).has_code(charset)"""
 
class IDvMultimedia(Interface):
    """
    A specialisation of DvEncapsulated for audiovisual and biosignal types. Includes further 
    metadata relating to multimedia types which are not applicable to other subtypes of DvEncapsulated.
    """
    
    alternateText = TextLine(
        title=_(u"Alternate Text"),
        description=_(u"""Text to display in lieu of multimedia display/replay"""),
        required=False,
        )
    
    mediaType = Object(
        schema=ICodePhrase,
        title=_(u"Media Type"),
        description=_(u"""Data media type coded from openEHR code set "media types" 
        (interface for the IANA MIME types code set)."""),
        
        )
    
    compressionAlgorithm = Object(
        schema=ICodePhrase,
        title=_(u"Compression Algorithm"),
        description=_(u"""Compression type, a coded value from the openEHR "Integrity check" 
        code set. Void means no compression."""),
        required=False,
        )
    
    integrityCheck = BytesLine(
        title=_(u"Integrity Check"),
        description=_(u"""Binary cryptographic integrity checksum. Type==Array<Octet>"""),
        required=False,
        )
    
    integrityCheckAlgorithm = Object(
        schema=ICodePhrase,
        title=_(u"Integrity Check Algorithm"),
        description=_(u"""Type of integrity check, a coded value from the openEHR "Integrity check" code set."""),
        required=False,
        )
    
    thumbnail = Field(
        title=_(u"Thumbnail"),
        required=False
    )
   
    uri = Object(
        schema=IDvUri,
        title=_(u"URI"),
        description=_(u"""URI reference to electronic information stored outside the record as a file, 
        database entry etc, if supplied as a reference. Type == DvUri."""),
        required=False,
        )
    
    data = BytesLine(
        title=_(u"Data"),
        description=_(u"""The actual data found at uri, if supplied inline. Type==Array<Octet>"""),
        required=False,
        )
    
    def isExternal():
        """Computed from the value of the uri attribute: True if the data is stored externally 
        to the record, as indicated by 'uri'. A copy may also be stored internally, in which case 
        'isExpanded' is also true.  Ensure uri !=None and uri != '' """
        
    def isInline():
        """Computed from the value of the data attribute: True if the data is stored in expanded 
        form, ie within the EHR itself. Ensure data != None. """
        
    def isCompressed():
        """Computed from the value of the compression_algorithm attribute: True if the data is 
        stored in compressed form. Ensure compressionAlgorithm != None. """
        
    def hasIntegrityCheck():
        """Computed from the value of the integrityCheckAlgorithm attribute: True if an 
        integrity check has been computed. Ensure integrityCheckAlgorithm != None."""
        
        
class DvMultimedia(DvEncapsulated):
    """
    A specialisation of DvEncapsulated for audiovisual and biosignal types. Includes further 
    metadata relating to multimedia types which are not applicable to other subtypes of DvEncapsulated.
    """
    
    implements(IDvMultimedia)

    def __init__(self,altTxt,mType,compAlg,intChk,intChkAlg,tnail,uri,data,charset,language):
        self.alternateText=altTxt
        self.mediaType=mType
        self.integrityCheck=intChk
        self.integrityCheckAlgorithm=intChkAlg
        self.thumbnail=tnail
        self.uri=uri
        self.data=data
        self.size=len(data)
        DvEncapsulated.__init__(self,charset,language)
        
    def isExternal(self):
        u"""Computed from the value of the uri attribute: True if the data is stored externally 
        to the record, as indicated by 'uri'. A copy may also be stored internally, in which case 
        'isExpanded' is also true.  Ensure uri !=None and uri != '' """
        
    def isInline(self):
        u"""Computed from the value of the data attribute: True if the data is stored in expanded 
        form, ie within the EHR itself. Ensure data != None. """
        
    def isCompressed(self):
        u"""Computed from the value of the compression_algorithm attribute: True if the data is 
        stored in compressed form. Ensure compressionAlgorithm != None. """
        
    def hasIntegrityCheck(self):
        u"""Computed from the value of the integrityCheckAlgorithm attribute: True if an 
        integrity check has been computed. Ensure integrityCheckAlgorithm != None."""
                 
    def mediaTypeValidity(self): 
        u"""mediaType != None and mediaType in codeSetIdMediaTypes"""
        
    def compressionAlgorithmValidity(self):
        u"""compressionAlgorithm != None and compressionAlgorithm in codeSetIdCompressionAlgorithms."""
        
    def integrityCheckValidity(self):
        u"""integrityCheck != None and integrityCheckAlgorithm != None"""
        
    def integrityCheckAlgorithmValidity(self):
        u"""integrityCheckAlgorithm  != None and integrityCheckAlgorithm in codeSetIdIntegrityCheckAlgorithms"""

        
        
                
        
class IDvParsable(Interface):
    """
    Encapsulated data expressed as a parsable String. The internal model of the data item is not 
    described in the openEHR model in common with other encapsulated types, but in this case, the 
    form of the data is assumed to be plaintext, rather than compressed or other types of large binary data.
    Used for representing values which are formal textual representations, e.g. guidelines.
    """

    size=Int(
        title=_(u"Size"),
        description=_(u""" """),
        
        )

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""The string, which may validly be empty in some syntaxes"""),
        
        )
    
    formalism = TextLine(
        title=_(u"Formalism"),
        description=_(u"""The name of the formalism, e.g. "GLIF 1.0", "proforma" etc."""),
        
        )
    
    def valueValid():
        """value != None."""

    def formalismValidity():
        """formalism != None and formalism != '' """
        
        
class DvParsable(DvEncapsulated):
    u"""
    Encapsulated data expressed as a parsable String. The internal model of the data item is not 
    described in the openEHR model in common with other encapsulated types, but in this case, the 
    form of the data is assumed to be plaintext, rather than compressed or other types of large binary data.
    Used for representing values which are formal textual representations, e.g. guidelines.
    """
    
    implements(IDvParsable)

    def __init__(self,size,value,formalism,charset,language):
        self.size=len(value)
        self.value=value
        self.formalism=formalism
        DvEncapsulated.__init__(self,charset,language)
        
    def valueValid(self):
        u"""value != None."""
        return self.value!=None

    def formalismValidity(self):
        u"""formalism != None and formalism != '' """
        return self.formalism!=None and self.formalism!=''
    
        
# Begin the Quantity package
class IDvOrdered(Interface):
    """
    Purpose:           
    Abstract class defining the concept of ordered values, which includes ordinals as
    well as true quantities. It defines the functions '<' and is_strictly_comparable_to,
    the latter of which must evaluate to True for instances being compared with the
    '<' function, or used as limits in the DV_INTERVAL<T> class.

    Use:    
    Data value types which are to be used as limits in the DV_INTERVAL<T> class
    must inherit from this class, and implement the function
    is_strictly_comparable_to to ensure that instances compare meaningfully. For
    example, instances of DV_QUANTITY can only be compared if they measure the
    same kind of physical quantity.
    """
    
    """ Cause circular import
    normalRange = Object(
        schema=IDvInterval,
        title = _(u"normalRange"),
        description = _(u"Optional normal range."),
        required = False
        )
    """

    normalRange = Int(
        title = _(u"normalRange"),
        description = _(u"""Optional normal range."""),
        required = False
        )
    
    otherReferenceRanges = List(
        value_type=Object(schema=IObjectRef),
        title = _(u"otherReferenceRanges"),
        description = _(u"""Optional tagged other reference ranges for this value in its particular measurement context. A list of ReferenceRange types."""),
        required = False
        )
    
    normalStatus = Object(
        schema=ICodePhrase,
        title = _(u"normalStatus"),
        description = _(u"""Optional normal status indicator of value with respect to normal range for this value. Often included by lab, even if the normal range itself is not included. Coded by ordinals in series HHH, HH, H, (nothing), L, LL, LLL; see openEHR terminology group "normal status"."""),
        required = False
    )
       
    def isStrictlyComparableTo(other):
        """Test if two instances are strictly comparable. Called by object.__cmp__"""


    def isNormal():
        """ 
        Value is in the normal range, determined by comparison of the value to the normalRange if present, or by the normalStatus marker if present.
        isNormal: Boolean
        require
        normalRange /= Void or normalStatus /= Void
        ensure
        normalRange /= Void implies Result = normalRange.has(Current)
        normalStatus /= Void implies normal_status.code_string.is_equal("N")
        """
    
    def isSimple():
        """
        is_simple: Boolean 
        True if this quantity has no reference ranges.
        """
    
 
class DvOrdered(DataValue,Orderable):
    """
    Purpose:           
    Abstract class defining the concept of ordered values, which includes ordinals as
    well as true quantities. It defines the functions '<' and is_strictly_comparable_to,
    the latter of which must evaluate to True for instances being compared with the
    '<' function, or used as limits in the DV_INTERVAL<T> class.

    Use:    
    Data value types which are to be used as limits in the DV_INTERVAL<T> class
    must inherit from this class, and implement the function
    is_strictly_comparable_to to ensure that instances compare meaningfully. For
    example, instances of DV_QUANTITY can only be compared if they measure the
    same kind of physical quantity.
    """

    implements(IDvOrdered)
    
    def __init__(self,normalRange,otherReferenceRanges,normalStatus):
        self.normalRange=normalRange
        self.otherReferenceRanges=otherReferenceRanges
        self.normalStatus=normalStatus
                
        index=False
        for e in otherReferenceRanges:
            if e.meaning.value=='limits':
                index=True
                limitsRange=e
                break
        
        if index==False:
            raise ValueError(_("No limits in otherReferenceRanges"))

    def isNormal(self):
        """ 
        Value is in the normal range, determined by comparison of the value to the normalRange 
        if present, or by the normalStatus marker if present.

        isNormal: Boolean
        require
        normalRange /= Void or normalStatus /= Void
        ensure
        normalRange /= Void implies Result = normalRange.has(Current)
        normalStatus /= Void implies normal_status.code_string.is_equal("N")
        """
        
        if self.normalStatus.codeString == "N":
            return True
        else:
            return self.value in self.normalRange 
        
        
    def isSimple(self):
        """
        is_simple: Boolean 
        True if this quantity has no reference ranges.
        """
        if (self.normalRange is None or self.normalRange is []) and (self.otherReferenceRanges is None or self.otherReferenceRanges is []):
            return True
        else:
            return False
                  
        
        
class IDvQuantified(Interface):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """
    
    magnitude = Float(
        title=_(u"magnitude"),
        description=_(u"""Numeric value of the quantity in canonical (i.e. single value)
                          form. Implemented as constant, function or attribute in subtypes as
                          appropriate. The type OrdereNumeric is mapped to the available 
                          appropriate type in each implementation technology."""),
        required=True
    )
      
    magnitudeStatus = List(
        value_type=TextLine(),
        title=_(u"magnitudeStatus"),
        description=_(u"""Optional status of magnitude with values:
                                = : magnitude is a point value
                                < : value is < magnitude
                                > : value is > magnitude
                                <= : value is <= magnitude
                                >= : value is >= magnitude
                                ~ : value is approximately magnitude
                                If not present, meaning is =. """),
        required=True
    )
    
                      
    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """

    def magnitudeExists():
        """
        Does the magnitude exist?
        """
        


 
class DvQuantified(DvOrdered):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    
    
    """
     
    implements(IDvQuantified)
    
    def __init__(self,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        self.magnitude=magnitude
        self.magnitudeStatus=magnitudeStatus
        DvOrdered.__init__(self,normalRange,otherReferenceRanges,normalStatus)
        
        
    def validMagnitudeStatus(self,val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """

    def magnitudeExists(self):
        """
        Does the magnitude exist?
        """
        return self.magnitude != None

class IDvAbsoluteQuantity(Interface):
    """
    Abstract class defining the concept of quantified entities whose values are absolute with respect to an origin. Dates and Times are the main example.
    """
    
    accuracy = Field(
        title=_(u"Accuracy"),
        description=_(u"""Accuracy of measurement, expressed as a half-range value of the diff type for this quantity (i.e. an accuracy of x means +/- x)."""),
        default=None,
        )
    
    def __add__():
        """Addition of a diffential amount to this quantity"""
        
    def __sub__():
        """Result of a subtracting a differential amount from this quantity"""
        
    def diff():
        """Difference two quantities"""
        
    def accuracyUnknown():
        """ True if accuracy is None """

class DvAbsoluteQuantity(DvQuantified):
    """
    Abstract class defining the concept of quantified entities whose values are abso-
    lute with respect to an origin. Dates and Times are the main example.
    """
    
    implements(IDvAbsoluteQuantity)
    
    
    def __init__(self,accuracy,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        self.accuracy=accuracy
        DvQuantified.__init__(self,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus)
        
    def add(self,a_diff):
        """(a_diff: like diff): like Current
        """
    
    def subtract(self,a_diff):
        """(a_diff: like diff): like Current 
        """
        
    def diff(self,other):
        """(other: like Current): DV_AMOUNT
        """
        
    def accuracyUnknown(self):
        """ True if accuracy is None """
        return self.accuracy==None
            
        
        
class IDvAmount(Interface):
    """   
    Abstract class defining the concept of relative quantified amounts. For relative
    quantities, the + and - operators are defined (unlike descendants of
    DV_ABSOLUTE_QUANTITY, such as the date/time types).
    """

    accuracy = Int(
        title=_(u"accuracy"),
        description=_(u"""Accuracy of measurement, expressed either as a half-range 
                         percent value (accuracyIsPercent = True) or a half-range
                         quantity. A value of 0 means that accuracy was not recorded."""),
        required=False
    )

  
    accuracyIsPercent = Bool(
        title=_(u"accuracyIsPercent"),
        description=_(u"""If True, indicates that when this object was created, accuracy was recorded 
                    as a percent value; if False, as an absolute quantity value."""),
        required=False
    )

    
    def validPercentage(val):
        """
        Test whether a number is a valid percentage,i.e. between 0 and 100.
        ensure
        Result implies val >= 0.0 and val <= 100.0
        """

    def __add__(val):
        """
        Sum of this quantity and another whose formal type must be the 
        difference type of this quantity
        """
        
    def __sub__(val):
        """
        Difference of this quantity and another whose formal type must be the
        difference type of this quantity
        """

    def negate():
        """
        Negated version of current object, such as used for representing a
        difference type of this quantity
        """

class DvAmount(DvQuantified):
    u"""   
    Abstract class defining the concept of relative quantified 'amounts'. For relative
    quantities, the '+' and '-' operators are defined (unlike descendants of
    DV_ABSOLUTE_QUANTITY, such as the date/time types).
    """
    
    implements(IDvAmount)
    
    def __init__(self,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        if accuracy==None:        
            self.accuracy=-1
        else:
            self.accuracy=accuracy
        self.accuracyIsPercent=accuracyIsPercent
        DvQuantified.__init__(self,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus)
        
    def validPercentage(val):
        u"""
        Test whether a number is a valid percentage,i.e. between 0 and 100.
        ensure
        Result implies val >= 0.0 and val <= 100.0
        """
        
        return val>=0 and val<=100
    
    def __add__(self,val):
        """
        Sum of this quantity and another whose formal type must be the 
        difference type of this quantity
        """
        
    def __sub__(self,val):
        """
        Difference of this quantity and another whose formal type must be the
        difference type of this quantity
        """

    def negate(self):
        """
        Negated version of current object, such as used for representing a
        difference type of this quantity
        """
    
    
    
    
class IDvDuration(IDvAmount):
    """
    Represents a period of time with respect to a notional point in time, which is not
    specified. A sign may be used to indicate the duration is "backwards" in time
    rather than forwards.
    
    Note that a deviation from ISO8601 is supported, allowing the 'W' designator to
    be mixed with other designators. See assumed types section in the Support IM.

    Used for recording the duration of something in the real world, particularly when
    there is a need a) to represent the duration in customary format, i.e. days, hours,
    minutes etc, and b) if it will be used in computational operations with date/time
    quantities, i.e. additions, subtractions etc.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 duration"""),
        required=True,
        )     
        
    def magnitude():
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """


    def valueValid(): 
        """validIso8601Duration(value)"""
            
class DvDuration(DvAmount):
    u"""
    Represents a period of time with respect to a notional point in time, which is not
    specified. A sign may be used to indicate the duration is "backwards" in time
    rather than forwards.
    
    Note that a deviation from ISO8601 is supported, allowing the 'W' designator to
    be mixed with other designators. See assumed types section in the Support IM.

    Used for recording the duration of something in the real world, particularly when
    there is a need a) to represent the duration in customary format, i.e. days, hours,
    minutes etc, and b) if it will be used in computational operations with date/time
    quantities, i.e. additions, subtractions etc.
    """

    implements(IDvDuration)

    def __init__(self,value,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalStatus,normalRange,otherReferenceRanges):
        self.value=value
        DvAmount.__init__(self,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus)
       
    def magnitude(self):
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """

    def valueValid(self): 
        u"""validIso8601Duration(value)"""
        
class IDvCount(Interface):
    """        
    Purpose: Countable quantities
         
             Used for countable types such as pregnancies and steps (taken by a physiotherapy
    Use:     patient), number of cigarettes smoked in a day.

    Misuse:  Not used for amounts of physical entities (which all have units)
    """
    
    magnitude = Int(
        title=_(u"Magnitude"),
        description=_(u"""numeric magnitude of the quantity"""),
        required=True
        )

    
class DvCount(DvAmount):
    u"""        
    Purpose: Countable quantities
         
             Used for countable types such as pregnancies and steps (taken by a physiotherapy
    Use:     patient), number of cigarettes smoked in a day.

    Misuse:  Not used for amounts of physical entities (which all have units)
    
    
    """
    
    implements(IDvCount)
    
    def __init__(self,magnitude,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        self.magnitude=magnitude
        DvAmount.__init__(self,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus)
    
    def __add__(self, val):
        if not isinstance(val,DvCount):
            raise TypeError("Argument type must be DvCount")
        else:
            return DvCount(self.magnitude + val.magnitude, self.accuracy, self.accuracyIsPercent, self.magnitudeStatus, self.normalStatus, self.normalRange, self.otherReferenceRanges)
        
        
    def __sub__(self, val):
        if not isinstance(val,DvCount):
            raise TypeError("Argument type must be DvCount")
        else:
            return DvCount(self.magnitude - val.magnitude, self.accuracy, self.accuracyIsPercent, self.magnitudeStatus, self.normalStatus, self.normalRange, self.otherReferenceRanges)

    def negate(self):
        return DvCount(-self.magnitude, self.accuracy, self.accuracyIsPercent, self.magnitudeStatus, self.normalStatus, self.normalRange, self.otherReferenceRanges)
        

class IDvInterval(Interface):
    """
    Used to define intervals of dates, times, quantities (whose units match) and so on.
    The type parameter, T, must be a descendant of the type DV_ORDERED, which is
    necessary (but not sufficient) for instances to be compared (strictly_comparable
    is also needed).
    Without the DV_INTERVAL class, quite a few more DV_ classes would be needed
    to express logical intervals, namely interval versions of all the date/time classes,
    and of quantity classes. Further, it allows the semantics of intervals to be stated in
    one place unequivocally, including the conditions for strict comparison.
    The basic semantics are derived from the class INTERVAL<T>, described in the
    support RM.
    """

    lower = Object(
        schema=IDvOrdered,
        title=_(u"lower value"),
        description=_(u"""Interval lower value."""),
        required=True
    )
    
    upper = Object(
        schema=IDvOrdered,
        title=_(u"upper value"),
        description=_(u"""Interval upper value."""),
        required=True
    )
    
    
    lower_included = Bool(
        title=_(u"Lower value included"),
        description=_(u"""Lower value included in interval."""),
        required=True
    )    
    
    upper_included = Bool(
        title=_(u"upper value"),
        description=_(u"""Interval upper value."""),
        required=True
    )
    
    lower_unbounded = Bool(
        title=_(u"lower unbounded"),
        description=_(u"""Lower value unbounded in interval."""),
        required=False
    )    
    
    upper_unbounded = Bool(
        title=_(u"upper unbounded"),
        description=_(u"""Upper value unbounded in interval."""),
        required=False
    )
    
    
    
class DvInterval(DataValue,Interval):
    """
    Used to define intervals of dates, times, quantities (whose units match) and so on.
    The type parameter, T, must be a descendant of the type DV_ORDERED, which is
    necessary (but not sufficient) for instances to be compared (strictly_comparable
    is also needed).
    Without the DV_INTERVAL class, quite a few more DV_ classes would be needed
    to express logical intervals, namely interval versions of all the date/time classes,
    and of quantity classes. Further, it allows the semantics of intervals to be stated in
    one place unequivocally, including the conditions for strict comparison.
    The basic semantics are derived from the class INTERVAL<T>, described in the
    support RM.
    
    """
    
    implements(IDvInterval)
    
    def __init__(self, lower, upper, lower_included, upper_included):
        Interval.__init__(self, lower, upper, lower_included, upper_included)

        
        
class IDvOrdinal(Interface):
    """
    Models rankings and scores, e.g. pain, Apgar values, etc, where there is a)
    implied ordering, b) no implication that the distance between each value is con-
    stant, and c) the total number of values is finite.

    Used for recording any clinical datum which is customarily recorded using sym-
    bolic values. Example: the results on a urinalysis strip, e.g. {neg, trace, +,
    ++, +++} are used for leucocytes, protein, nitrites etc; for non-haemolysed
    blood {neg, trace, moderate}; for haemolysed blood {neg, trace,
    small, moderate, large}.
    """
    
    value = Int(
        title=_(u"value"),
        description=_(u""" Ordinal position in enumeration of values. """),
        required=True
    )
    
    symbol = Object(
        schema=IDvCodedText,
        title=_(u"symbol"),
        description=_(u"""Coded textual representation of this 
                       value in the enumeration, which may be strings made from "+" symbols, 
                       or other enumerations of terms such as "mild", "moderate", "severe",
                       or even the same number series as the values,
                       e.g. "1", "2", "3". Codes come from archetype."""),
        required=True
    )


    def limits():
        """
        limits of the ordinal enumeration, to allow
        comparison of an ordinal value to its limits.
        Returns DvOrdinal.
        """

    def isStrictlyComparableTo(self, other):
        """        
        True if symbols come from same vocabulary,assuming the vocabulary is a 
        subset or value range, e.g. urine:protein.
        
        (other: like Current): Boolean 
        ensure
        symbol.is_comparable (other.symbol) implies Result
        """
        
        
    def compareTo(self, dvOrdinal):
        u"""True if types are the same and values compare
        infix '<' (other: like Current):
        Boolean
        ensure
        value<other.values implies
        Result
        """
        
        
class DvOrdinal(DvOrdered):
    u"""
    Models rankings and scores, e.g. pain, Apgar values, etc, where there is a)
    implied ordering, b) no implication that the distance between each value is con-
    stant, and c) the total number of values is finite.

    Used for recording any clinical datum which is customarily recorded using sym-
    bolic values. Example: the results on a urinalysis strip, e.g. {neg, trace, +,
    ++, +++} are used for leucocytes, protein, nitrites etc; for non-haemolysed
    blood {neg, trace, moderate}; for haemolysed blood {neg, trace,
    small, moderate, large}.
    """

    implements(IDvOrdinal)
    
    def __init__(self,value,symbol,normalRange,otherReferenceRanges,normalStatus):
        self.value=value
        self.symbol=symbol
        DvOrdered.__init__(self,normalRange,otherReferenceRanges,normalStatus)

        if symbol == None:
            raise ValueError(_("No symbol"))
            
    def limits(self):
        """
        limits of the ordinal enumeration, to allow
        comparison of an ordinal value to its limits.
        Returns DvOrdinal.
        """
            

    def isStrictlyComparableTo(self, other):
        u"""        
        True if symbols come from same vocabulary,assuming the vocabulary is a 
        subset or value range, e.g. "urine:protein".
        
        (other: like Current): Boolean 
        ensure
        symbol.is_comparable (other.symbol) implies Result
        """
        
        

    
class IProportionKind(Interface):
    """
    Class of enumeration constants defining types of proportion for the
    DV_PROPORTION class.
    """


    def validProportionKind(n):
        """
        True if n is one of the defined types.
        """
        
class ProportionKind(grok.Model):
    """
    Class of enumeration constants defining types of proportion for the
    DV_PROPORTION class.
    """
    def __init__(self):
        self.pkRatio = 0
        self.pkUnitary = 1
        self.pkPercent = 2
        self.pkFraction = 3
        self.pkIntegerFraction = 4

    def validProportionKind(n):
        """
        True if n is one of the defined types.
        """
        return n in (pkRatio,pkUnitary,pkPercent,pkFraction,pkIntegerFraction)
    
        
    
class IDvProportion(Interface):
    """
              Models a ratio of values, i.e. where the numerator and denominator are both pure
    Purpose:  numbers.
    
              Used for recording titers (e.g. 1:128), concentration ratios, e.g. Na:K (unitary
      Use:    denominator), albumin:creatinine ratio, and percentages, e.g. red cell distirbution
              width (RDW).
        
              Should not be used to represent things like blood pressure which are often written
              using a / character, giving the misleading impression that the item is a ratio,
    MisUse:   when in fact it is a structured value. E.g. visual acuity 6/24 is not a ratio.
              Should not be used for formulations.
    """
    
    
    numerator = Float(
        title=_(u"numerator"),
        description=_(u"""numerator of ratio"""),
        required=True
    )
    
    denominator = Float(
        title=_(u"denominator"),
        description=_(u"""denominator of ratio"""),
        required=True
    )
    
    type = Int(
        title=_(u"type"),
        description=_(u"""Indicates semantic type of proportion, including percent, unitary etc."""),
        required=True
    )
    
    precision = Int(
        title=_(u"precision"),
        description=_(u"""Precision to which the numerator and denominator values of the proportion 
                    are expressed, in terms of number of decimal places. The value 0 implies an 
                    integral quantity. The value -1 implies no limit, i.e.any number of decimal places."""),
        required=False
    )
    
    
    def isIntegral():
        """
        True if the numerator and denominator values are integers, i.e. if the precision is 0.
        """

    def magnitude():
        """
        Effective magnitude represented by ratio.
        Result = numerator / denominator
        """
        
class DvProportion(DvAmount,ProportionKind):
    """
              Models a ratio of values, i.e. where the numerator and denominator are both pure
    Purpose:  numbers.
    
              Used for recording titers (e.g. 1:128), concentration ratios, e.g. Na:K (unitary
      Use:    denominator), albumin:creatinine ratio, and percentages, e.g. red cell distirbution
              width (RDW).
        
              Should not be used to represent things like blood pressure which are often written
              using a '/' character, giving the misleading impression that the item is a ratio,
    MisUse:   when in fact it is a structured value. E.g. visual acuity "6/24" is not a ratio.
              Should not be used for formulations.
    """

    implements(IDvProportion)
    
    def __init__(self,numerator,denominator,type,precision,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        if isinstance(numerator, float) or isinstance(numerator, int):
            self.numerator = numerator
        else:
            raise AttributeError(_("Invalid numerator type."))
        
        if isinstance(denominator, float) or isinstance(denominator,int):
            self.denominator = denominator
        else:
            raise AttributeError(_("Invalid denominator type."))
        
        if isinstance(type, ProportionKind):
            self.type = type
        else:
            raise AttributeError(_("Invalid type type."))
        
        if precision != None:
            if isinstance(precision,int):
                self.precision = precision
            else:
                raise AttributeError(_("Invalid precision type."))
            
        DvAmount.__init__(self,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus)
            
            
    def isIntegral(self):
        """
        True if the numerator and denominator values are integers, i.e. if the precision is 0.
        """
        return isinstance(self.numerator,int) and isinstance(self.denominator,int) 

    def magnitude(self):
        """
        Effective magnitude represented by ratio.
        Result = numerator / denominator
        """  
        return self.numerator / self.denominator
    
class IDvQuantified(Interface):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """
    
    magnitude = Float(
        title=_(u"magnitude"),
        description=_(u"""Numeric value of the quantity in canonical (i.e. single value)
                          form. Implemented as constant, function or attribute in subtypes as
                          appropriate. The type OrdereNumeric is mapped to the available 
                          appropriate type in each implementation technology."""),
        required=True
    )
    
      
    magnitudeStatus = List(
        #value_type=TextLine(),
        title=_(u"magnitudeStatus"),
        description=_(u"""Optional status of magnitude with values:
                                = : magnitude is a point value
                                < : value is < magnitude
                                > : value is > magnitude
                                <= : value is <= magnitude
                                >= : value is >= magnitude
                                ~ : value is approximately magnitude
                                If not present, meaning is =. """),
        required=True
    )
    
                      
    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """

    def magnitudeExists():
        """
        Does the magnitude exist?
        """
        


class DvQuantified(DvOrdered):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """

    def __init__(self,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        self.magnitude=magnitude
        self.magnitudeStatus=magnitudeStatus
        DvOrdered.__init__(self,normalRange,otherReferenceRanges,normalStatus)
        
    def magnitudeExists(self):
        return self.magnitude!=None
        
    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """
        if(magnitudeExists()):
            if val in ("=",">=","<=",">","<","~"):
                return True
        else:
            return False
        

class IDvQuantity(Interface):
    """
    Quantitified type representing scientific quantities, i.e. quantities expressed as a
    magnitude and units.
    Units were inspired by the Unified Code for Units of Measure (UCUM), devel-
    oped by Gunther Schadow and Clement J. McDonald of The Regenstrief Institute.
        
    Can also be used for time durations, where it is more convenient to treat these as
    simply a number of seconds rather than days, months, years.
    """

    magnitude = Float(
        title=_(u"Magnitude"),
        description=_(u"""Numeric magnitude of the quantity."""),
        required=True
        )
    
    units = TextLine(
        title=_(u"Units"),
        description=_(u"""Stringified units, expressed in UCUM unit syntax, 
                    e.g. "kg/m2", "mm[Hg]", "ms-1", "km/h".Implemented accordingly in subtypes."""),
                      
        )

    
    precision = Int(
        title=_(u"Precision"),
        description=_(u"""Precision to which the value of the quantity is expressed, in terms of 
                    number of decimal places. The value 0 implies an integral quantity.
                    The value -1 implies no limit, i.e. any number of decimal places."""),        
        required=False,
        )
    
    def precisionValid():
        """Precision must be >= -1"""
            
    def isIntegral():
        """True if precision = 0; quantity represents an integral number."""

    
    def isStrictlyComparableTo(other):
        """Test if two instances are strictly comparable by ensuring that the measured 
        property is the same, achieved using the Measurement service function units_equivalent.
        
        Return selfunits == other.units
        """
        
        
class DvQuantity(DvAmount):
    """
    Quantitified type representing "scientific" quantities, i.e. quantities expressed as a
    magnitude and units.
    Units were inspired by the Unified Code for Units of Measure (UCUM), devel-
    oped by Gunther Schadow and Clement J. McDonald of The Regenstrief Institute.
        
    Can also be used for time durations, where it is more convenient to treat these as
    simply a number of seconds rather than days, months, years.
    """
    
    implements(IDvQuantity)
   
    def __init__(self,magnitude,units,precision,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        self.magnitude=magnitude
        self.units=units
        self.precision=precision
        DvAmount.__init__(self,accuracy,accuracyIsPercent,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus)
        
    def precisionValid(self):
        return self.precision >= -1
    
    def isIntegral(self):
        """True if precision = 0; quantity represents an integral number."""
        return self.precision==0

    
    def isStrictlyComparableTo(self,other):
        """
        Test if two instances are strictly comparable by ensuring that the measured 
        property is the same, achieved using the Measurement service function units_equivalent.
        """
        if(isinstance(other, self.__class__)): 
            return self.units==other.units and self.magnitude==other.magnitude
              
    
class IReferenceRange(Interface):
    """
    Defines a named range to be associated with any ORDERED datum. Each such
    range is particular to the patient and context, e.g. sex, age, and any other factor
    which affects ranges.
    May be used to represent normal, therapeutic, dangerous, critical etc ranges.
    """
    
    meaning=Object(
        schema=IDvText,
        title=_(u"meaning"),
        description=_(u"""Term whose value indicates the meaning of this range,  e.g. "normal", "critical", "therapeutic" etc."""),
        required=True
        )
    
    range=Object(
        schema=IDvInterval,
        title=_(u"range"),
        description=_(u"""The data range for this meaning, e.g."critical" etc."""),
        required=True
        )

    def isInRange(val):
        """
        Indicates if the value 'val' is inside the range
        """

class ReferenceRange(DvOrdered):
    """
    Defines a named range to be associated with any ORDERED datum. Each such
    range is particular to the patient and context, e.g. sex, age, and any other factor
    which affects ranges.
    May be used to represent normal, therapeutic, dangerous, critical etc ranges.
    """
    
    implements(IReferenceRange)
    
    def __init__(self,meaning,range,normalRange,otherReferenceRanges,normalStatus):
        self.meaning=meaning
        self.range=range
        DvOrdered.__init__(self,normalRange,otherReferenceRanges,normalStatus)
        
    def isInRange(self,val):
        """
        Indicates if the value 'val' is inside the range
        """
        return self.range.has(val)
    
# Begin the Datetime package
class IDvTemporal(Interface):
    """
    Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is DvDuration.
    """

    pass

class DvTemporal(DvAbsoluteQuantity):
    """
    Abstract class. Specialised temporal variant of DV_ABSOLUTE_QUANTITY whose diff type is
    DV_DURATION.
    """
    
    implements(IDvTemporal)

    def __init__(self,accuracy,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus):
        DvAbsoluteQuantity.__init__(self,accuracy,magnitude,magnitudeStatus,normalRange,otherReferenceRanges,normalStatus)
        
    def diff(self,other):
        """
        Redefined to return a DvDuratio
        """
        return DvDuration(other,self.magnitude)


class IDvDate(Interface):
    """
    Represents an absolute point in time, as measured on the Gregorian calendar, and
    specified only to the day. Semantics defined by ISO 8601.
    Used for recording dates in real world time. The partial form is used for 
    approximate birth dates, dates of death, etc.   
    """
    
    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 date string"""),
        
        )

    def diff(self,other):
        """Difference of two dates. Returns a DvDuration"""
        
        
    def magnitude(self):
        """ Returns the numeric value of the date as days since the calendar origin point 1/1/0000"""


class DvDate(DvTemporal):
    """
    Represents an absolute point in time, as measured on the Gregorian calendar, and
    specified only to the day. Semantics defined by ISO 8601.
    Used for recording dates in real world time. The partial form is used for 
    approximate birth dates, dates of death, etc.   
    """

    implements(IDvDate)

    def __init__(self,value):
        try:
            d=value.split('-')
            self.value = date(int(d[0]),int(d[1]),int(d[2]))
        except Exception:
            raise ValueError(_('Incorrect date format. Date must be YYYY-MM-DD'))
    

    def diff(other):
        """Difference of two dates. Returns a Dv_Duration"""
        return DvDuration(other,self.value)
        
    def magnitude():
        """ Returns the numeric value of the date as days since the calendar origin point 1/1/0000"""
        return date(value.tm_year, value.tm_mon, value.tm_mday).toordinal()

class IDvDateTime(Interface):
    """
    Represents an absolute point in time, specified to the second. Semantics defined by ISO 8601.
    Used for recording a precise point in real world time, and for approximate time
    stamps, e.g. the origin of a HISTORY in an OBSERVATION which is only partially known.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 date/time string"""),
        
        )

    def diff(other):
        """Difference of two date/times. Returns a DvDuration"""
        
        
    def magnitude():
        """
        numeric value of the date/time as seconds since the calendar origin point.
        Result >= 0.0        
        """


    def valueValid(): 
        """validIso8601DateTime(value)"""
  
        
class DvDateTime(DvTemporal):
    u"""
    Represents an absolute point in time, specified to the second. Semantics defined by ISO 8601.
    Used for recording a precise point in real world time, and for approximate time
    stamps, e.g. the origin of a HISTORY in an OBSERVATION which is only partially known.
    """

    implements(IDvDateTime)

    def __init__(self,value):
        self.value=datetime.now()
        

    def diff(self,other):
        u"""Difference of two date/times. Returns a DvDuration"""
        return self.value-other
        
    def magnitude(self):
        u"""
        numeric value of the date/time as seconds since the calendar origin point.
        Result >= 0.0        
        """
        return time.time()

    def valueValid(): 
        u"""validIso8601DateTime(value)"""

        
        
class IDvDuration(Interface):
    """
    Represents a period of time with respect to a notional point in time, which is not
    specified. A sign may be used to indicate the duration is "backwards" in time
    rather than forwards.
    
    Note that a deviation from ISO8601 is supported, allowing the 'W' designator to
    be mixed with other designators. See assumed types section in the Support IM.

    Used for recording the duration of something in the real world, particularly when
    there is a need a) to represent the duration in customary format, i.e. days, hours,
    minutes etc, and b) if it will be used in computational operations with date/time
    quantities, i.e. additions, subtractions etc.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 duration"""),
        
        )     
        
    def magnitude(self):
        """
        Numeric value of the duration in seconds.
        Result >= 0.0        
        """


    def valueValid(self): 
        """validIso8601 Duration(value)"""


        
class IDvTime(Interface):
    """
    Represents an absolute point in time from an origin usually interpreted as meaning the start 
    of the current day, specified to the second. Semantics defined by ISO8601.
    
    Used for recording real world times, rather than scientifically measured fine
    amounts of time. The partial form is used for approximate times of events and
    substance administrations. 
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""ISO8601 time string"""),
        
        )

    def diff(other):
        """Difference of two times. Returns a DvDuration"""
        
        
    def magnitude():
        """
        Returns the numeric value of the seconds since midnight.
        Result >= 0.0        
        """


    def valueValid(): 
        """validIso8601Time(value)"""
        
        
class DvTime(DvTemporal):
    u"""
    Represents an absolute point in time from an origin usually interpreted as meaning the start 
    of the current day, specified to the second. Semantics defined by ISO8601.
    
    Used for recording real world times, rather than scientifically measured fine
    amounts of time. The partial form is used for approximate times of events and
    substance administrations. 
    """

    implements(IDvTime)

    def __init__(self,value):
        self.value=time(value)

    def diff(self,other):
        u"""Difference of two times. Returns a DvDuration"""
        return other-self.value
        
        
    def magnitude(self):
        u"""
        Returns the numeric value of the seconds since midnight.
        Result >= 0.0        
        """
        n=time.localtime()
        y,m,d,z=n[0],n[1],n[2],n[8]
        return time.mktime(n)-time.mktime((y,m,d,0,0,0,0,z))


    def valueValid(self): 
        u"""validIso8601Time(value)"""
        return True
    


class DvText(DataValue):
    """
    A text item, which may contain any amount of legal characters arranged as e.g.
    words, sentences etc (i.e. one DV_TEXT may be more than one word). Visual for-
    matting and hyperlinks may be included.
    A DV_TEXT can be "coded" by adding mappings to it.
    Fragments of text, whether coded or not are used on their own as values, or to
    make up larger tracts of text which may be marked up in some way, eventually
    going to make up paragraphs.

    >>> from oship.openehr.datatypes import DvText
    >>> t=DvText("Text")
    >>> t.value
    'Text'
    >>> t.mappings
    >>> t.formatting
    >>> t.hyperlink
    >>> t.language
    >>> t.encoding
    >>> t=DvText("Different Text",None,None,None,"en-us",None)
    >>> t.value
    'Different Text'
    >>> t.mappings
    >>> t.formatting
    >>> t.hyperlink
    >>> t.language
    'en-us'
    >>> t.encoding
    
    """

    implements(IDvText)
    
    def __init__(self,value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None):
        self.value = value
        self.mappings = mappings
        self.formatting = formatting
        self.hyperlink = hyperlink
        self.language = language
        self.encoding = encoding
     
   
       
        
       
class CodePhrase(grok.Model):
    """
    A fully coordinated (i.e. all "coordination" has been performed) term from a ter-
    minology service (as distinct from a particular terminology).
    
    Simple doctest:
    
    >>> from oship.openehr.datatypes import CodePhrase
    >>> from oship.openehr.support import TerminologyId
    >>> tid = TerminologyId(u"SNOMED-CT(2003)")
    >>> cp = CodePhrase(tid,u"abc123")
    >>> cp.terminologyId.name()
    u'SNOMED-CT'
    >>> cp.terminologyId.versionId()
    u'2003'
    >>> tid = TerminologyId(1234)
    AttributeError: 'int' object has no attribute 'partition'    
    """
    
    implements(ICodePhrase)
    
    def __init__(self, terminologyId, codeString):
        
        self.terminologyId=terminologyId
        self.codeString=codeString

        
    def __eq__(self, other):
        if  not isinstance(other, CodePhrase):
            return False
        if self.codeString != other.codeString:
            return False
        return self.terminologyId == other.terminologyId

        


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
    
    
    >>> from oship.openehr.datatypes import *
    >>> from oship.openehr.support import *
    >>> tid = TerminologyId(u"SNOMED-CT(2003)")
    >>> cp = CodePhrase(tid,u"abc123")
    >>> dct=DvCodedText(cp,cp.codeString)
    >>> dct.value==cp.codeString
    True
    >>> dct.definingCode==cp
    True
    
    
    """

    implements(IDvCodedText)
    
    def __init__(self, definingCode,value, mappings=None, formatting=None, hyperlink=None, language=None, encoding=None):
        self.definingCode=definingCode
        self.value = value
        self.mappings = mappings
        self.formatting = formatting
        self.hyperlink = hyperlink
        self.language = language
        self.encoding = encoding

        
class IDvParagraph(Interface):
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
    
                

class TermMapping(DataValue):
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
    
    def __init__(self,target,match,purpose):
        self.target = target       
        self.purpose = purpose
        if match in ['<','>','=','?']:
            self.match = match
        else:
            raise AttributeError(_('Invalid match parameter'))
        
        
    def narrower():
        return self.match == '<'
    
    def equivalent():
        return self.match == '='
    
    def broader():
        return self.match == '>'
    
    def unknown():
        return self.match == '?'
    
    def isValidMatchCode(match):
        " I see no purpose in this method. twc"
        return match in ['<','>','=','?']

    
#Begin the timespecification package
class IDvTimeSpecification(Interface):
    """
    This is an abstract class of which all timing specifications are specialisations.
    Specifies points in time, possibly linked to the calendar, or a real world repeating
    event, such as "breakfast".
    """
    
    value = Object(
        schema=IDvParsable,
        title=_(u"value"),
        description=_(u"""the specification, in the HL7v3 syntax for PIVL or EIVL types. 
                    See section 8.2.2.1 Phase-linked Time Specification Syntax"""),
        required=True
    )
    
    def calendarAlignment():
        """Indicates what prototypical point in the calendar the specification is
        aligned to, e.g. "5th of the month". Empty if not aligned. Extracted from 
        the 'value' attribute.
        """
        
    def eventAlignment():
        """Indicates what real-world event the specification is aligned to if any.
        Extracted from the 'value' attribute.
        """
        
    def institutionSpecified():
        """Indicates if the specification is aligned with institution schedules, 
        e.g. a hospital nursing changeover or meal serving times. Extracted from 
        the 'value' attribute.
        """
        
        
class DvTimeSpecification(DataValue):
    u"""
    This is an abstract class of which all timing specifications are specialisations.
    Specifies points in time, possibly linked to the calendar, or a real world repeating
    event, such as "breakfast".
    """
    
    implements(IDvTimeSpecification)
    
    def __init__(self,value):
        self.value=value
    
    def calendarAlignment(self):
        u"""Indicates what prototypical point in the calendar the specification is
        aligned to, e.g. "5th of the month". Empty if not aligned. Extracted from 
        the 'value' attribute.
        """
        
    def eventAlignment(self):
        u"""Indicates what real-world event the specification is aligned to if any.
        Extracted from the 'value' attribute.
        """
        
    def institutionSpecified(self):
        u"""Indicates if the specification is aligned with institution schedules, 
        e.g. a hospital nursing changeover or meal serving times. Extracted from 
        the 'value' attribute.
        """
        
    def valueValid(self):
        u"""value != None"""

class IDvGeneralTimeSpecification(Interface):
    """Specifies points in time in a general syntax. Based on the HL7v3 GTS data type."""
    
    def calendarAlignment():
        """Calendar alignment extracted from value. """
        
    def eventAlignment():
        """Event alignment extracted from value."""
        
    def institutionSpecified():
        """Extracted from value."""
        
    def valueValid():
        """value.formalism.is_equal("HL7:GTS")"""


        
class DvGeneralTimeSpecification(DvTimeSpecification):
    u"""Specifies points in time in a general syntax. Based on the HL7v3 GTS data type."""

    implements(IDvGeneralTimeSpecification)

    def __init__(self,value):
        DvTimeSpecification.__init__(self,value)     

    def calendarAlignment(self):
        u"""Calendar alignment extracted from value. """

    def eventAlignment(self):
        u"""Event alignment extracted from value."""

    def institutionSpecified(self):
        u"""Extracted from value."""

    def valueValid(self):
        u"""value.formalism.is_equal("HL7:GTS")"""
        
        
class IDvPeriodicTimeSpecification(Interface):
    """
    Specifies periodic points in time, linked to the calendar (phase-linked), 
    or a real world repeating event, such as "breakfast" (event-linked). 
    Based on the HL7v3 data types PIVL<T> and EIVL<T>.
    Used in therapeutic prescriptions, expressed as INSTRUCTIONs in the openEHR model.
    """
    
    def period():
        """The period of the repetition, computationally derived from the syntax 
        representation. Extracted from the 'value' attribute. Returns a DvDuration.
        """

    def calendarAlignment():
        """Calendar alignment extracted from value."""


    def eventAlignment():
        u"""Event alignment extracted from value."""
        
    def institutionSpecified():
        """Extracted from value. """
        
    def valueValid():
        """value.formalism.is_equal("HL7:PIVL") or value.formalism.is_equal("HL7:EIVL")"""

    
class DvPeriodicTimeSpecification(DvTimeSpecification):
    u"""
    Specifies periodic points in time, linked to the calendar (phase-linked), 
    or a real world repeating event, such as "breakfast" (event-linked). 
    Based on the HL7v3 data types PIVL<T> and EIVL<T>.
    Used in therapeutic prescriptions, expressed as INSTRUCTIONs in the openEHR model.
    """
    
    implements(IDvPeriodicTimeSpecification)

    def __init__(self,value):
        DvTimeSpecification.__init__(self,value)
    
    def period(self):
        u"""The period of the repetition, computationally derived from the syntax 
        representation. Extracted from the 'value' attribute.
        """

    def calendarAlignment(self):
        u"""Calendar alignment extracted from value."""


    def eventAlignment(self):
        u"""Event alignment extracted from value."""
        
    def institutionSpecified(self):
        u"""Extracted from value. """
        
    def valueValid(self):
        u"""value.formalism.is_equal("HL7:PIVL") or value.formalism.is_equal("HL7:EIVL")"""
        
        
class DvUri(DataValue,URI):
    """A reference to an object which conforms to the Universal Resource Identifier
    (URI) standard, as defined by W3C RFC 2936. See "Universal Resource Identifiers in WWW"
    by Tim Berners-Lee at http://www.ietf.org/rfc/rfc2396.txt. This is a World-Wide Web RFC 
    for global identification of resources. See http://www.w3.org/Addressing for a starting 
    point on URIs. See http://www.ietf.org/rfc/rfc2806.txt for new URI types like telephone, 
    fax and modem numbers.
    
    Enables external resources to be referenced from within the content of the EHR. A number 
    of functions return the logical subparts of the URI string."""
    
    implements(IDvUri)

    def __init__(self, value):
        if URI._validate(value):
            self.value=value
        else:
            raise AttributeError(_("Invalid URI"))
 
    
    def scheme(self):
        """A distributed information "space" in which information objects exist. The scheme 
        simultaneously specifies an information space and a mechanism for accessing objects 
        in that space. For example if scheme = "ftp", it identifies the information space in 
        which all ftpable objects exist, and also the application - ftp - which can be used 
        to access them. Values may include: "ftp", "telnet", "mailto", "gopher" and many others. 
        Refer to WWW URI RFC for a full list. New information spaces can be accommodated within 
        the URI specification."""
        
        
    def path(self):
        u"""A string whose format is a function of the scheme. Identifies the location in 
        <scheme>-space of an information entity. Typical values include hierarchical directory 
        paths for any machine. For example, with scheme = "ftp", path might be /pub/images/image_01. 
        The strings "." and ".." are reserved for use in the path. Paths may include internet/intranet 
        location identifiers of the form: sub_domain...domain, e.g. "info.cern.ch" """

    def fragmentId(self):
        u"""A part of, a fragment or a sub-function within an object. Allows references to sub-parts 
        of objects, such as a certain line and character position in a text object. The syntax and 
        semantics are defined by the application responsible for the object. """


    def query(self):
        u"""Query string to send to application implied by scheme and path Enables queries to 
        applications, including databases to be included in the URI Any query meaningful to the 
        server, including SQL."""
        

    def valueExists(self):
        u"""value != None and value != '' """
        
 

class IDvEhrUri(Interface):
    """
    A DvEhrUri is a DvUri which has the scheme name "ehr", and which can only reference 
    elements in EHRs. The syntax is described below.
    
    Used to reference elements in an EHR, which may be the current one, or another.
    
    The syntax of a DV_EHR_URI is an openEHR path, inside the "ehr" URI scheme-space, and is 
    of the form: "ehr://" ehr_path
    The syntax of ehr_path is described in the section on Paths in The openEHR Architecture Overview 
    document. DV_EHR_URIs are used as a mechanism for referencing in the EHR, ensuring readability by 
    humans, as well as validity when extracts are transmitted elsewhere: even if the target of a path 
    is not present, the path can be used to locate the missing item on demand.
    """
    
    def schemeIsEhr():
        """ Ensure scheme == 'ehr' """
        
       
class DvEhrUri(DvUri):
    u"""
    A DvEhrUri is a DvUri which has the scheme name ehr, and which can only reference 
    elements in EHRs. The syntax is described below.
    
    Used to reference elements in an EHR, which may be the current one, or another.
    
    The syntax of a DV_EHR_URI is an openEHR path, inside the ehr URI scheme-space, and is 
    of the form: ehr:// ehr_path
    The syntax of ehr_path is described in the section on Paths in The openEHR Architecture Overview 
    document. DV_EHR_URIs are used as a mechanism for referencing in the EHR, ensuring readability by 
    humans, as well as validity when extracts are transmitted elsewhere: even if the target of a path 
    is not present, the path can be used to locate the missing item on demand.
    """
    def __init__(self,value,path,fragmentId,query,scheme=u"ehr"):
        self.value=value
        self.scheme=scheme 
        self.path=path
        self.fragmentId=fragmentId
        self.query=query
    
    def schemeIsEhr(self):
        u""" Ensure scheme == 'ehr' """
        return self.scheme == 'ehr'

        
        
