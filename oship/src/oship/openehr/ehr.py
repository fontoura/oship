# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""
openEHR EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = u'Renato Pesca <rpesca@gmail.com>'


import grok

from datetime import datetime
from zope.interface import Interface, implements
from zope.schema import List,Field,TextLine,Object,Bool
from zope.i18nmessageid import MessageFactory

from common import Locatable,Pathable,IPartyIdentified,IParticipation,IPartyProxy
from support import IHierObjectId,IObjectRef,ILocatableRef
from datatypes import IDvDateTime,IDvCodedText,ICodePhrase,IDvParsable,IDvText
from datastructure import IItemStructure,IHistory

_ = MessageFactory('oship')

class IContentItem(Interface):
    """
    Abstract ancestor of all concrete content types.
    """

    pass

class IIsmTransition(Interface):
    """
    Model of a transition in the Instruction state machine.
    """

    currentState=Object(
        schema=IDvCodedText,
        title=_(u"Current State"),
        description=_(u"The ISM current state."),

    )

    transition=Object(
        schema=IDvCodedText,
        title=_(u"Transition"),
        description=_(u"The ISM transition which occured to arrive at the current state."),
        required=False,
    )

    careflowStep=Object(
        schema=IDvCodedText,
        title=_(u"Careflow Step"),
        description=_(u"The step in the careflow process which occured as part of this process."),
        required=False,
    )


class IEhr(Interface):
    """
    Root EHR container
    """

    systemId=Object(
        schema=IHierObjectId,
        title=_(u"System Id"),
        description=_(u"Id of system where this EHR was created."),

    )

    ehrId=Object(
        schema=IHierObjectId,
        title=_(u"EHR ID"),
        description=_(u"Id of this EHR."),

    )

    timeCreated=Object(
        schema=IDvDateTime,
        title=_(u"Created"),
        description=_(u"Creation data/time"),

    )

    contributions=List(
        title=_(u"Contributions"),
        description=_(u"List of contributions causing changes to this EHR."),
	value_type=Object(schema=IObjectRef),

    )

    ehrAccess=Object(
        schema=IObjectRef,
        title=_(u"EHR Access"),
        description=_(u"A reference to the EHR Access object."),

    )

    ehrStatus=Object(
        schema=IObjectRef,
        title=_(u"EHR Status"),
        description=_(u"A reference to the EHR Status object."),

    )

    directory=Object(
        schema=IObjectRef,
        title=_(u"Directory"),
        description=_(u"Optional directory structure."),
        required=False,
    )

    compositions=List(
        title=_(u"Compositions"),
        description=_(u"Master list of all compositions references."),
	value_type=Object(schema=IObjectRef),

    )


class Ehr(grok.Container):
    """
    Root EHR container.
    """

    implements(IEhr)

    def __init__(self,systemId,ehrId,timeCreated,contributions,ehrAccess,ehrStatus,directory,compositions):

        self.systemId=systemId
        self.ehrId=ehrId
        self.timeCreated=timeCreated
        self.ehrStatus=ehrStatus


class IEventContext(Interface):
    """
    The context information of a healthcare event.
    These include patient contacts or other investigations.
    """

    healthCareFacility=Object(
        schema=IPartyIdentified,
        title=_(u"Healthcare Facility"),
        description=_(u"Where this event took place."),
        required=False,
    )

    startTime=Object(
        schema=IDvDateTime,
        title=_(u"Start Time"),
        description=_(u"Start Time"),

    )

    endTime=Object(
        schema=IDvDateTime,
        title=_(u"End Time"),
        description=_(u"End Time"),
        required=False,
    )

    participations=List(
        title=_(u"Participations"),
        description=_(u"List of all parties involved in the event."),
	value_type=Object(schema=IParticipation),
        required=False,
    )

    location=TextLine(
        title=_(u"Location"),
        description=_(u"Physical location of this event; ABCLab, home,etc."),
        required=False,
    )

    setting=Object(
        schema=IDvCodedText,
        title=_(u"Setting"),
        description=_(u"The setting of the clinical event."),

    )

    otherContext=Object(
        schema=IItemStructure,
        title=_(u"Other Context"),
        description=_(u"Other optional archetyped context."),
        required=False,
    )

