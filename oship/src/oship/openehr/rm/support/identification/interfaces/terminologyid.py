# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

from objectid import IObjectId

_ = MessageFactory('oship')


class ITerminologyId(IObjectId):
    u"""
    Identifier for terminologies such accessed via a terminology query service. In this
    class, the value attribute identifies the Terminology in the terminology service,
    e.g. "SNOMED-CT". A terminology is assumed to be in a particular language,
    which must be explicitly specified.
    
    The value if the id attribute is the precise terminology id identifier, including
    actual release (i.e. actual "version"), local modifications etc; e.g. "ICPC2".
    Lexical form: name [ '(' version ')' ]
    """

    name = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        required=True)

    versionId = TextLine(
        title=_(u"Version"),
        description=_(u"A single unicode string containing a valid version if supported. Otherwise and empty string."),
        default=u'',        
        required=True)
   
    def valueExists():
        u"""        
        value != None and then not value != ''
        """

    def name():
        u"""
        Return the terminology id (which includes the "version" in some cases). 
        Distinct names correspond to distinct (i.e. non-compatible) terminologies.
        Thus the names "ICD10AM" and "ICD10" refer to distinct terminologies.
        """
        
    def versionId():
        u""" Version of this terminology, if versioning supported, else the empty string."""
        
    
    def nameValid():
        u""" name != None and name != '' """

    def versionIdValid():
        u""" versionId != None """
        