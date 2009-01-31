# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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
__contributors__ = 'Andre Goncalves <goncalves.aluiz@gmail.com>'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from careentry import CareEntry
from interfaces.evaluation import IEvaluation

_ = MessageFactory('oship')

            
class Evaluation(CareEntry):
    """
    Entry type for evaluation statements.
    """
    
    implements(IEvaluation)
 
    def __init__(self,data,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links):
        CareEntry.__init__(self,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)        
        self.data=data
        
  