class IComposition(Interface):
    """
    One version in a VersionedComposition.  A compsoition is considerred the unit of modification in an EHR.
    """

    content=List(
        title=_(u"Content"),
        description=_(u"Content of this composition."),
	value_type=Object(schema=IContentItem),
        required=False,
    )

    context=Object(
        schema=IEventContext,
        title=_(u"Context"),
        description=_(u"The clinical session context."),
        required=False,
    )

    composer=Object(
        schema=IPartyProxy,
        title=_(u"Composer"),
        description=_(u"The party responsible for the content. It may not be the actual person entering the data."),

    )

    category=Object(
        schema=IDvCodedText,
        title=_(u"Category"),
        description=_(u"Defines the broad category of this composition."),

    )

    language=Object(
        schema=ICodePhrase,
        title=_(u"Language"),
        description=_(u"Indicator of the localised language where this composition was created."),

    )

    territory=Object(
        schema=ICodePhrase,
        title=_(u"Territory"),
        description=_(u"Territory where this composition was written. ISO 3166."),

    )

    isPersistent=Bool(
        title=_(u"Persistent"),
        description=_(u"Used to locate items that are of interest to most users."),

    )

class Composition(Locatable,grok.Container):
    """
    One version in a VersionedComposition.  A composition is considered the unit of modification in an EHR.
    """

    implements(IComposition)


    def __init__(self,content,context,composer,cat,lang,terr,persistuid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
        self.content=content
        self.context=context
        self.composer=composer
        self.category=cat
        self.language=lang
        self.territory=terr
        self.isPersistent=persist






class EventContext(Pathable):
    """
    The context information of a healthcare event.
    These include patient contacts or other investigations.
    """

    implements(IEventContext)

    def __init__(self,hcf,start,end,part,loc,sett,other):
        self.healthCareFacility=hcf
        self.startTime=start
        self.endTime=end
        self.participations=part
        self.location=loc
        self.setting=sett
        self.otherContext=other



class ContentItem(grok.Container):
    """
    Abstract ancestor of all concrete content types.
    """

    implements(IContentItem)


    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)


#Begin the entry package
class IEntry(Interface):
    u"""
        The abstract parent of all ENTRY subtypes. An ENTRY is the root of a logical item
        of "hard" clinical information created in the "clinical statement" context, within a
        clinical session. There can be numerous such contexts in a clinical session. Obser-
        vations and other Entry types only ever document information captured/created in
        the event documented by the enclosing Composition.
        An ENTRY is also the minimal unit of information any query should return, since a
        whole ENTRY (including subparts) records spatial structure, timing information,
        and contextual information, as well as the subject and generator of the informa-
        tion.

    """

    language = Object(
        schema=ICodePhrase,
        title = _(u"language"),
        description = _(u"""Mandatory indicator of the localised language in which this Entry
                      is written. Coded from openEHR Code Set "languages"."""),
        required = True
        )

    encoding = Object(
        schema=ICodePhrase,
        title = _(u"encoding"),
        description = _(u"""Name of character set in which text values in this Entry are encoded.
                      Coded from openEHR Code Set "character sets"."""),
        required = True
        )


    subject = Object(
        schema=IPartyProxy,
        title = _(u"subject"),
        description = _(u"""Id of human subject of this ENTRY, e.g.
                           organ donor, foetus, a family member
                           another clinically relevant person."""),
        required = True
        )

    provider = Object(
        schema=IPartyProxy,
        title = _(u"provider"),
        description = _(u"""Optional identification of provider of the information in this ENTRY, which might be:
                        the patient
                        a patient agent, e.g. parent, guardian
                        the clinician
                        a device or software
                       Generally only used when the recorder needs to make it explicit. Otherwise, Composition
                       composer and other participants are assumed. """),
        required = False
        )

    otherParticipations = List(
        title = _(u"otherParticipations"),
        description = _(u"""Other participations at ENTRY level."""),
	value_type=Object(schema=IParticipation),
        required = False
        )

    workflowId = Object(
        schema=IObjectRef,
        title = _(u"workflowId"),
        description = _(u"""Identifier of externally held workflow engine data for this
                      workflow execution, for this subject of care."""),
        required = False
        )


    def subectIsSelf():
        u"""Returns True if this Entry is about the subject of the EHR, in which case the
        subject attribute is of type PARTY_SELF. """



