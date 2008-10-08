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

from uid import IUid

_ = MessageFactory('oship')


class IIsoOid(IUid):
    u"""
    Model of ISO's Object Identifier (oid) as defined by the standard ISO/IEC 8824 .
    Oids are formed from integers separated by dots. Each non-leaf node in an Oid
    starting from the left corresponds to an assigning authority, and identifies that
    authority's namespace, inside which the remaining part of the identifier is locally unique.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid UID"),
        required=True)

