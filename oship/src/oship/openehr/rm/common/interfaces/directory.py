# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

These are the interfaces for the directory package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.app.container.interface import IContainer

from zope.schema import Field
from zope.schema import Text
from zope.schema import TextLine
from zope.schema import List

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class IVersionedFolder(IVersionedObject):
    u"""
    A version-controlled hierarchy of FOLDERs giving the effect of a directory.
    """
    pass
    

class IFolder(ILocatable, IContainer):
    u"""
    The concept of a named folder.
    """

    folders = List(
        title=_(u"""Folders"""),
        description=_(u"""Subfolders of this folder."""),
        required=False,
        )
    
    items = List(
        title=_(u"""Items"""),
        description=_(u"""The list of references to other (usually) versioned 
                    objects logically in this folder."""),
        required=False,
        )
    
    def foldersValid():
        u"""folders != None and folders != '' """
        