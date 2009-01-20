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

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory 

from interfaces.versiontreeid import IVersionTreeId
import re

_ = MessageFactory('oship')

class VersionTreeId(object):
    u"""
    Version tree identifier for one version. Lexical form:
    trunkVersion [ '.' branchNumber '.' branchVersion ]
    """
    
    implements(IVersionTreeId)

    PATTERN = r"[1-9](\d)*(\.(\d)+\.(\d)+)?"    
    
    def __init__(self, value):
        self.__branchNumber = None
        self.__branchVersion = None
        match = re.compile(self.PATTERN).match(value)
        if (match is None) or (match.start() != 0) or (match.end() != len(value)):
            raise(ValueError, 'wrong format')

        branch = value.find('.')
        if branch < 0: # no branch, just trunk
            self.__trunkVersion = value;
            self.value = value;
        else:
            entries = value.split(r".")
            self.__validateValues(int(entries[0]), int(entries[1]), int(entries[2]))
            self.__trunkVersion = entries[0]
            # never set branchNo or branchV to 0
            if int(entries[1]) > 0:
                self.__branchNumber = entries[1]
                self.__branchVersion = entries[2]
                self.value = value;
            else:
                self.value = entries[0]
    
    def __validateValues(self, trunk, branchNo, branchV):
        if (trunk < 1) or (branchNo < 0) or (branchV < 0):
            raise(ValueError, 'version number smaller than 0')

        # 0 for branchNo or branchV is special case,
        # where both must be 0 to indicate no branch
        if (branchNo == 0) or (branchV == 0):
            if branchV != branchNo:
                raise(ValueError, 'breach of branch_validity') 
        
        
    def trunkVersion(self):
        u"""
        Returns a string of the trunk version number; numbering starts at 1.     
        """
        return self.__trunkVersion
        

    def branchNumber(self):
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """
        return self.__branchNumber
         
    def branchVersion(self):
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """
        return self.__branchVersion

    def isBranch():
        u"""
        Returns True if this version identifier represents a branch,
        i.e. has branchNumber and branchVersion parts.
        """
        return not self.__branchVersion is None
    
    def isFirst(self):
        u"""
        True if this version identifier corresponds to the
        first version, i.e. trunkVersion == "1"
        """
        return self.__trunkVersion == '1' and  (not self.isBranch())

    def __loadValue(self, value):
        match = re.compile(self.PATTERN).match(value)
        if (match is None) or (match.start() != 0) or (match.end() != len(value)):
            raise(ValueError, 'wrong format')

        branch = value.find('.')
        if branch < 0: # no branch, just trunk
            self.__trunkVersion = value;
            self.value = value;
        else:
            entries = value.split(r".")
            self.__validateValues(int(entries[0]), int(entries[1]), int(entries[2]))
            self.__trunkVersion = entries[0]
            # never set branchNo or branchV to 0
            if int(entries[1]) > 0:
                self.__branchNumber = entries[1]
                self.__branchVersion = entries[2]
                self.value = value;
            else:
                self.value = entries[0]
    
    def __validateValues(self, trunk, branchNo, branchV):
        if (trunk < 1) or (branchNo < 0) or (branchV < 0):
            raise(ValueError, 'version number smaller than 0')

        # 0 for branchNo or branchV is special case,
        # where both must be 0 to indicate no branch
        if (branchNo == 0) or (branchV == 0):
            if branchV != branchNo:
                raise(ValueError, 'breach of branch_validity') 
     
    def branchNumber(self):
        return self.__branchNumber
   
    def __eq__(self, other):
        if not isinstance(other,  VersionTreeId):
            return False
        return self.value == other.value
