# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')
       
class OpenehrTerminologyGroupIdentifiers():
    """
    List of identifiers for groups in the openEHR terminology.
    """
    terminologyId='openehr'
    groupIdAuditChangeType='audit change type'
    groupIdAttestationReason='attestation reason'
    groupIdCompositionCategory='composition category'
    groupIdEventMathFunction='event math function'
    groupIdIsmStates='instruction states'
    groupIdIsmTransitions='instruction transitions'
    groupIdNullFlavours='null flavours'
    groupIdMeasurableProperties='property'
    groupIdParticipationFunction='participation function'
    groupIdParticipationMode='participation mode'
    groupIdRelatedPartyRelationship='related party relationship'
    groupIdSetting='setting'
    groupIdTermMappingPurpose='term mapping purpose'	
    groupIdVersionLifecycleState='version lifecycle state'	
	
    values=(terminologyId, groupIdAuditChangeType, groupIdAttestationReason,\
	    groupIdCompositionCategory, groupIdEventMathFunction, groupIdIsmStates, \
	    groupIdIsmTransitions, groupIdNullFlavours, groupIdMeasurableProperties, \
	    groupIdParticipationFunction, groupIdParticipationMode, \
	    groupIdRelatedPartyRelationship, groupIdSetting, groupIdTermMappingPurpose, \
	    groupIdVersionLifecycleState)
      
def validTerminologyGroupId(anId):
    u"""
    Validity function to test if an identifier is in the tuple defined by class OpenehrTerminologyGroupIdentifiers.
    """
    return anId in OpenehrTerminologyGroupIdentifiers.values


