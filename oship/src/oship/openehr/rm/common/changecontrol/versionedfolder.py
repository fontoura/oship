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


from zope.i18nmessageid import MessageFactory
from zope.interface import implements

from versionedobject import VersionedObject
from interfaces.versionedobject import IVersionedObject

_ = MessageFactory('oship')

class VersionedFolder(VersionedObject):
    u"""
    A version-controlled hierarchy of FOLDERs giving the effect of a directory.
    """
    
    implements(IVersionedObject)
    
    pass
    
