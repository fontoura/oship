# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the integration package in integration_im.pdf Rev. 0.6

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

import grok

from zope.interface import Interface
from zope.schema import Field,Object
from zope.i18nmessageid import MessageFactory

from datastructure import IItemTree

_ = MessageFactory('oship')

class IGenericEntry(Interface):
    """
    This class is used to create intermediate representations of data from sources not
    otherwise conforming to openEHR classes, such as HL7 messages, relational databases and so on.
    """

    data = Object(
        schema=IItemTree,
       title=_(u"Data"),
       description=_(u"an ITEM_TREE - The 'data' from the source message or record."),
       
       )

    

class GenericEntry(object):
    """
    This class is used to create intermediate representations of data from sources not
    otherwise conforming to openEHR classes, such as HL7 messages, relational databases and so on.
    """

    def __init__(self, data):
        self.data=data
