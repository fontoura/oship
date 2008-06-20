# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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


from zope.interface import Interface
from zope.schema import Field

class IGenericEntry(Interface):
    """
    This class is used to create intermediate representations of data from sources not
    otherwise conforming to openEHR classes, such as HL7 messages, relational databases and so on.
    """

    data = Field(
       title=u"Data",
       description=u"an ITEM_TREE - The ‘data’ from the source message or record.",
       required =True,
       )

class GenericEntry(object):
    """
    This class is used to create intermediate representations of data from sources not
    otherwise conforming to openEHR classes, such as HL7 messages, relational databases and so on.
    """

    def __init__(self, data,**kw):
        self.data=data
        for n,v in kw.items():
            setattr(self,n,v)
