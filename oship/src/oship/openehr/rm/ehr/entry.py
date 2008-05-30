# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementations for specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory

from openehr.rm.ehr.interfaces.entry import *


_ = MessageFactory('oship')


class Entry(ContentItem):
    """
    The abstract parent of all ENTRY subtypes. An ENTRY is the root of a logical item
    of “hard” clinical information created in the “clinical statement” context, within a
    clinical session. There can be numerous such contexts in a clinical session. Obser-
    vations and other Entry types only ever document information captured/created in
    the event documented by the enclosing Composition.
    An ENTRY is also the minimal unit of information any query should return, since a
    whole ENTRY (including subparts) records spatial structure, timing information,
    and contextual information, as well as the subject and generator of the informa-
    tion.   
    """

    implements(IEntry)
    
    def __init__(self,lang,encod,subject,provider,opart,wfid,**kwargs):
        self.language=lang
        self.encoding=encod
        self.subject=subject
        self.provider=provider
        self.otherParticipations=opart
        self.workflowId=wfid    
    
    def subectIsSelf():
        u"""Returns True if this Entry is about the subject of the EHR, in which case the 
        subject attribute is of type PARTY_SELF. """
    
    
class AdminEntry(Entry):
    """
    Entry subtype for administrative information, i.e. information about setting up the
    clinical process, but not itself clinically relevant. Archetypes will define con-
    tained information.
    Used for admistrative details of admission, episode, ward location, discharge,
    appointment (if not stored in a practice management or appointments system).
    
    Not used for any clinically significant information.
    """
    
    implements(IAdminEntry)
    
    def __init__(self,data,**kwargs):
        self.data=data
    
class CareEntry(Entry):
    """
    The abstract parent of all clinical ENTRY subtypes. A CARE_ENTRY defines 
    protocol and guideline attributes for all clinical Entry subtypes.
    """

    implements(ICareEntry)
    
    def __init__(self,protocol,gid,**kwargs):
        self.protocol=protocol
        self.guidelineId=gid
            
    
class Observation(CareEntry):
    """
    Entry subtype for all clinical data in the past or present, i.e. which (by the time it 
    is recorded) has already occurred. OBSERVATION data is expressed using the class
    HISTORY<T>, which guarantees that it is situated in time.
    OBSERVATION is used for all notionally objective (i.e. measured in some way)
    observations of phenomena, and patient-reported phenomena, e.g. pain.
    Not used for recording opinion or future statements of any kind, including instructions, 
    intentions, plans etc.
    """

    implements(IObservation)
    
    def __init__(self,data,state,**kwargs):
        self.data=data
        self.state=state
            
class Evaluation(CareEntry):
    """
    Entry type for evaluation statements.
    """
    
    Implements(IEvaluation)
 
    def __init__(self,data,state,**kwargs):
        self.data=data
    
class Instruction(CareEntry):
    """
    Used to specify future actions and includes a workflow form.
    """
    
    implements(IInstruction)
    
    def __init__(self,narr,act,exp,wfd,**kwargs):
        self.narrative=narr
        self.activities=act
        self.expiryTime=exp
        self.wfDefinition=wfd
        
   
class Activity(Locatable):
    """
    A single activity within an instruction.
    """
    
    implements(IActivity)
    
    def __init__(self,desc,tim,atid,**kwargs):
        self.description=desc
        self.timing=tim
        self.actionArchetypeId=atid
        
    
class Action(CareEntry):
    """
    Used to record a clinical action that has been performed.
    """
    
    implements(IAction)
    
    def __init__(self,time,desc,ism,inst,**kwargs):
        self.time=time
        self.description=desc
        self.ismTransition=ism
        self.instructionDetails=inst
            
class InstructionDetails(Pathable):
    """
    Used to record the details of an Instruction causing an Action.
    """
    
    implements(IInstructionDetails)
    
    def __init__(self,inst,actid,wfd,**kwargs):
        self.instructionId=inst
        self.activityId=actid
        self.wfDetails=wfd
    
    
class IsmTransition(Pathable):
    """
    Model of a transition in the Instruction state machine.
    """
    
    implements(IIsmTransition)
    
    def __init__(self,cstate,trans,cfs,**kwargs):
        self.currentState=cstate
        self.transition=trans
        self.careflowStep=cfs
