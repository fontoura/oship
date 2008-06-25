# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import Interface
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class IOpenehrTerminologyGroupIndentifiers(Interface):
    u"""
    List of constant identifiers for groups in the openEHR terminology.
    """
    
    terminologyId = TextLine(
        title=_(u"Terminology ID"),
        description=_(u"Name of openEHR’s own terminology"),
        default=u"openehr",
        readonly=True,
        )
        
    groupIdAuditChangeType = TextLine(
        title=_(u"Group ID Audit Change"),
        default=_(u"audit change type"),
        readonly=True,
        )
    
    groupIdAttestationReason = TextLine(
        title=_(u"Group ID Atesstation Reason"),
        default=_(u"attestation reason"),
        readoly=True,
        )
    
    groupIdCompositionCategory = TextLine(
        title=_(u"Group ID Composition Category"),
        default=_(u"composition category"),
        readonly=True,
        )
        
    groupIdEventMathFunction = TextLine(
        title=_(u"Group Id Event Math Function"),
        default=_(u"event math function"),
        readonly=True,
        )
        
    groupIdIsmStates = TextLine(
        title=_(u"Group ID ISM States"),
        default=_(u"ISM states"),
        readonly=True,
        )
    
    groupIdIsmTransitions = TextLine(
        title=_(u"Group ID ISM Transitions"),
        default=_(u"ISM transitions"),
        readonly=True,
        )
    
    groupIdNullFlavours = TextLine(
        title=_(u"Group ID Null Flavours"),
        default=_(u"null flavours"),
        readonly=True,
        )
    
    groupIdMeasurableProperties = TextLine(
        title=_(u"Group ID Measurable Properties"),
        default=_(u"measurable properties"),
        readonly=True,
        )
        
        
    groupIdParticipationFunction = TextLine(
        title=_(u"Group ID Participation Function"),
        default=_(u"participation function"),
        readonly=True,
        )
    
    groupIdParticipationMode = TextLine(
        title=_(u"Group ID Participation Mode"),
        default=_(u"participation mode"),
        readonly=True,
        )
    
    groupIdRelatedPartyRelationship = TextLine(
        title=_(u"Group Id Related Party Relationship"),
        default=_(u"related party relationship"),
        readonly=True,
        )
        
    groupIdSetting = TextLine(
        title=_(u"Group ID Setting"),
        default=_(u"setting"),
        readonly=True,
        )
        
    groupIdTermMappingPurpose = TextLine(
        title=_(u"Group Id Term Mapping Purpose"),
        default=_(u"term mapping purpose"),
        readonly=True,
        )
        
        
    groupIdVersionLifecycleState = TextLine(
        title=_(u"Group Id Version Lifecycle State"),
        default=_(u"version lifecycle state"),
        readonly=True,
        )
    
    
    def validTerminologyGroupId(anId):
        u"""
        Validity function to test if an identifier anId==<String> is in the set defined by this class.
        """
        
        
