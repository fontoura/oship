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
from zope.schema import Set

from openehr.rm.support.identification.hierobjectid import HierObjectId
from openehr.rm.common.generic.auditdetails import AuditDetails

_ = MessageFactory('oship')

class IContribution(IContainer):
    u"""
    Documents a contribution of one or more versions added to a change-controlled repository.
    """
    
    uid=HierObjectId(
        title=_(u'UID'),
        description=_(u"""Unique identifier for this contribution."""),
        required=True
    )
    
    versions=Set(
        title=_(u'Versions'),
        description=_(u"""Set of references to versions causing changes to
                      this EHR. Each contribution contains a list of versions
                      which may include paths pointing to any number of 
                      VERSIONABLE items, i.e. items of type COMPOSITION and FOLDER."""),
        required=True
    )
   
    audit=AuditDetails(
        title=_(u'Audit'),
        description=_(u"""Audit trail corresponding to the committal of this Contribution."""),
        required=True
    )
    
    