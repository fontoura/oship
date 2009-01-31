# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.datatypes.basic.datavalue import DataValue
from oship.openehr.rm.datatypes.text.codephrase import CodePhrase
from oship.openehr.rm.datatypes.encapsulated.interfaces.dvencapsulated import IDvEncapsulated

_=MessageFactory('oship')

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
 