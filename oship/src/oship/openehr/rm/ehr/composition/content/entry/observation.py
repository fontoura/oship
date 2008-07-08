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
from zope.interface import implements,classProvides

from careentry import CareEntry
from interfaces.observation import IObservation

_ = MessageFactory('oship')

    
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
    classProvides(IObservation)
    
    def __init__(self,data,state):
        self.data=data
        self.state=state
 
            
            
            