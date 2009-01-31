# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.schema import TextLine,Object
from zope.interface import Interface
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.identification.interfaces.objectid import IObjectId

_ = MessageFactory('oship')

class IObjectRef(Interface):
    u"""
    Class describing a reference to another object, which may exist locally or be
    maintained outside the current namespace, e.g. in another service. Services are
    usually external, e.g. available in a LAN (including on the same host) or the inter-
    net via Corba, SOAP, or some other distributed protocol. However, in small sys-
    tems they may be part of the same executable as the data containing the Id.
    """

    refId = Object(
        schema=IObjectId,
        title = _(u'Id'),
        description = _(u'Globally unique id of an object (of type ObjectId), regardless of where it is stored.'),
        required = False,
        )

    refNameSpace = TextLine(
        title = _(u"Namespace"),
        description = _(u"""Namespace to which this identifier belongs in
                        the local system context (and possibly in any
                        other openEHR compliant environment) e.g.
                        "terminology", "demographic". These names
                        are not yet standardised. Legal values for the
                        namespace are
                        "local" | "unknown" | "[a-zA-
                        Z][a-zA-Z0-9_-:/&+?]*" """),
        required = False,
        )


    refType = TextLine(
        title = _(u"Type"),
        description = _(u"""Name of the class (concrete or abstract) of object to which this 
                        identifier type refers, e.g."PARTY", "PERSON", "GUIDELINE" etc.
                        These class names are from the relevant reference model. 
                        The type name "ANY" can be used to indicate that any type is accepted 
                        (e.g. if the type is unknown). """),
        required = False,
        )
