# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the generic package as described in the 
Common Information Model Rev. 2.1.0 

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import Interface
from zope.schema import List,Object
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.support.identification.interfaces.objectversionid import IObjectVersionId
from oship.openehr.rm.common.generic.interfaces.auditdetails import IAuditDetails

_ = MessageFactory('oship')


class IRevisionHistoryItem(Interface):
    u"""
    An entry in a revision history, corresponding to a version from a versioned 
    container. Consists of AUDIT_DETAILS instances with revision identifier of 
    the revision to which the AUDIT_DETAILS intance belongs.
    """

    audits = List(
        value_type=Object(IAuditDetails),
        title=_(u'Audits'),
        description=_(u"""The audits for this revision; there will always be at 
                    least one commit audit (which may itself be an ATTESTATION), 
                    there may also be further attestations."""),
        required=True,
        )
    
    versionId = Object(
        schema=IObjectVersionId,
        title=_(u'Version Id'),
        description=_(u"""Version identifier for this revision."""),
        required=True,
        )
    
    def auditValid():
        u"""audits != None and audits != ' """

    def versionIdValid():
        u"""versionId != None"""
        
        
