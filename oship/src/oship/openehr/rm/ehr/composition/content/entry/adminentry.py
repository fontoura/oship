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
from interfaces.adminentry import IAdminEntry

_ = MessageFactory('oship')

   
class AdminEntry(Entry):
    """
    Entry subtype for administrative information, i.e. information about setting up the
    clinical process, but not itself clinically relevant. Archetypes will define con-
    tained information.
    Used for admistrative details of admission, episode, ward location, discharge,
    appointment (if not stored in a practice management or appointments system).
    
    Not used for any clinically significant information.
    """
    
    implements(IAdminEntry)
    
    
    def __init__(self,data):
        self.data=data
