# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.schema import Bool,Object
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.generic.interfaces.partyself import IPartySelf
from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from oship.openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure

_ = MessageFactory('oship')

    
class IEhrStatus(ILocatable):
    """
    Instance providing various EHR wide status information.
    """
    
    subject=Object(
        schema=IPartySelf,
        title=_(u"Subject"),
        description=_(u"The subject of this EHR."),
        required=True,
    )
     
    isQueryable=Bool(
        title=_(u"Queryable"),
        description=_(u"True if this EHR can be included in population wide queries."),
        required=True,
    )
    
    isModifiable=Bool(
        title=_(u"Modifiable"),
        description=_(u"True if this EHR can be written to."),
        required=True,
    )
    
    otherDetails=Object(
        schema=IItemStructure,
        title=_(u"Other Details"),
        description=_(u"Any other details of the EHR summary."),
        required=False,
    )
    
   