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

from zope.interface import Interface
from zope.schema import List,Object
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.archetyped.interfaces.feederauditdetails import IFeederAuditDetails
from openehr.rm.datatypes.encapsulated.interfaces.dvencapsulated import IDvEncapsulated
from openehr.rm.common.archetyped.interfaces.locatable import ILocatable


_ = MessageFactory('oship')


class IFeederAudit(ILocatable):
    """
    Audit and other meta-data for systems in the feeder chain.
    """
    
    originatingSystemAudit = Object(
        schema=IFeederAuditDetails,
        title=_(u"Originating System Audit"),
        description=_(u"""Any audit information for the information item from the originating system."""),
        required =True,
        )
    
    originatingSystemItemIds = List(
        title=_(u"Originating System Item IDs"),
        description=_(u"""Identifiers used for the item in the originating system, e.g. filler and placer ids."""),
        required=False,
        )
    
    
    feederSystemAudit = Object(
        schema=IFeederAuditDetails,
        title=_(u"Feeder System Audit"),
        description=_(u"""Any audit information for the information item from the feeder system, 
                    if different from the originating system."""),
        required=False,
        )
    
    feederSystemItemIds = List(
        title=_(u"Feeder System Item IDs"),
        description=_(u"""Identifiers used for the item in the feeder system, where the feeder 
                    system is distinct from the originating system. The List contents are restricted to
                    type == DvIdentifiers"""),
        required=False,
        )
    
    originalContent=Object(
        schema=IDvEncapsulated,
        title=_(u"Original Content"),
        description=_(u""" """),
        required=False,
        )
    
    def originatingSystemAuditValid():
        """ originatingSystemAudit != None """
