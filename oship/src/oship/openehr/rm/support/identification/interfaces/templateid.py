# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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


class ITemplateId(IObjectId):
    u""" Identifier for templates. Lexical form to be determined. """
    
    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        required=True,
    )    
