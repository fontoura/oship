# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

Implementations for specifications for the composition package from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from interfaces.eventcontext import IEventContext
from oship.openehr.rm.common.archetyped.pathable import Pathable

_ = MessageFactory('oship')
   
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
        
  