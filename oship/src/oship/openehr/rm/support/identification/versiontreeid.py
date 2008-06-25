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

from zope.interface import implements 
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory 

from interfaces.versiontreeid import IVersionTreeId

_ = MessageFactory('oship')

class VersionTreeId(Field):
    u"""
    Version tree identifier for one version. Lexical form:
    trunkVersion [ '.' branchNumber '.' branchVersion ]
    """
    
    implements(IVersionTreeId)

    def __init__(self, value,**kw):
        self.value = value
        for n,v in kw.items():
            setattr(self,n,v)


    def valueValid(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''
        
    def trunkVersion():
        u"""
        Returns a string of the trunk version number; numbering starts at 1.     
        """
        
    def branchVersion():
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """

    def isBranch():
        u"""
        Returns True if this version identifier represents a branch,
        i.e. has branchNumber and branchVersion parts.
        """
    
    def isFirst():
        u"""
        True if this version identifier corresponds to the
        first version, i.e. trunkVersion == "1"
        """
        
    def trunkVersionValid():
        u"""
        trunkVersion != None and isinstance(trunkVersion, int) and trunkVersion >= 1
        """

    def branchNumberValid():
        """
        branchNumber != None and isinstance(branchNumber, int) and branchNumber >= 1
        """
    
    def branchVersionValid():
        u"""
        branchVersion != None and isinstance(branchVersion, int) and branchVersion >= 1
        """
        
    def branchValidity():
        u"""
        (branchNumber == None and branchVersion == None ) xor
        (branchNumber != None and branchVersion != None )
        """
        
    def isBranchValidity():
        u""" isBranch xor (branchNumber == None) """
        
    def isFirstValidity():
        u""" not isFirst xor trunkVersion == "1" """

