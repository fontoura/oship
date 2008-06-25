# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

These are the interface specifications from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.archetyped.locatable import Locatable

_ = MessageFactory('oship')

    
class EhrStatus(Locatable):
    """
    Instance providing various EHR wide status information.
    """
    
    subject=PartySelf(
        title=_("Subject"),
        description=_("The subject of this EHR."),
        required=True,
    )
     
    isQueryable=Bool(
        title=_("Queryable"),
        description=_("True if this EHR can be included in population wide queries."),
        required=True,
        default=True,
    )
    
    isModifiable=Bool(
        title=_("Modifiable"),
        description=_("True if this EHR can be written to."),
        required=True,
        default=True,
    )
    
    otherDetails=ItemStructure('',
        title=_("Other Details"),
        description=_("Any other details of the EHR summary."),
        required=False,
    )
    
   