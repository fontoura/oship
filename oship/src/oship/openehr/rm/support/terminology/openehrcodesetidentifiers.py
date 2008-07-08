# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from interfaces.openehrcodesetidentifiers import IOpenehrCodeSetIdentifiers

_ = MessageFactory('oship')


class OpenehrCodeSetIdentifiers(object):
    u""" 
    List of identifiers for code sets in the openEHR terminology. 
    In the specs these are strings.  But it makes more sense to implement them as Lists.    
    """

    implements(IOpenehrCodeSetIdentifiers)
    classProvides(IOpenehrCodeSetIdentifiers)
    
    def __init__(self,codeSetIdCharacterSets,codeSetIdCompressionAlgorithms,codeSetIdCountries,\
    codeSetIdIntegrityCheckAlgorithms,codeSetIdLanguages,codeSetIdMediaTypes,codeSetIdNormalStatuses,**kw):
        
        self.codeSetIdCharacterSets=codeSetIdCharacterSets
        self.codeSetIdCompressionAlgorithms=codeSetIdCompressionAlgorithms
        self.codeSetIdCountries=codeSetIdCountries
        self.codeSetIdIntegrityCheckAlgorithms=codeSetIdIntegrityCheckAlgorithms
        self.codeSetIdLanguages=codeSetIdLanguages
        self.codeSetIdMediaTypes=codeSetIdMediaTypes
        self.codeSetIdNormalStatuses=codeSetIdNormalStatuses
        for n,v in kw.items():
            setattr(self,n,v)
        
        

    def validCodeSetId(anId):
        u"""
        Boolean Validity function to test if an identifier is in 
        the set defined by this class.
        """
        
