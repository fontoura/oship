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
from zope.schema import Object

from version import IVersion
from oship.openehr.rm.common.changecontrol.interfaces.resourceoriginalversion import IOriginalVersion

_ = MessageFactory('oship')

class IImportedVersion(IVersion):
    u"""
    A Version containing locally created content and optional attestations.
    """
    
    item=Object(
        schema=IOriginalVersion,
        title=_(u"Item"),
        description=_(u"""Original Version object that was imported."""),
        required=True
    )
    
    
   