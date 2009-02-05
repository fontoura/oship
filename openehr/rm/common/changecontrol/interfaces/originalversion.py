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
from zope.schema.interfaces import IContainer
from zope.schema import Object

from oship.openehr.rm.support.identification.interfaces.objectversionid import IObjectVersionId

_ = MessageFactory('oship')

class IOriginalVersion(IContainer):
    u"""
    A Version containing locally created content and optional attestations.
    """
    
    uid=Object(
        schema=IObjectVersionId,
        title=_(u"UID"),
        description=_(u"""Stored version of inheritence precursor."""),
        required=True
    )
    
    precedingVersionUid=Object(
        schema=IObjectVersionId,
        title=_(u"Preceding Version UID"),
        description=_(u"""Stored version of inheritence precursor."""),
        required=True
    )
  
    