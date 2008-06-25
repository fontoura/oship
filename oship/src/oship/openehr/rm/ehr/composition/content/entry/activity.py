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
from zope.interface import implements

from openehr.rm.common.archetyped.locatable import Locatable
from interfaces.activity import IActivity

_ = MessageFactory('oship')

   
class Activity(Locatable):
    """
    A single activity within an instruction.
    """
    
    implements(IActivity)
    
    def __init__(self,desc,tim,atid,**kwargs):
        self.description=desc
        self.timing=tim
        self.actionArchetypeId=atid
        
