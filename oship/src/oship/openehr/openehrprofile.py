# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the Mozilla Public License Version 1.1 - see docs/OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the Archetype Profile specifications

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'


from zope.interface import Interface,implements
from zope.i18nmessageid import MessageFactory
from zope.schema import TextLine,Field,List,Set,Object
import grok

from archetype import CDomainType
from datatypes import IDvOrdinal,ICodePhrase
from support import Interval,ITerminologyId

_ = MessageFactory('oship')

#Begin Basic Datatypes package
class IState(Interface):
    """        
    Abstract definition of one state in a state machine.
    """

    name = TextLine(
        title=_(u"Name"),
        description=_(u"""Name of this State."""),
        required=False,
        )
    
class State(grok.Model):
    """        
    Abstract definition of one state in a state machine.
    """
    implements(IState)
   
    def __init__(self,name):
        self.name=name

class IStateMachine(Interface):
    """        
    Definition of a state machine in terms of states, transition events and outputs, and
    next states.
    """
    
    states = Set(
        title=_(u"States"),
        description=_(u"""A Set of State types. """),
        value_type=Object(schema=IState),
        )
          
        

class ICDvState(Interface):
    """
    Constrainer type for DV_STATE instances. The attribute c_value defines a
    state/event table which constrains the allowed values of the attribute value in a
    DV_STATE instance, as well as the order of transitions between values.
    """
    
    value = Object(
        schema=IStateMachine,
        title=_(u"Value"),
        description=_(u""" """),
        
        )
    
     
class CDvState(CDomainType):
    u"""
    Constrainer type for DV_STATE instances. The attribute c_value defines a
    state/event table which constrains the allowed values of the attribute value in a
    DV_STATE instance, as well as the order of transitions between values.
    """
    
    implements(ICDvState)
    
    
    def __init__(self,value):
        self.value=value

class ITransition(Interface):
    """
    Definition of a state machine transition.
    """
    
    event = TextLine(
        title=_(u"Event"),
        description=_(u"""Event which fires this transition."""),
        
        )

    guard = TextLine(
        title=_(u"Guard"),
        description=_(u"""Guard condition which must be true for this transition to fire."""),
        required=False,
        )

    action = TextLine(
        title=_(u"Action"),
        description=_(u"""Side-effect action to execute during the firing of this transition."""),
        required=False,
        )

    nextState = Object(
        schema=IState,
        title=_(u"Next State"),
        description=_(u"""Target state of next transition. """),
        
        )
     
class INonTerminalState(Interface):
    """
    Definition of a non-terminal state in a state machine, i.e. one that has transitions.
    """
    
    transitions = Set(
        title=_(u"Transitions"),
        description=_(u"""A Set of Transition types. """),
        required=False,
        value_type=Object(schema=ITransition),
        )
 
class NonTerminalState(State):
    """
    Definition of a non-terminal state in a state machine, i.e. one that has transitions.
    """
    implements(INonTerminalState)
    
    def __init__(self,transitions):
        self.transitions=transitions
 

  
  
class StateMachine(grok.Model):
    u"""        
    Definition of a state machine in terms of states, transition events and outputs, and
    next states.
    """
    implements(IStateMachine)
    
    def __init__(self,states):
        self.states=states
      

class ITerminalState(Interface):
    """
    Definition of a terminal state in a state machine, i.e. a state with no exit transitions.
    """
    pass

class TerminalState(State):
    u"""
    Definition of a terminal state in a state machine, i.e. a state with no exit transitions.
    """
    implements(ITerminalState)

    def __init__(self,name):
        State.__init__(self,name)
        

    

class Transition(grok.Model):
    """
    Definition of a state machine transition.
    """
    implements(ITransition)
    
    def __init__(self,event,guard,action,nextstate):
        self.event=event
        self.guard=guard
        self.action=action
        self.nextState=nextstate
            
    
#Begin Quantity Datatypes package
class ICDvOrdinal(Interface):
    """
    Class specifying constraints on instances of DV_ORDINAL. Custom constrainer type for instances of DV_ORDINAL.
    """
    
    list_ = Set(
        title=_(u"List"),
        description=_(u"""Set of allowed DV_ORDINALS."""),
        value_type=Object(schema=IDvOrdinal),
        )
      
