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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'


from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory 

from interfaces.objectid import IObjectId

_ = MessageFactory('oship')

class ObjectId(object):
    u"""
    Ancestor (abstract) class of identifiers of informational objects. Ids may be completely
    meaningless, in which case their only job is to refer to something, or may carry
    some information to do with the identified object.
    Object ids are used inside an object to identify that object. To identify another
    object in another service, use an OBJECT_REF, or else use a UID for local objects
    identified by UID. If none of the subtypes is suitable, direct instances of this class
    may be used.
    """

    implements(IObjectId)

    def __init__(self, value):
        self.value = value
 