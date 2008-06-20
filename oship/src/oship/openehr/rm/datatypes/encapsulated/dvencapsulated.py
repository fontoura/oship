# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the encapsulated data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


from zope.interface import implements 
from zope.schema import Int
from zope.i18nmessageid.message import MessageFactory 

from openehr.rm.datatypes.datavalue import DataValue,IDataValue
from openehr.rm.datatypes.codephrase import CodePhrase

_=MessageFactory('oship')

class IDvEncapsulated(IDataValue):
    """Abstract class defining the common meta-data of all types of encapsulated data."""
    
    size = Int(
        title=_(u"Size"),
        description=_(u"""Original size in bytes of unencoded encapsulated data. I.e. encodings 
                    such as base64, hexadecimal etc do not change the value of this attribute."""),
        required=True,
        )
    
    charset = CodePhrase(
        title=_(u"charset"),
        description=_(u"""Name of character encoding scheme in which this value is encoded. 
        Coded from openEHR Code Set “character sets”. Unicode is the default assumption 
        in openEHR, with UTF-8 being the assumed encoding. This attribute allows for 
        variations from these assumptions. Type==CodePhrase"""),
        required=False,
        )
    
    language = CodePhrase(
        title=_(u"Language"),
        description=_(u"""Optional indicator of the localised language in which the data 
                    is written, if relevant. Coded from openEHR Code Set “languages”. Type==CodePhrase"""),
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

    def __init__(self,size,charset,language):
        self.size=size
        self.charset=charset
        self.language=language
    
    def asString():
        u"""Result = alternate_text [(uri)]"""
        
    def sizePositive():
        u"""size >= 0"""
        return size>0
        
    def languageValid():
        u"""language /= Void implies code_set(Code_set_id_languages).has_code(language)"""
        
    def charsetValid():
        u"""charset /= Void implies code_set(Code_set_id_character_sets).has_code(charset)"""
 