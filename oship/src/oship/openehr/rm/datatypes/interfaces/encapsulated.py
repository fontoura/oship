# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

These are the interfaces for the encapsulated data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.interface import *
from zope.schema.interfaces import IDate, IDatetime, ITime, ITimedelta
from zope.schema import Int,TextLine,BytesLine,Dict
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.interfaces.basic import IDataValue
from openehr.rm.datatypes.interfaces.quantity import *
from openehr.rm.datatypes.uri import DvUri
from openehr.rm.datatypes.thumbnail import ThumbNail

_ = MessageFactory('oship')


class IDvEncapsulated(IDataValue):
    """Abstract class defining the common meta-data of all types of encapsulated data."""
    
    size = Int(
        title=_(u"Size"),
        description=_(u"""Original size in bytes of unencoded encapsulated data. I.e. encodings 
                      such as base64, hexadecimal etc do not change the value of this attribute."""),
        required=True,
        )
    
    charset = CodePhrase('','',
        title=_(u"charset"),
        description=_(u"""Name of character encoding scheme in which this value is encoded. 
                      Coded from openEHR Code Set character sets. Unicode is the default assumption 
                      in openEHR, with UTF-8 being the assumed encoding. This attribute allows for 
                      variations from these assumptions. Type==CodePhrase"""),
        required=False,
        )
    
    language = CodePhrase('','',
        title=_(u"Language"),
        description=_(u"""Optional indicator of the localised language in which the data 
                      is written, if relevant. Coded from openEHR Code Set languages. Type==CodePhrase"""),
        required=False
        )
    
    def asString():
        """Result = alternate_text [(uri)]"""
        
    def sizePositive():
        """size >= 0"""
        
    def languageValid():
        """language /= Void implies code_set(Code_set_id_languages).has_code(language)"""
        
    def charsetValid():
        """charset /= Void implies code_set(Code_set_id_character_sets).has_code(charset)"""
        
class IDvMultimedia(IDvEncapsulated):
    """
    A specialisation of DvEncapsulated for audiovisual and biosignal types. Includes further 
    metadata relating to multimedia types which are not applicable to other subtypes of DvEncapsulated.
    """
    
    alternateText = TextLine(
        title=_(u"Alternate Text"),
        description=_(u"""Text to display in lieu of multimedia display/replay"""),
        required=False,
        )
    
    mediaType = CodePhrase('','',
        title=_(u"Media Type"),
        description=_(u"""Data media type coded from openEHR code set media types (interface for the IANA MIME types code set)."""),
        required=True,
        )
    
    compressionAlgorithm = CodePhrase('','',
        title=_(u"Compression Algorithm"),
        description=_(u"""Compression type, a coded value from the openEHR Integrity check code set. Void means no compression."""),
        required=False,
        )
    
    integrityCheck=Dict(
        title=_(u"Integrity Check"),
        description=_(u"""Binary cryptographic integrity checksum. Type==Array<Octet>"""),
        required=False,
        )
    
    integrityCheckAlgorithm = CodePhrase('','',
        title=_(u"Integrity Check Algorithm"),
        description=_(u"""Type of integrity check, a coded value from the openEHR Integrity check code set."""),
        required=False,
        )
    
    thumbnail = ThumbNail('','','','','','','','','','',
        title=_(u"Thumbnail"),
        description=_(u"""The thumbnail for this item, if one exists; mainly for graphics formats. Type == DvMultimedia"""),
        required=False,
        )
    
    uri = DvUri('','','','','',
        title=_(u"URI"),
        description=_(u"""URI reference to electronic information stored outside the record as a file,database entry etc, if supplied as a reference. Type == DvUri."""),
        required=False,
        )
    
    data = BytesLine(
        title=_(u"Data"),
        description=_(u"""The actual data found at uri, if supplied inline. Type==Array<Octet>"""),
        required=False,
        )
    
    def isExternal():
        """Computed from the value of the uri attribute: True if the data is stored externally 
        to the record, as indicated by uri'. A copy may also be stored internally, in which case 
        isExpanded' is also true.  Ensure uri !=None and uri != '' """
        
    def isInline():
        """Computed from the value of the data attribute: True if the data is stored in expanded 
        form, ie within the EHR itself. Ensure data != None. """
        
    def isCompressed():
        """Computed from the value of the compression_algorithm attribute: True if the data is 
        stored in compressed form. Ensure compressionAlgorithm != None. """
        
    def hasIntegrityCheck():
        """Computed from the value of the integrityCheckAlgorithm attribute: True if an 
        integrity check has been computed. Ensure integrityCheckAlgorithm != None."""
        
    
class IDvParsable(IDvEncapsulated):
    """
    Encapsulated data expressed as a parsable String. The internal model of the data item is not 
    described in the openEHR model in common with other encapsulated types, but in this case, the 
    form of the data is assumed to be plaintext, rather than compressed or other types of large binary data.
    Used for representing values which are formal textual representations, e.g. guidelines.
    """

    size=Int(
        title=_(u"Size"),
        description=_(""" """),
        required=True,
        )

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""The string, which may validly be empty in some syntaxes"""),
        required=True,
        )
    
    formalism = TextLine(
        title=_(u"Formalism"),
        description=_(u"""The name of the formalism, e.g. GLIF 1.0, proforma etc."""),
        required=True,
        )
    
    def valueValid():
        """value != None."""

    def formalismValidity():
        """formalism != None and formalism != '' """
