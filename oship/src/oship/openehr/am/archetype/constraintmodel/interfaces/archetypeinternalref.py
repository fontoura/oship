# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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
from zope.interface import implements
from zope.schema import Text, TextLine, Field

from openehr.am.archetype.creferenceobject import ICReferenceObject,CReferenceObject

_ = MessageFactory('oship')


class IArchetypeInternalRef(ICReferenceObject):
    """
    See the AOM reference document.
    """
    
    targetPath=TextLine(
        title=_(u"Target Path"),
        description=_(u"Reference to an object node using archetype path notation."),
        required=True,
    )

class ArchetypeInternalRef(CReferenceObject):
    """
    See the AOM reference document.
    """
    
    implements(IArchetypeInternalRef)
    
    def __init__(self,tgtpath,**kw):
        self.tgtpath=tgtpath
        for n,v in kw.items():
            setattr(self,n,v)