class CDvOrdinal(CDomainType):
    """
    Class specifying constraints on instances of DV_ORDINAL. Custom constrainer type for instances of DV_ORDINAL.
    """
    
    implements(ICDvOrdinal)
    
    
    def __init__(self,list):
        self.list=list
 
class ICQuantityItem(Interface):
    """
    Constrains instances of DvQuantity.
    """
    
  
    magnitude = Interval(
        title=_(u"Magnitude"),
        description=_(u"Interval constraint on magnitude."),
        required=False,
        )
    
    precision = Interval(
        title=_(u"Precision"),
        description=_(u"Interval constraint on precision."),
        required=False,
        )
  
    
    units = TextLine(
        title=_(u"Units"),
        description=_(u"""Constraint on units."""),
        
        )
    
    def precisionUnconstrained():       
        """
        True if no constraint on precision; True if precision = -1.
        precision = -1 implies Result
        """
         
        
class ICDvQuantity(Interface):
    """
    Constrains instances of DvQuantity.
    """
    
    list = List(
        title=_(u"List"),
        description=_(u"""List of value/unit pairs."""),
        required=False,
        value_type=Object(schema=ICQuantityItem),
        )
    
    property = Object(
        schema=ICodePhrase,
        title=_(u"Property"),
        description=_(u"""Optional constraint of units property."""),
        required=False
        )

    def anyAllowed():
        """True if any DVQuantity instance allowed"""
        
class CDvQuantity(CDomainType):
    """
    Constrains instances of DvQuantity.
    """
    implements(ICDvQuantity)
    
    def __init__(self,list,property):
        self.list=list
        self.property=property
        
    
    def anyAllowed():
        """True if any DVQuantity instance allowed."""
        return self.list == None and self.property == None
    
    def listValid():
        return self.list != None and self.list.__len__() == 0
    
    def overallValidity():
        return xor(self.list != None or self.property != None, self.anyAllowed())        
        
    
class ICQuantityItem(Interface):
    """
    Constrains instances of DvQuantity.
    """
    
  
    magnitude = Interval(
        title=_(u"Magnitude"),
        description=_(u"Interval constraint on magnitude."),
        required=False,
        )
    
    precision = Interval(
        title=_(u"Precision"),
        description=_(u"Interval constraint on precision."),
        required=False,
        )
  
    
    units = TextLine(
        title=_(u"Units"),
        description=_(u"""Constraint on units."""),
        
        )
    
    def precisionUnconstrained():       
        """
        True if no constraint on precision; True if precision = -1.
        precision = -1 implies Result
        """
        
        
class CQuantityItem(grok.Model):
    """
    Constrains instances of DvQuantity.
    """
    implements(ICQuantityItem)
    
    def __init__(self,magnitude,precision,units):
        self.magnitude=magnitude
        self.precision=precision
        self.units=units
    
    
    def precisionUnconstrained():       
        """
        True if no constraint on precision; True if precision = -1.
        precision = -1 implies Result
        """
        return precision == -1
        
#Begin Text Datatypes package
class ICCodePhrase(Interface):
    u"""
    Express constraints on instances of CODE_PHRASE. The terminology_id attribute
    may be specified on its own to indicate any term from a specified terminology;
    the code_list attribute may be used to limit the codes to a specific list.
    """
    
    terminologyId = Object(
        schema=ITerminologyId,
        title=_(u"Terminology ID"),
        description=_(u"""Syntax string expressing constraint on allowed primary terms."""),
        required=False,
        )

    codeList = List(
        title=_(u"Code List"),
        description=_(u"""List of allowed codes.  If empty it means any code is allowed."""),
        required=False,
        value_type=TextLine(),
    )
    
    
class CCodePhrase(CDomainType):
    u"""
    Express constraints on instances of CODE_PHRASE. The terminology_id attribute
    may be specified on its own to indicate any term from a specified terminology;
    the code_list attribute may be used to limit the codes to a specific list.
    """
    
    implements(ICCodePhrase)
    
 
    def __init__(self,termid,codelist):
        self.terminologyId=termid
        self.codeList=codelist
     
