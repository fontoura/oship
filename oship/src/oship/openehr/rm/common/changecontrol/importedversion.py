# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the change_control package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
 
from zope.i18nmessageid import MessageFactory

from version import Version
from openehr.rm.common.resource.originalversion import OriginalVersion

_ = MessageFactory('oship')

class ImportedVersion(Version):
    u"""
    A Version containing locally created content and optional attestations.
    """
    
    item=OriginalVersion(
        title=_("Item"),
        description=_("""Original Version object that was imported."""),
        required=True
    )
    
    
   