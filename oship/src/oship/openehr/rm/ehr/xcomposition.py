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

from openehr.rm.ehr.interfaces.composition import *

_ = MessageFactory('oship')

class Composition(Locatable):
    """
    One version in a VersionedComposition.  A composition is considered the unit of modification in an EHR.
    """
    
    implements(IComposition)
    
    def __init__(self,content,context,composer,cat,lang,terr,persist,**kwargs):
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
    
    def __init__(self,hcf,start,end,part,loc,sett,other,**kwargs):
        self.healthCareFacility=hcf
        self.startTime=start
        self.endTime=end
        self.participations=part
        self.location=loc
        self.setting=sett
        self.otherContext=other
        
  
    
    
    
    