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
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.archetyped.locatable import Locatable
from interfaces.feederaudit import IFeederAudit

_ = MessageFactory('oship')

class FeederAudit(Locatable):
    """
    Audit and other meta-data for systems in the feeder chain.
    """

    implements(IFeederAudit)
    
    def __init__(self,orgsysaudit,orgsysids,fsaudit,fsauditids,orgcontent):
        self.originatingSystemAudit=orgsysaudit
        self.originatingSystemItemIds=orgsysids
        self.feederSystemAudit=fsaudit
        self.feederSystemItemIds=fsauditids
        self.originalContent=orgcontent        
     
    def originatingSystemAuditValid():
        """ originatingSystemAudit != None """