class Entry(ContentItem):
    """
    The abstract parent of all ENTRY subtypes. An ENTRY is the root of a logical item
    of "hard" clinical information created in the "clinical statement" context, within a
    clinical session. There can be numerous such contexts in a clinical session. Obser-
    vations and other Entry types only ever document information captured/created in
    the event documented by the enclosing Composition.
    An ENTRY is also the minimal unit of information any query should return, since a
    whole ENTRY (including subparts) records spatial structure, timing information,
    and contextual information, as well as the subject and generator of the informa-
    tion.
    """

    implements(IEntry)

    def __init__(self,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        ContentItem.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)

        self.language=lang
        self.encoding=encod
        self.subject=subject
        self.provider=provider
        self.otherParticipations=opart
        self.workflowId=wfid

    def subectIsSelf():
        u"""Returns True if this Entry is about the subject of the EHR, in which case the
        subject attribute is of type PARTY_SELF. """
        return (isinstance(subject, PartyProxy))


class ICareEntry(Interface):
    u"""
            The abstract parent of all clinical ENTRY subtypes. A CARE_ENTRY defines
            protocol and guideline attributes for all clinical Entry subtypes.

    """

    protocol = Object(
        schema=IItemStructure,
        title=_(u"Protocol"),
        description=_(u"""Description of the method (i.e. how) the information in this
                    entry was arrived at. For OBSERVATIONs, this is a description of the
                    method or instrument used. For EVALUATIONs, how the evaluation was
                    arrived at. For INSTRUCTIONs, how to execute the Instruction.
                    This may take the form of references to guidelines, including
                    manually followed and executable; knowledge references such as a
                    paper in Medline; clinical reasons within a largercare process."""),
        required=False
    )

    guidelineId = Object(
        schema=IObjectRef,
        title=_(u"guidelineId"),
        description=_(u"""Optional external identifier of guideline creating this
                    action if relevant."""),
        required=False
    )




