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
from interfaces.uidbasedid import IUidBasedId

_ = MessageFactory('oship')
     
class UidBasedId(ObjectId):
    u"""
    Abstract model of UID-based identifiers consisting of a root part and an optional
    extension; lexical form: root '::' extension
    """

    implements(IUidBasedId)
    classProvides(IUidBasedId)

    def __init__(self, value):
        self.value = value


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''


    def root():
        u"""
        The identifier of the conceptual namespace in which the object exists, within 
        the identification scheme.
        Returns the part to the left of the first '::' separator, if any, or else the whole string.
        """


    def extension():
        u"""
        Optional local identifier of the object within the context of the root identifier.
        Returns the part to the right of the first '::' separator if any, or else any empty String.
        """


    def hasExtension():
        u""" True if extension != None """

        
    def rootValid():
        u""" True if root != None """
        
    def extensionValidity():
        u""" True if extension != None """
        
        
    def hasExtensionValidity():
        """ extension == '' xor hasExtension() """

