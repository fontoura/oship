# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


from zope.interface import implements 
from zope.schema import TextLine,BytesLine
from zope.i18nmessageid.message import MessageFactory 


from openehr.rm.datatypes.encapsulated.interfaces.dvencapsulated import IDvEncapsulated
from openehr.rm.datatypes.text.codephrase import CodePhrase
from openehr.rm.datatypes.uri.dvuri import DvUri

_=MessageFactory('oship')
        
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
        description=_(u"""     Data media type coded from openEHR code set “media types” 
        (interface for the IANA MIME types code set)."""),
        required=True,
        )
    
    compressionAlgorithm = CodePhrase('','',
        title=_(u"Compression Algorithm"),
        description=_(u"""Compression type, a coded value from the openEHR “Integrity check” 
        code set. Void means no compression."""),
        required=False,
        )
    
    integrityCheck = BytesLine(
        title=_(u"Integrity Check"),
        description=_(u"""Binary cryptographic integrity checksum. Type==Array<Octet>"""),
        required=False,
        )
    
    integrityCheckAlgorithm = CodePhrase('','',
        title=_(u"Integrity Check Algorithm"),
        description=_(u"""Type of integrity check, a coded value from the openEHR “Integrity check” code set."""),
        required=False,
        )
    
    thumbnail = DvMultimedia(
        title=_(u"Thumbnail"),
        description=_(u"""The thumbnail for this item, if one exists; 
                    mainly for graphics formats. Type == DvMultimedia"""),
        required=False,
        )
    
    uri = DvUri(
        title=_(u"URI"),
        description=_(u"""URI reference to electronic information stored outside the record as a file, 
        database entry etc, if supplied as a reference. Type == DvUri."""),
        required=False,
        )
    
    data = BytesLine(
        title=_(u"Data"),
        description=_(u"""The actual data found at uri, if supplied inline. Type==Array<Octet>"""),
        requires=False,
        )
    
    def isExternal():
        """Computed from the value of the uri attribute: True if the data is stored externally 
        to the record, as indicated by `uri'. A copy may also be stored internally, in which case 
        `isExpanded' is also true.  Ensure uri !=None and uri != '' """
        
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

    def __init__(self,altTxt,mType,compAlg,intChk,intChkAlg,tnail,uri,data):
        self.alternateText=altTxt
        self.mediaType=mType
        self.integrityCheck=intChk
        self.integrityCheckAlgorithm=intChkAlg
        self.thumbnail=tnail
        self.uri=uri
        self.data=data
   
    def isExternal():
        u"""Computed from the value of the uri attribute: True if the data is stored externally 
        to the record, as indicated by `uri'. A copy may also be stored internally, in which case 
        `isExpanded' is also true.  Ensure uri !=None and uri != '' """
        
    def isInline():
        u"""Computed from the value of the data attribute: True if the data is stored in expanded 
        form, ie within the EHR itself. Ensure data != None. """
        
    def isCompressed():
        u"""Computed from the value of the compression_algorithm attribute: True if the data is 
        stored in compressed form. Ensure compressionAlgorithm != None. """
        
    def hasIntegrityCheck():
        u"""Computed from the value of the integrityCheckAlgorithm attribute: True if an 
        integrity check has been computed. Ensure integrityCheckAlgorithm != None."""
                 
    def mediaTypeValidity(): 
        u"""mediaType != None and mediaType in codeSetIdMediaTypes"""
        
    def compressionAlgorithmValidity():
        u"""compressionAlgorithm != None and compressionAlgorithm in codeSetIdCompressionAlgorithms."""
        
    def integrityCheckValidity():
        u"""integrityCheck != None and integrityCheckAlgorithm != None"""
        
    def integrityCheckAlgorithmValidity():
    u"""integrityCheckAlgorithm  != None and integrityCheckAlgorithm in codeSetIdIntegrityCheckAlgorithms"""
