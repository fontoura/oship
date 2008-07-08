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

from zope.location import Location
from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from objectref import ObjectRef
from interfaces.locatableref import ILocatableRef

_ = MessageFactory('oship')
       
class LocatableRef(ObjectRef,Location):
    u"""
    Reference to a LOCATABLE instance inside the top-level content structure inside a
    VERSION<T>; the path attribute is applied to the object that VERSION.data points to.
    """

    implements(ILocatableRef)
    classProvides(ILocatableRef)
    
    def __init__(self,id,path):
        self.id=id
        self.path=path
       
    def idExists():
        u""" id != None """
        
    def nameSpaceExists():
        u""" nameSpace != None and nameSpace != '' """
        
    def typeExists():
        u""" type != None and type != '' """
    
    def asUri():
        u"""
        A URI form of the reference, created by concatenating the following:
        "ehr://" + id.value + "/" + path
        """
        
    def pathValid():
        u""" path != None and path != '' """
    def typeExists():
        u""" type != None and type != '' """
    
    def asUri():
        u"""
        A URI form of the reference, created by concatenating the following:
        "ehr://" + id.value + "/" + path
        """
        
    def pathValid():
        u""" path != None and path != '' """

