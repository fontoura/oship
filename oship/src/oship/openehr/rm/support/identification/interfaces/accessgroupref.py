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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

from objectref import IObjectRef

_ = MessageFactory('oship')


class IAccessGroupRef(IObjectRef):
    u""" Reference to access group in an access control service. """

    id = TextLine(
        title = _(u"Id"),
        description = _(u"Globally unique id of an object, regardless of where it is stored."),
        required = True,
        )
    
    nameSpace = TextLine(
        title = _(u"Namespace"),
        description = _(u"""Namespace to which this identifier belongs in
                       the local system context (and possibly in any
                       other openEHR compliant environment) e.g.
                       "terminology", "demographic". These names
                       are not yet standardised. Legal values for the
                       namespace are
                       "local" | "unknown" | "[a-zA-
                       Z][a-zA-Z0-9_-:/&+?]*" """),
        required = True,
        )
    
    
    type = TextLine(
        title = _(u"Type"),
        description = _(u"""Name of the class (concrete or abstract) of object to which this 
                          identifier type refers, e.g."PARTY", "PERSON", "GUIDELINE" etc.
                          These class names are from the relevant reference model. 
                          The type name "ANY" can be used to indicate that any type is accepted 
                          (e.g. if the type is unknown). """),
        required = True,
        )
        
        
    def idExists():
        u""" id != None """
        
    def nameSpaceExists():
        u""" nameSpace != None and nameSpace != '' """
        
    def typeExists():
        u""" type != None and type != '' """    
    
    def typeValidity():
        u""" True if type == 'ACCESS_GROUP' """
        