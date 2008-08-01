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
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.datatypes.encapsulated.dvencapsulated import DvEncapsulated
from interfaces.dvmultimedia import IDvMultimedia

_=MessageFactory('oship')
    
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
        to the record, as indicated by 'uri'. A copy may also be stored internally, in which case 
        'isExpanded' is also true.  Ensure uri !=None and uri != '' """
        
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
