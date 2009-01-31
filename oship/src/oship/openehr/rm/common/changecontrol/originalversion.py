# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the change_control package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
 
from zope.i18nmessageid import MessageFactory
from zope.schema import Container
from zope.interface import implements

from interfaces.originalversion import IOriginalVersion
_ = MessageFactory('oship')

class OriginalVersion(Container):
    u"""
    A Version containing locally created content and optional attestations.
    """
    
    implements(IOriginalVersion)
    
    def __init__(self,uid,previd):
        self.uid=uid
        self.precedingVersionUid=previd
        
  
    
