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

from zope.schema.interfaces import IField
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class IUid(IField):
    u"""
    Abstract parent of classes representing unique identifiers which identify informa-
    tion entities in a durable way. UIDs only ever identify one IE in time or space and
    are never re-used.
    """
    
    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid UID"),
        default=_(u""),
        required=True)

    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
            