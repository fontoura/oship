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


class IGenericId(IObjectId):
    u"""
    Generic identifier type for identifiers whose format is othterwise unknown to openEHR. 
    Includes an attribute for naming the identification scheme (which may well be local).
    """

    scheme = TextLine(
        title = _(u"Scheme"),
        description = _(u"Name of the scheme to which this identifier conforms."),
        required = True
        )
            
    def schemeValid():
        u""" scheme != None and scheme != ''  """
        
