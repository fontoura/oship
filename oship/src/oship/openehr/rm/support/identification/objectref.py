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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire sergio@lampada.uerj.br'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.identification.objectid import ObjectId
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef

_ = MessageFactory('oship')

class ObjectRef(object):
    u"""
    Class describing a reference to another object, which may exist locally or be
    maintained outside the current namespace, e.g. in another service. Services are
    usually external, e.g. available in a LAN (including on the same host) or the inter-
    net via Corba, SOAP, or some other distributed protocol. However, in small sys-
    tems they may be part of the same executable as the data containing the Id.
    """

    implements(IObjectRef)
    
    def __init__(self,refId,refNameSpace,refType):
        self.refId=refId
        self.refNameSpace=refNameSpace
        self.refType=refType
        
    def __eq__(self, other):
        if not isinstance(other,  ObjectRef):
            return False
        if self.refId != other.refId:
            return False
        if self.refNameSpace != other.refNameSpace:
            return False
        return self.refType == other.refType
