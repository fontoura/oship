# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the change_control package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.i18nmessageid import MessageFactory
from zope.schema import Object
from version import Version
from interfaces.importedversion import IImportedVersion
from oship.openehr.rm.common.changecontrol.interfaces.originalversion import IOriginalVersion

_ = MessageFactory('oship')

class ImportedVersion(Version):
    u"""
    A Version containing locally created content and optional attestations.
    """
    implements(IImportedVersion)
    
    def __init__(self,item):
        self.item = item
        
    
   