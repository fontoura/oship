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

from uidbasedid import UidBasedId
from uuid import Uuid
from internetid import InternetId
from isooid import IsoOid
import re
from interfaces.hierobjectid import IHierObjectId

_ = MessageFactory('oship')


class HierObjectId(UidBasedId):
    u"""
    Concrete type corresponding to hierarchical identifiers of the form defined by UID_BASED_ID.
    """

    implements(IHierObjectId)

    def __init__(self, value):
        self.__name__=''
        self.value = value
        doubleColons = value.find('::')
        # Check for root segment
        if doubleColons == 0:
            raise ValueError('bad format, missing root')

        elif doubleColons > 0:
            rootStr = value[0:doubleColons]
        else:
            rootStr = value

        matchUUID = re.compile(self.SIMPLE_UUID_PATTERN).match(rootStr)
        matchISO = re.compile(self.SIMPLE_ISOOID_PATTERN).match(rootStr)
        matchInternet = re.compile(self.SIMPLE_INTERNET_PATTERN).match(rootStr)
        if (matchUUID is not None) and (matchUUID.start() == 0) and (matchUUID.end() == len(rootStr)):
            self.rootPart = Uuid(rootStr)
        elif (matchISO is not None) and (matchISO.start() == 0) and (matchISO.end() == len(rootStr)):
            self.rootPart = IsoOid(rootStr);
        elif (matchInternet is not None) and (matchInternet.start() == 0) and (matchInternet.end() == len(rootStr)):
            self.rootPart = InternetId(rootStr);
        else:
            raise ValueError("wrong format")
        
        if (0 < doubleColons) and (doubleColons < (len(value) - 2)):
            self.extensionPart = value[doubleColons + 2:]
        else:
            self.extensionPart = ''

