# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementations for specifications for the navigation package from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.interface import implements,classProvides

from interfaces.section import ISection
from openehr.rm.ehr.composition.content.contentitem import ContentItem

_ = MessageFactory('oship')

class Section(ContentItem):
    """
    Represents a heading in a heading structure or 'section tree'.
    """

    implements(ISection)
    classProvides(ISection)
    
    def __init__(self,items,**kwargs):
        self.items=items
    
    