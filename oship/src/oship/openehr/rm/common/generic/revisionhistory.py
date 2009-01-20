# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the generic package as described in the 
Common Information Model Rev. 2.1.0 

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid import MessageFactory

from interfaces.revisionhistory import IRevisionHistory

_ = MessageFactory('oship')        
        
class RevisionHistory(object):
    u"""
    Defines the notion of a revision history of audit items, each associated 
    with the version for which that audit was committed. The list is in 
    most-recent-first order.
    """

    implements(IRevisionHistory)
    
    def __init__(self,items):
        self.items=items
        self.__name__=''

    def mostRecentVersion():
        u"""The version id of the most recent item, as a String. 
        Ensure Result.is_equal(items.last.version_id.value)"""
        
    def mostRecentVersionTimeCommitted():
        u"""The commit date/time of the most recent item, as a string.
        Ensure Result.is_equal(items.last.audits.first.time_committed.value)"""
        
    def itemsValid():
        u"""items != None """
        
