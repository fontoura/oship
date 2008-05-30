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


from zope.interface import implements 
from zope.schema import Field 
from zope.i18nmessageid.message import MessageFactory 

from openehr.rm.datatypes.basic import DataValue
from openehr.rm.datatypes.interfaces.encapsulated import IDvMultimedia
from openehr.rm.datatypes.interfaces.encapsulated import IDvEncapsulated
from openehr.rm.datatypes.interfaces.encapsulated import IDvParsable


_ = MessageFactory('oship')

class DvEncapsulated(DataValue):
    """Abstract class defining the common meta-data of all types of encapsulated data."""

    implements(IDvEncapsulated)

    def __init__(self,size,charset,language):
        self.size=size
        self.charset=charset
        self.language=language
    
    def asString():
        u"""Result = alternate_text [(uri)]"""
        
    def sizePositive():
        u"""size >= 0"""
        
    def languageValid():
        u"""language /= Void implies code_set(Code_set_id_languages).has_code(language)"""
        
    def charsetValid():
        u"""charset /= Void implies code_set(Code_set_id_character_sets).has_code(charset)"""
        
class DvMultimedia(DvEncapsulated):
    """
    A specialisation of DvEncapsulated for audiovisual and biosignal types. Includes further 
    metadata relating to multimedia types which are not applicable to other subtypes of DvEncapsulated.
    """
    
    implements(IDvMultimedia)

    def __init__(self,altTxt,mType,compAlg,intChk,intChkAlg,tnail,uri,data,**kwargs):
        self.alternateText=altTxt
        self.mediaType=mType
        self.integrityCheck=intChk
        self.integrityCheckAlgorithm=intChkAlg
        self.thumbnail=tnail
        self.uri=uri
        self.data=data
        Field.__init__(self,**kwargs)

    
    
    
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
    
class DvParsable(DvEncapsulated):
    u"""
    Encapsulated data expressed as a parsable String. The internal model of the data item is not 
    described in the openEHR model in common with other encapsulated types, but in this case, the 
    form of the data is assumed to be plaintext, rather than compressed or other types of large binary data.
    Used for representing values which are formal textual representations, e.g. guidelines.
    """
    
    implements(IDvParsable)

    def __init__(self,size,value,formalism,**kwargs):
        self.size=size
        self.value=value
        self.formalism=formalism
        Field.__init__(self,**kwargs)

    def valueValid():
        u"""value != None."""

    def formalismValidity():
        u"""formalism != None and formalism != '' """
