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

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 
from zope.interface import invariant

from objectref import IObjectRef

_ = MessageFactory('oship')


class IAccessGroupRef(IObjectRef):
    u""" Reference to access group in an access control service. """  
    
    type = TextLine(
        title = _(u"Type"),
        description = _(u"""Name of the class (concrete or abstract) of object to which this 
                          identifier type refers, e.g."PARTY", "PERSON", "GUIDELINE" etc.
                          These class names are from the relevant reference model. 
                          The type name "ANY" can be used to indicate that any type is accepted 
                          (e.g. if the type is unknown). """),
        required = True,
        )
    
    @invariant
    def validateType(self):
        return self.type in ["PERSON","PARTY","GUIDELINE"]
        
       