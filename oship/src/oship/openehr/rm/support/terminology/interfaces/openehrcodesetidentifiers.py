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

from zope.interface import Interface
from zope.schema import TextLine

from zope.i18nmessageid.message import MessageFactory 


_ = MessageFactory('oship')


class IOpenehrCodeSetIdentifiers(Interface):
    u""" 
    List of identifiers for code sets in the openEHR terminology. 
    In the specs these are strings.  But it makes more sense to implement them as Lists
    with one class instance in OSHIP SUPPORT site.    
    """
        
    
    codeSetIdCharacterSets = TextLine(
        title=_(u"Code Set Id Character Sets"),
        description=_(u"character sets"),
        readonly=True,
        default=u"character sets",
        )
        
    codeSetIdCompressionAlgorithms = TextLine(
        title=_(u"Code Set Id Compression Algorithms"),
        description=_(u"compression algorithms"),
        readonly=True,
        default=u"compression algorithms",
        )
    
    codeSetIdCountries = TextLine(
        title=_(u"Code Set Id Countries"),
        description=_(u"countries"),
        readonly=True,
        default=u"countries",
        )
    
    codeSetIdIntegrityCheckAlgorithms = TextLine(
        title=_(u"Code Set Id Integrity Check Algorithms"),
        description=_(u"integrity check algorithms"),
        readonly=True,
        default=u"integrity check algorithms",
        )
    
    codeSetIdLanguages = TextLine(
        title=_(u"Code Set Id Languages"),
        description=_(u"languages"),
        readonly=True,
        default=u"languages",
        )
        
    codeSetIdMediaTypes = TextLine(
        title=_(u"Code Set Id Media Types"),
        description=_(u"media types"),
        readonly=True,
        default="media types",
        )
        
    codeSetIdNormalStatuses = TextLine(
        title=_(u"Code Set Id Normal Statuses"),
        description=_(u"normal statuses"),
        readonly=True,
        default=u"normal statuses",
        )


    def validCodeSetId(an_id):
        u"""
        Boolean Validity function to test if an identifier is in 
        the set defined by this class.
        """
