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

from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from uidbasedid import UidBasedId
from interfaces.hierobjectid import IHierObjectId

_ = MessageFactory('oship')


class HierObjectId(UidBasedId):
    u"""
    Concrete type corresponding to hierarchical identifiers of the form defined by UID_BASED_ID.
    """

    implements(IHierObjectId)
    classProvides(IHierObjectId)

    def __init__(self):
        self.__name__=''

