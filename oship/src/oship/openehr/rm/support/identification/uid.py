# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements 
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory 

from interfaces.uid import IUid

_ = MessageFactory('oship')
        
class Uid(Field):
    u"""
    Abstract parent of classes representing unique identifiers which identify informa-
    tion entities in a durable way. UIDs only ever identify one IE in time or space and
    are never re-used.
    """
    
    implements(IUid)

    def __init__(self, value,**kw):
        self.value = value
        for n,v in kw.items():
            setattr(self,n,v)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        
        return self.value!=None and self.value!=''
            
