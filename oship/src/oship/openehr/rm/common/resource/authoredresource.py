# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the resource package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
 
from zope.i18nmessageid import MessageFactory
from zope.interface import implements
from zope.schema import Field

from interfaces.authoredresource import IAuthoredResource


_ = MessageFactory('oship')

class AuthoredResource(Field):
    u"""Abstract idea of an online resource created by a human author. """
    
    implements(IAuthoredResource)
    
    def __init__(self, olang,trans,descr,revhist,ctrld,**kw):
        self.originalLanguage=olang
        self.translations=trans
        self.description=descr
        self.revisionHistory=revhist
        self.isControlled=ctrld
        for n,v in kw.items():
            setattr(self,n,v)

    def currentRevision():
        u""" """
         
    def languagesAvailable():
        u""" """
                                
    