# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

Interfaces for the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema.interfaces import IField
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 


_ = MessageFactory('oship')


class IObjectId(IField):
    u"""
    Ancestor (abstract) class of identifiers of informational objects. Ids may be completely
    meaningless, in which case their only job is to refer to something, or may carry
    some information to do with the identified object.
    Object ids are used inside an object to identify that object. To identify another
    object in another service, use an OBJECT_REF, or else use a UID for local objects
    identified by UID. If none of the subtypes is suitable, direct instances of this class
    may be used.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        required=False,
    )

