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
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

import objectid

_ = MessageFactory('oship')


class ITemplateId(IObjectId):
    u""" Identifier for templates. Lexical form to be determined. """
    
    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        default=_(u""),
        required=True)
    
    def valueExists():
        u"""        
        value != None and then not value != ''
        """
    
class TemplateId(ObjectId):
    u""" Identifier for templates. Lexical form to be determined. """
    
    implements(ITemplateId)

    def __init__(self, value,**kw):
        self.value = value
        for n,v in kw.items():
            setattr(self,n,v)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''
    