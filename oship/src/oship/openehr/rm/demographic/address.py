# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

From the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.interface import implements,classProvides

from oship.openehr.rm.common.archetyped.locatable import Locatable

_ = MessageFactory('oship')

class Address(Locatable):
    """
    Address of contact.
    """
    
    details=ItemStructure(
        title=_(u"Details"),
        description=_(u"The details of the address."),
        required=False,
    )
    
    
       
    
    def type():
        """
        Return the type of address from 'name'.
        """
    
    def asString():
        """
        Address in the form of a string.
        """