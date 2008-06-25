# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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

from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from careentry import ICareEntry

_ = MessageFactory('oship')

class IEvaluation(ICareEntry):
    """
    Entry type for evaluation statements.
    """
    
    data=ItemStructure(
        title=_("Data"),
        description=_("The data of this evaluation."),
        required=True,
    )
    
