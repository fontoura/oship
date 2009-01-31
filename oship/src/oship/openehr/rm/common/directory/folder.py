# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the directory package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.archetyped.locatable import Locatable
from interfaces.folder import IFolder

_ = MessageFactory('oship')

class Folder(Locatable):
    u"""
    The concept of a named folder.
    """

    implements(IFolder)
    
    def __init__(self,folders,items):
        self.folders=folders
        self.items=items    
    
    def foldersValid():
        u"""folders != None and folders != '' """
        