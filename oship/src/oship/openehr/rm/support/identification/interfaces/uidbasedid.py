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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

from objectid import IObjectId

_ = MessageFactory('oship')


class IUidBasedId(IObjectId):
    u"""
    Abstract model of UID-based identifiers consisting of a root part and an optional
    extension; lexical form: root '::' extension
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        required=True)
    
    def root():
        u"""
        The identifier of the conceptual namespace in which the object exists, within 
        the identification scheme.
        Returns the part to the left of the first '::' separator, if any, or else the whole string.
        """

    def extension():
        u"""
        Optional local identifier of the object within the context of the root identifier.
        Returns the part to the right of the first '::' separator if any, or else any empty String.
        """

    def hasExtension():
        u""" True if extension != None """

