# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementations for specifications for the content package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Andre Goncalves <goncalves.aluiz@gmail.com>'

from zope.i18nmessageid import MessageFactory
from zope.schema import Container
from zope.interface import implements

from oship.openehr.rm.ehr.composition.content.interfaces.contentitem import IContentItem
from oship.openehr.rm.common.archetyped.locatable import Locatable 

_ = MessageFactory('oship')

class ContentItem(Container):
    """
    Abstract ancestor of all concrete content types.
    """
    
    implements(IContentItem)
    
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
    