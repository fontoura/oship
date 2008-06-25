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

from zope.location.interfaces import ILocation
from zope.location import Location
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

from openehr.rm.support.identification.objectversionid import ObjectVersionId
from objectref import IObjectRef

_ = MessageFactory('oship')


class ILocatableRef(IObjectRef,ILocation):
    u"""
    Reference to a LOCATABLE instance inside the top-level content structure inside a
    VERSION<T>; the path attribute is applied to the object that VERSION.data points to.
    """
    
    id = ObjectVersionId(
        title = _(u'Id'),
        description = _(u'id is redefined here to contain an ObjectVersionId. The identifier of the Version.'),
        required = True,
        )
    
    
    path = TextLine(
        title = _(u"Path"),
        description=_(u"""The path to an instance in question, as an absolute path 
        with respect to the object found at VERSION.data. An empty path means that
        the object referred to by id being specified."""),
        required = False,
        )
            
        
    def idExists():
        u""" id != None """
        
    def nameSpaceExists():
        u""" nameSpace != None and nameSpace != '' """
        
