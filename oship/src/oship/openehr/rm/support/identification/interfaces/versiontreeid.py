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


from zope.interface import Interface
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')

class IVersionTreeId(Interface):
    u"""
    Version tree identifier for one version. Lexical form:
    trunkVersion [ '.' branchNumber '.' branchVersion ]
    """
    
    value = TextLine(
        title=_(u"Value"),
        description=_(u"String form of this Version Tree identifier."),
        required=True
        )
        
    def trunkVersion():
        u"""
        Returns a string of the trunk version number; numbering starts at 1.     
        """
        
    def branchNumber():
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """

    def branchVersion():
        u"""
        Version of the branch; numbering starts at 1.
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
   
