# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.identification.objectref import ObjectRef
from oship.openehr.rm.support.identification.interfaces.accessgroupref import IAccessGroupRef

_ = MessageFactory('oship')
       
class AccessGroupRef(ObjectRef):
    u""" Reference to access group in an access control service. """

    implements(IAccessGroupRef)
    
    def __init__(self,id,nameSpace,type):
        self.id=id
        self.nameSpace=nameSpace
        self.type=type     
        
    def validateType(self):
        u"""
        type is in "ACCESS_GROUP"
        """
        return self.type == 'ACCESS_GROUP'
        