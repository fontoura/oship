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


from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from objectid import ObjectId

_ = MessageFactory('oship')
      
class GenericId(ObjectId):
    u"""
    Generic identifier type for identifiers whose format is othterwise unknown to openEHR. 
    Includes an attribute for naming the identification scheme (which may well be local).
    """

    implements(IGenericId)
    classProvides(IGenericId)

    def __init__(self,scheme,**kw):
        self.scheme=scheme
        for n,v in kw.items():
            setattr(self,n,v)


    def schemeValid():
        return self.scheme!=None and self.scheme!=''
        
