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

from oship.openehr.rm.common.archetyped.locatable import Locatable

_ = MessageFactory('oship')

    
class EhrAccess(Locatable):
    """
    EHR-wide access control object. Contains all policies and rules for access to data in this EHR.
    """
        
    settings=AccessControlSettings(
        title=_("Settings"),
        description=_("Access control settings for this EHR."),
        required=False,
    )
    
    scheme=TextLine(
        title=_("Scheme"),
        description=_("Name of the access control scheme."),
        required=True,
    )
    
