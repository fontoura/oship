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
from interfaces.instruction import IInstruction

_ = MessageFactory('oship')

    
class Instruction(CareEntry):
    """
    Used to specify future actions and includes a workflow form.
    """
    
    implements(IInstruction)
    classProvides(IInstruction)
    
    def __init__(self,narr,act,exp,wfd,nodeid):
        self.narrative=narr
        self.activities=act
        self.expiryTime=exp
        self.wfDefinition=wfd
        self.__name__=nodeid
        