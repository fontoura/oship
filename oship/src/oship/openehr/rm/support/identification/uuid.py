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

from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory 

from uid import Uid
from interfaces.uuid import IUuid

_ = MessageFactory('oship')

class Uuid(Uid):
    u"""
    Model of the DCE Universal Unique Identifier or UUID which takes the form of
    hexadecimal integers separated by hyphens, following the pattern 8-4-4-4-12 as
    defined by the Open Group, CDE 1.1 Remote Procedure Call specification,
    Appendix A. Also known as a GUID.
    """

    implements(IUuid)
   
    def __init__(self, value):
        self.value = value

