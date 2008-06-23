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
from zope.schema import Field
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.generic.partyproxy import PartyProxy
from openehr.rm.datatypes.text.dvtext import DvText
from openehr.rm.datatypes.text.dvcodedtext import DvCodedText
from openehr.rm.datatypes.quantity.dvinterval import DvInterval

_ = MessageFactory('oship')

        
class IParticipation(Interface):
    u"""
    Model of a participation of a Party (any Actor or Role) in an activity.
    
    Used to represent any participation of a Party in some activity, which is 
    not explicitly in the model, e.g. assisting nurse. Can be used to record 
    past or future participations.
        
    Should not be used in place of more permanent relationships between demographic entities.
    """
    
    performer = PartyProxy(
        title=_(u'Performer'),
        description=_(u"""The id and possibly demographic system link of performer: 
                    (PartyProxy) the party participating in the activity."""),
        required=True,
        constraint = isinstance(PartyProxy)
        )
    
    function = DvText(
        title=_(u'Function'),
        description=_(u"""The function of the Party in this participation (note 
                    that a given party might participate in more than one way 
                    in a particular activity). This attribute should be coded, 
                    but cannot be limited to the HL7v3:ParticipationFunction 
                    vocabulary, since it is too limited and hospital-oriented."""),
        required=True,
        )
    
    mode = DvCodedText(
        title=_(u'Mode'),
        description=_(u"""The mode of the performer / activity interaction, e.g. 
                    present, by telephone, by email etc. Type == DvCodedText"""),
        required=True,
        )
    
    time = DvInterval(
        title=_(u'Time Interval'),
        description=_(u"""The time interval during which the participation took 
                    place, if it is used in an observational context (i.e. 
                    recording facts about the past); or the intended time 
                    interval of the participation when used in future contexts,
                    such as EHR Instructions."""),
        required=False,
        )
    
    
    def performerValid():
        u"""performer != None"""
        
    def functionValid():
        u"""function != None and then function.generating_type.is_equal(“DV_CODED_TEXT”) 
        implies terminology(Terminology_id_openehr).has_code_for_group_id(Group_id_participation_function, 
        function.defining_code)"""
        
    def modeValid(): 
        u"""mode != None and terminology(Terminology_id_openehr).has_code_for_group_id
        (Group_id_participation_mode, mode.defining_code)"""
        
