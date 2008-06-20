﻿# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

    
class IContact(ILocatable):
    """
    Description of a means of contacting a party.
    """
    
    timeValidity=DvInterval(
        title=_("Time Validity"),
        description=_("Valid time interval for this contact descriptor."),
        requires=False,
    )
    
    addresses=List(
        title=_("Addresses"),
        description=_("A set of addresses for this purpose and time frame."),
        required=True,
    )
    
    def purpose():
        """
        Purpose for which this contact is used.
        Taken from the inherited 'name' attribute.        
        """
     
class Contact(Locatable):
    """
    Description of a means of contacting a party.
    """
    
    timeValidity=DvInterval(
        title=_("Time Validity"),
        description=_("Valid time interval for this contact descriptor."),
        requires=False,
    )
    
    addresses=List(
        title=_("Addresses"),
        description=_("A set of addresses for this purpose and time frame."),
        required=True,
    )
    
    def purpose():
        """
        Purpose for which this contact is used.
        Taken from the inherited 'name' attribute.        
        """
    
