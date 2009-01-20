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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.schema import TextLine,Object
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.identification.interfaces.uidbasedid import IUidBasedId
from objectref import IObjectRef

_ = MessageFactory('oship')


class ILocatableRef(IObjectRef):
    u"""
    Reference to a LOCATABLE instance inside the top-level content structure inside a
    VERSION<T>; the path attribute is applied to the object that VERSION.data points to.
    """
       
    id = Object(
        schema=IUidBasedId,
        title = _(u'Id'),
        description = _(u'Globally unique id of an object (of type UidBasedId), regardless of where it is stored.'),
        required = True
        )

    path = TextLine(
        title = _(u"Path"),
        description=_(u"""The path to an instance in question, as an absolute path 
        with respect to the object found at VERSION.data. An empty path means that
        the object referred to by id being specified."""),
        required = False
        )
            
        
    def asUri():
        u""" 
        A URI form of the reference, created by concatenating the following:
        "ehr://" + id.value + "/" + path
        """
        
        
