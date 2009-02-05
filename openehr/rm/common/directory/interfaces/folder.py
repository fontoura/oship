# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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

from zope.schema import List,Object
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef

_ = MessageFactory('oship')

class IFolder(ILocatable):
    u"""
    The concept of a named folder.
    """

    folders = List(
        value_type=Object(schema=IObjectRef), # documented as a list of folders
        title=_(u"Folders"),
        description=_(u"""Subfolders of this folder."""),
        required=False,
        )
    
    items = List(
        value_type=Object(schema=IObjectRef),
        title=_(u"Items"),
        description=_(u"""The list of references to other (usually) versioned 
                    objects logically in this folder."""),
        required=False,
        )
    
    def foldersValid():
        u"""folders != None and folders != '' """

        