class CareEntry(Entry):
    """
    The abstract parent of all clinical ENTRY subtypes. A CARE_ENTRY defines
    protocol and guideline attributes for all clinical Entry subtypes.
    """

    implements(ICareEntry)


    def __init__(self,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        Entry.__init__(self,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)
        self.protocol=protocol
        self.guidelineId=gid

class IInstructionDetails(Interface):
    """
    Used to record the details of an Instruction causing an Action.
    """

    instructionId=Object(
        schema=ILocatableRef,
        title=_(u"Instruction Id"),
        description=_(u"Reference to causing Instruction."),

    )

    activityId=TextLine(
        title=_(u"Activity Id"),
        description=_(u"Indentifier of Activity within Instruction."),

    )

    wfDetails=Object(
        schema=IItemStructure,
        title=_(u"WF Details"),
        description=_(u"Various workflow engine state details."),
        required=False,
    )


class IAction(Interface):
    """
    Used to record a clinical action that has been performed.
    """

    time=Object(
        schema=IDvDateTime,
        title=_(u"Timing"),
        description=_(u"Point in time of completion of this action."),

    )

    description=Object(
        schema=IItemStructure,
        title=_(u"Description"),
        description=_(u"Description of the activity in ItemStructure form."),

    )

    ismTransition=Object(
        schema=IIsmTransition,
        title=_(u"ISM Transition"),
        description=_(u"Details of the transition of the Instruction state."),

    )

    instructionDetails=Object(
        schema=IInstructionDetails,
        title=_(u"Instruction Details"),
        description=_(u"Details of the Instruction causing this Action."),
        required=False,
    )


class Action(CareEntry):
    """
    Used to record a clinical action that has been performed.
    """

    implements(IAction)


    def __init__(self,time,desc,ism,inst,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        CareEntry.__init__(self,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)
        self.time=time
        self.description=desc
        self.ismTransition=ism
        self.instructionDetails=inst



class IActivity(Interface):
    """
    A single activity within an instruction.
    """

    description=Object(
        schema=IItemStructure,
        title=_(u"Description"),
        description=_(u"Description of the activity."),

    )

    timing=Object(
        schema=IDvParsable,
        title=_(u"Timing"),
        description=_(u"Timing of the activity in a format such as ISO8601."),

    )

    actionArchetypeId=TextLine(
        title=_(u"Action ArchetypeId"),
        description=_(u"re pattern enclosed in '//' delimiters."),

    )

class Activity(Locatable):
    """
    A single activity within an instruction.
    """

    implements(IActivity)


    def __init__(self,descr,tim,atid,nodeid,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)

        self.description=descr
        self.timing=tim
        self.actionArchetypeId=atid
        self.archetypeNodeId=nodeid


class IAdminEntry(Interface):
    u"""
        Entry subtype for administrative information, i.e. information about setting up the
        clinical process, but not itself clinically relevant. Archetypes will define con-
        tained information.
        Used for admistrative details of admission, episode, ward location, discharge,
        appointment (if not stored in a practice management or appointments system).

        Not used for any clinically significant information.
    """

    data = Object(
        schema=IItemStructure,
        title=u"""data""",
        description=u"""The data of the Entry; modelled in archetypes.""",
        required=True
        )

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


    def __init__(self,data,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        Entry.__init__(self,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)
        self.data=data


class IEvaluation(Interface):
    """
    Entry type for evaluation statements.
    """

    data=Object(
        schema=IItemStructure,
        title=_(u"Data"),
        description=_(u"The data of this evaluation."),

    )

class Evaluation(CareEntry):
    """
    Entry type for evaluation statements.
    """

    implements(IEvaluation)

    def __init__(self,data,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        CareEntry.__init__(self,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)

        self.data=data


class InstructionDetails(Pathable):
    """
    Used to record the details of an Instruction causing an Action.
    """

    implements(IInstructionDetails)

    def __init__(self,inst,actid,wfd):

        self.instructionId=inst
        self.activityId=actid
        self.wfDetails=wfd

class IInstruction(Interface):
    """
    Used to specify future actions and includes a workflow form.
    """

    narrative=Object(
        schema=IDvText,
        title=_(u"Narrative"),
        description=_(u"Human readable version of the Instructions."),

    )

    activities=List(
        value_type = Object(schema = IActivity),
        title=_(u"Activities"),
        description=_(u"List of all activities in the Instruction."),
        required=False,
    )

    expiryTime=Object(
        schema=IDvDateTime,
        title=_(u"Expiry Time"),
        description=_(u"Data/time when this Instruction can be assumed to have expired."),
        required=False,
    )

    wfDefinition=Object(
        schema=IDvParsable,
        title=_(u"Workflow Definition"),
        description=_(u"Workflow engine executable expression of the Instruction."),
        required=False,
    )




class Instruction(CareEntry):
    """
    Used to specify future actions and includes a workflow form.
    """

    implements(IInstruction)

    def __init__(self,narr,act,exp,wfd,nodeid,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        CareEntry.__init__(self,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)
        self.narrative=narr
        self.activities=act
        self.expiryTime=exp
        self.wfDefinition=wfd



class IsmTransition(Pathable):
    """
    Model of a transition in the Instruction state machine.
    """

    implements(IIsmTransition)

    def __init__(self,cstate,trans,cfs):
        self.currentState=cstate
        self.transition=trans
        self.careflowStep=cfs

class IObservation(Interface):
    u"""Entry subtype for all clinical data in the past or present, i.e. which (by the time it
    is recorded) has already occurred. OBSERVATION data is expressed using the class
    HISTORY<T>, which guarantees that it is situated in time.
    OBSERVATION is used for all notionally objective (i.e. measured in some way)
    observations of phenomena, and patient-reported phenomena, e.g. pain.
    Not used for recording opinion or future statements of any kind, including instructions,
    intentions, plans etc."""

    data = Object(
        schema=IHistory,
        title=_(u"data"),
        description=_(u"""The data of this observation, in the form of a history of
                    values which may be of any complexity."""),
        required=True
    )

    state = Object(
        schema=IHistory,
        title=_(u"state"),
        description=_(u"""Optional recording of the state of subject of this
                    observation during the observation process, in the form of
                    a separate history of values which may be of any complexity.
                    State may also be recorded within the History of the data attribute."""),
        required=False
    )


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

    def __init__(self,data,state,nodeid,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        CareEntry.__init__(self,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)
        self.data=data
        self.state=state
        self.archetypeNodeId=nodeid


#Begin Navigation package

class ISection(Interface):
    """
    Represents a heading in a heading structure or 'section tree'.
    """

    items=List(
        title=_(u"Items"),
        description=_(u"Ordered list of content items that may include more SECTIONs or ENTRYs."),
	value_type=Object(schema=IContentItem),
        required=False,
    )


class Section(ContentItem):
    """
    Represents a heading in a heading structure or 'section tree'.
    """

    implements(ISection)

    def __init__(self,items,uid,atnodeid,name,atdetails,fdraudit,links):
        ContentItem.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)

        self.items=items


