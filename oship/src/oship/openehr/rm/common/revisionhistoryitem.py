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

from zope.interface import implements
from zope.schema import List
from zope.i18nmessageid import MessageFactory

from openehr.rm.support.objectversionid import ObjectVersionId

_ = MessageFactory('oship')


class IRevisionHistoryItem(Interface):
    u"""
    An entry in a revision history, corresponding to a version from a versioned 
    container. Consists of AUDIT_DETAILS instances with revision identifier of 
    the revision to which the AUDIT_DETAILS intance belongs.
    """

    audits = List(
        title=_(u'Audits'),
        description=_(u"""The audits for this revision; there will always be at 
                    least one commit audit (which may itself be an ATTESTATION), 
                    there may also be further attestations."""),
        required=True,
        )
    
    versionId = ObjectVersionId(
        title=_(u'Version Id'),
        description=_(u"""Version identifier for this revision."""),
        required=True,
        )
    
    def auditValid():
        u"""audits != None and audits != ' """

    def versionIdValid():
        u"""versionId != None"""
        
        

class RevisionHistoryItem(Field):
    u"""
    An entry in a revision history, corresponding to a version from a versioned 
    container. Consists of AUDIT_DETAILS instances with revision identifier of 
    the revision to which the AUDIT_DETAILS intance belongs.
    """
    
    implements(IRevisionHistoryItem)
    
    def __init__(self,audits,verid,**kw):
        self.audits=audits
        self.versionId=verid
        for n,v in kw.items():
            setattr(self,n,v)

   
    def auditValid():
        u"""audits != None and audits != ' """

    def versionIdValid():
        u"""versionId != None"""
        