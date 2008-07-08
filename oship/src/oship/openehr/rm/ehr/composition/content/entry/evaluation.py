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
from interfaces.evaluation import IEvaluation

_ = MessageFactory('oship')

            
class Evaluation(CareEntry):
    """
    Entry type for evaluation statements.
    """
    
    implements(IEvaluation)
    classProvides(IEvaluation)
 
    def __init__(self,data,state):
        self.data=data
  
