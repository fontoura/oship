# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

The interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import Object

from oship.openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from careentry import ICareEntry

_ = MessageFactory('oship')

class IEvaluation(ICareEntry):
    """
    Entry type for evaluation statements.
    """
    
    data=Object(
        schema=IItemStructure,
        title=_(u"Data"),
        description=_(u"The data of this evaluation."),
        required=True,
    )
    