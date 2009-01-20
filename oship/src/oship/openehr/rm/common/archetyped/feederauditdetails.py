# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the archetyped package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid import MessageFactory

from interfaces.feederauditdetails import IFeederAuditDetails

_ = MessageFactory('oship')
        
        
class FeederAuditDetails(object):
    u"""
    Audit details for any system in a feeder system chain. Audit details here means
    the general notion of who/where/when the information item to which the audit is
    attached was created. None of the attributes is defined as mandatory, however, in
    different scenarios, various combinations of attributes will usually be mandatory.
    This can be controlled by specifying feeder audit details in legacy archetypes.
    """

    implements(IFeederAuditDetails)
    
    def __init__(self,sysid,provider,location,time,subject,verid):
        self.systemId=sysid
        self.provider=provider
        self.location=location
        self.time=time
        self.subject=subject
        self.versionId=verid
    
    def systemIdValid():
        u"""systemId != None and  systemId != '' """
        