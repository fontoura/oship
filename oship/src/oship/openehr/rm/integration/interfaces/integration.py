# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Defines the interfaces for the integration package in integration_im.pdf Rev. 0.6

"""
__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


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
     
         

