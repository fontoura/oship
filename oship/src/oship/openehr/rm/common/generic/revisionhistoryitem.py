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
from zope.schema import Field
from zope.i18nmessageid import MessageFactory

from interfaces.revisionhistoryitem import IRevisionHistoryItem

_ = MessageFactory('oship')
      

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
        