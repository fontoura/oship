# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements,classProvides

from oship.openehr.am.archetype.constraintmodel.creferenceobject import CReferenceObject
from oship.openehr.am.archetype.constraintmodel.interfaces.archetypeinternalref import IArchetypeInternalRef

_ = MessageFactory('oship')

class ArchetypeInternalRef(CReferenceObject):
    """
    See the AOM reference document.
    """
    
    implements(IArchetypeInternalRef)
    
    
    def __init__(self,tgtpath):
        self.tgtpath=tgtpath
