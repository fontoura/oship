# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

The interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import Object

from careentry import ICareEntry
from oship.openehr.rm.datastructures.history.interfaces.history import IHistory

_ = MessageFactory('oship')

class IObservation(ICareEntry):
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
    
