# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')


class IEntry(IContentItem):
    u"""
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

    language = CodePhrase(
        title = u"""language""",
        description = u"""Mandatory indicator of the localised language in which this Entry 
                      is written. Coded from openEHR Code Set “languages”.""",
        required = True
        )
    
    encoding = CodePhrase(
        title = u"""encoding""",
        description = u"""Name of character set in which text values in this Entry are encoded. 
                      Coded from openEHR Code Set “character sets”.""",
        required = True
        )

        
    subject = PartyProxy(
        title = u"""subject""",
        description = u"""Id of human subject of this ENTRY, e.g.
                          • organ donor
                          • foetus
                          • a family member
                          • another clinically relevant person.""",
        required = True
        )
    
    provider = PartyProxy(
        title = u"""provider""",
        description = u"""Optional identification of provider of the informatoin in this ENTRY, which might be:
                       • the patient
                       • a patient agent, e.g. parent, guardian
                       • the clinician
                       • a device or software
                       Generally only used when the recorder needs to make it explicit. Otherwise, Composition
                       composer and other participants are assumed. """,
        required = False
        )
    
    otherParticipations = List(
        title = u"""otherParticipations""",
        description = u"""Other participations at ENTRY level.""",
        required = False
        )
    
    workflowId = ObjectRef(
        title = u"""workflowId""",
        description = u"""Identifier of externally held workflow engine data for this 
                      workflow execution, for this subject of care.""",
        required = False
        )
    
    
    def subectIsSelf():
        u"""Returns True if this Entry is about the subject of the EHR, in which case the 
        subject attribute is of type PARTY_SELF. """
    
    
class IAdminEntry(IEntry):
    u"""
        Entry subtype for administrative information, i.e. information about setting up the
        clinical process, but not itself clinically relevant. Archetypes will define con-
        tained information.
        Used for admistrative details of admission, episode, ward location, discharge,
        appointment (if not stored in a practice management or appointments system).
        
        Not used for any clinically significant information.
    """
    
    data = ItemStructure(
        title=u"""data""",
        description=u"""The data of the Entry; modelled in archetypes.""",
        required=True
        )
    
    
class ICareEntry(IEntry):
    u"""
            The abstract parent of all clinical ENTRY subtypes. A CARE_ENTRY defines 
            protocol and guideline attributes for all clinical Entry subtypes.

    """

    protocol = ItemStructure(
        title=u"""protocol""",
        description=u"""Description of the method (i.e. how) the information in this 
                    entry was arrived at. For OBSERVATIONs, this is a description of the
                    method or instrument used. For EVALUATIONs, how the evaluation was 
                    arrived at. For INSTRUCTIONs, how to execute the Instruction. 
                    This may take the form of references to guidelines, including 
                    manually followed and executable; knowledge references such as a
                    paper in Medline; clinical reasons within a largercare process.""",
        required=False
    )
    
    guidelineId = ObjectRef(
        title=u"""guidelineId""",
        description=u"""Optional external identifier of guideline creating this 
                    action if relevant.""",
        required=False
    )
    
    
class IObservation(ICareEntry):
    u"""Entry subtype for all clinical data in the past or present, i.e. which (by the time it 
    is recorded) has already occurred. OBSERVATION data is expressed using the class
    HISTORY<T>, which guarantees that it is situated in time.
    OBSERVATION is used for all notionally objective (i.e. measured in some way)
    observations of phenomena, and patient-reported phenomena, e.g. pain.
    Not used for recording opinion or future statements of any kind, including instructions, 
    intentions, plans etc."""
    
    data = History(
        title=u"""data""",
        description=u"""The data of this observation, in the form of a history of 
                    values which may be of any complexity.""",
        required=True
    )
    
    state = History(
        title=u"""state""",
        description=u"""Optional recording of the state of subject of this
                    observation during the observation process, in the form of 
                    a separate history of values which may be of any complexity. 
                    State may also be recorded within the History of the data attribute.""",
        required=False
    )
    
class IEvaluation(ICareEntry):
    """
    Entry type for evaluation statements.
    """
    
    data=ItemStructure(
        title=_("Data"),
        description=_("The data of this evaluation."),
        required=True,
    )
    
class IInstruction(ICareEntry):
    """
    Used to specify future actions and includes a workflow form.
    """
    
    narrative=DvText('',
        title_("Narrative"),
        description=_("Human readable version of the Instructions."),
        required=True,
    )
    
    activities=List(
        title=_("Activities"),
        description=_("List of all activities in the Instruction."),
        required=False,
    )
    
    expiryTime=DvDateTime('',
        title=_("Expiry Time"),
        description=_("Data/time when this Instruction can be assumed to have expired."),
        required=False,
    )
    
    wfDefinition=DvParsable(
        title=_("Workflow Definition"),
        description=_("Workflow engine executable expression of the Instruction."),
        required=False,
    )
    
class IActivity(ILocatable):
    """
    A single activity within an instruction.
    """
    
    description=ItemStructure(
        title=_("Description"),
        description=_("Description of the activity."),
        required=True,
    )
    
    timing=DvParsable(
        title=_("Timing"),
        description=_("Timing of the activity in a format such as ISO8601."),
        required=True,
    )
    
    actionArchetypeId=TextLine(
        title=_("Action ArchetypeId"),
        description=_("re pattern enclosed in '//' delimiters."),
        required=True,
        default="/.*/",
    )
    
class IAction(ICareEntry):
    """
    Used to record a clinical action that has been performed.
    """
    
    time=DvDateTime('',
        title=_("Timing"),
        description=_("Point in time of completion of this action."),
        required=True,
    )
    
    description=ItemStructure(
        title=_("Description"),
        description=_("Description of the activity in ItemStructure form."),
        required=True,
    )
    
    ismTransition=IsmTransition(
        title=_("ISM Transition"),
        description=_("Details of the transition of the Instruction state."),
        required=True,
    )
    
    instructionDetails=InstructionDetails(
        title=_("Instruction Details"),
        description=_("Details of the Instruction causing this Action."),
        required=False,
    )
    
class IInstructionDetails(IPathable):
    """
    Used to record the details of an Instruction causing an Action.
    """
    
    instructionId=LocatableRef(
        title=_("Instruction Id"),
        description=_("Reference to causing Instruction."),
        required=True,
    )
    
    activityId=TextLine(
        title=_("Activity Id"),
        description=_("Indentifier of Activity within Instruction."),
        required=True,
    )
    
    wfDetails=ItemStructure(
        title=_("WF Details"),
        description=_("Various workflow engine state details."),
        required=False,
    )
    
class IIsmTransition(IPathable):
    """
    Model of a transition in the Instruction state machine.
    """
    
    currentState=DvCodedText(
        title=_("Current State"),
        description=_("The ISM current state."),
        required=True,
    )
    
    transition=DvCodedText(
        title=_("Transition"),
        description=_("The ISM transition which occured to arrive at the current state."),
        required=False,
    )
    
    careflowStep=DvCodedText(
        title=_("Careflow Step"),
        description=_("The step in the careflow process which occured as part of this process."),
        required=False,
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    