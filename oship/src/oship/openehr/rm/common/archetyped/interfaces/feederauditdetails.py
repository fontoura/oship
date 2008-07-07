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
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory

from openehr.rm.demographic.partyidentified import PartyIdentified
from openehr.rm.demographic.partyproxy import PartyProxy

from openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime

_ = MessageFactory('oship')


class IFeederAuditDetails(Interface):
    u"""
    Audit details for any system in a feeder system chain. Audit details here means
    the general notion of who/where/when the information item to which the audit is
    attached was created. None of the attributes is defined as mandatory, however, in
    different scenarios, various combinations of attributes will usually be mandatory.
    This can be controlled by specifying feeder audit details in legacy archetypes.
    """

    systemId = TextLine(
        title=_(u'System Id'),
        description=_(u"""Identifier of the system which handled the information item."""),
        required=True,
        )
    
    provider = PartyIdentified(
        title=_(u'Provider'),
        description=_(u"""Optional provider(s) who created, committed, forwarded or otherwise 
        handled the item. Type == PARTY_IDENTIFIED"""),
        required=False,
        )
    
    location = PartyIdentified(
        title=_(u'Location'),
        description=_(u"""Identifier of the particular site/facility within an organisation 
                    which handled the item. For computability, this identifier needs to be 
                    e.g. a PKI identifier which can be included in the identifier list of 
                    the PARTY_IDENTIFIED object."""),
        required=False,
        )
    
    time = DvDateTime(
        title=_(u'Time'),
        description=_(u"""Time of handling the item. For an originating time: DV_DATE_TIME system, 
                    this will be time of creation, for an intermediate feeder system, this will 
                    be a time of accession or other time of handling, where available."""),
        required=False,
        )
    
    subject = PartyProxy(
        title=_(u'Subject'),
        description=_(u"""Identifiers for subject of the received information item."""),
        required=False,
        )
    
    versionId = TextLine(
        title=_(u'Version Id'),
        description=_(u"""Any identifier used in the system such as "interim", "final", 
                      or numeric versions if available."""),
        required=False,
        )
    
    def systemIdValid():
        u"""systemId != None and  systemId != '' """
        
