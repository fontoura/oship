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

from zope.schema import TextLine,Object,List
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable

_ = MessageFactory('oship')

    
class IEhrAccess(ILocatable):
    """
    EHR-wide access control object. Contains all policies and rules for access to data in this EHR.
    """
       
    settings=List(
        title=_("Settings"),
        description=_("Access control settings for this EHR."),
        required=False,
    )
    
    
    """
    Where is the access control settings class?
    settings=Object(
        schema=IAccessControlSettings,
        title=_("Settings"),
        description=_("Access control settings for this EHR."),
        required=False,
    )
    
    """
    
    scheme=TextLine(
        title=_(u"Scheme"),
        description=_(u"Name of the access control scheme."),
        required=True,
    )
    
