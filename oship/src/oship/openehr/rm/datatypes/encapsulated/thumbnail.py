# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

Implementation for the encapsulated data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.interface import implements,classProvides 
from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Field
from openehr.rm.datatypes.basic import DataValue
from openehr.rm.datatypes.interfaces.thumbnail import IThumbNail

_ = MessageFactory('oship')
       
class ThumbNail(object):
    """
    A DvMultimedia equivalent without the thumbnail attribute to be used as the the thumbnail in DvMultimedia 
    """
    
    implements(IThumbNail)
    classProvides(IThumbNail)
    
    def __init__(self,size,charset,language,altTxt,mType,compAlg,intChk,intChkAlg,uri,data):
        self.size=size
        self.charset=charset
        self.language=language
        self.alternateText=altTxt
        self.mediaType=mType
        self.integrityCheck=intChk
        self.integrityCheckAlgorithm=intChkAlg
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
