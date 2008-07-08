# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

Implementations for specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.interface import implements,classProvides

from entry import Entry
from interfaces.careentry import ICareEntry

_ = MessageFactory('oship')

    
class CareEntry(Entry):
    """
    The abstract parent of all clinical ENTRY subtypes. A CARE_ENTRY defines 
    protocol and guideline attributes for all clinical Entry subtypes.
    """

    implements(ICareEntry)
    classProvides(ICareEntry)
    
    def __init__(self,protocol,gid):
        self.protocol=protocol
        self.guidelineId=gid
            
