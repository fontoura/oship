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
from interfaces.internetid import IInternetId

_ = MessageFactory('oship')

class InternetId(Uid):
    u"""
    Model of a reverse internet domain, as used to uniquely identify an internet
    domain. In the form of a dot-separated string in the reverse order of a domain
    name specified by IETF RFC1034 (http://www.ietf.org/rfc/rfc1034.txt).
    """
    
    implements(IInternetId)

    def __init__(self, value):
        self.value = value
