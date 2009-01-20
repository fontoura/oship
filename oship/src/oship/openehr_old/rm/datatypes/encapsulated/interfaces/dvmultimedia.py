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
from zope.schema import TextLine,BytesLine,Object,fieldproperty
from zope.i18nmessageid.message import MessageFactory 
from zope.app.file.interfaces import IImage

from oship.openehr.rm.datatypes.encapsulated.interfaces.dvencapsulated import IDvEncapsulated
from oship.openehr.rm.datatypes.text.interfaces.codephrase import ICodePhrase
from oship.openehr.rm.datatypes.uri.interfaces.dvuri import IDvUri

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
    
    mediaType = Object(
        schema=ICodePhrase,
        title=_(u"Media Type"),
        description=_(u"""Data media type coded from openEHR code set "media types" 
        (interface for the IANA MIME types code set)."""),
        required=True,
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
    
    thumbnail = Object(
        schema=IImage,
        title=_(u"Thumbnail"),
        description=_(u"""The thumbnail for this item, if one exists; 
                    mainly for graphics formats. Type == DvMultimedia"""),
        required=False,
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
        
