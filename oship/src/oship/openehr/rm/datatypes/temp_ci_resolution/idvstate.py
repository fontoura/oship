# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The basic openEHR data types interfaces. From the data types specification Rev 2.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.schema import Text,TextLine
from zope.schema import Bool 
from zope.i18nmessageid import MessageFactory

from openehr.rm.datatypes.interfaces.idatavalue import IDataValue


_ = MessageFactory('oship')

class IDvState(IDataValue):
    """
    For representing state values which obey a defined state machine, such as a vari-
    able representing the states of an instruction or care process.
    
    DV_STATE is expressed as a String but its values are driven by archetype-
    defined state machines. This provides a powerful way of capturing stateful com-
    plex processes in simple data.
    """
    
    value = TextLine(
        title = _(u"value"),
        description = _(u"""The state name. State names are determined by a state/event 
                      table defined in archetypes, and coded using openEHR Terminology 
                      or local archetype terms, as specified by the archetype.
                      
                      A module was added to the rm.support package to parse the State 
                      values from the archetype in the current context. This function 
                      is DvStateParser() and it may be called anywhere in the application
                      that the developer needs to know the current available states.
                      It returns a DvCodedText type.
                      """),
        required = True,
        )
    
    isTerminal = Bool(
        title = _(u"isTerminal"),
        description= _(u"""Indicates whether this state is a terminal
                      state, such as “aborted”, “completed” etc
                      from which no further transitions are possible.
                      It is required and the default is False.
                      """),
        required = True,
        default = False
        )
    
    