# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

The interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import Object

from oship.openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from entry import IEntry

_ = MessageFactory('oship')

    
class IAdminEntry(IEntry):
    u"""
        Entry subtype for administrative information, i.e. information about setting up the
        clinical process, but not itself clinically relevant. Archetypes will define con-
        tained information.
        Used for admistrative details of admission, episode, ward location, discharge,
        appointment (if not stored in a practice management or appointments system).
        
        Not used for any clinically significant information.
    """
    
    data = Object(
        schema=IItemStructure,
        title=u"""data""",
        description=u"""The data of the Entry; modelled in archetypes.""",
        required=True
        )
    
 