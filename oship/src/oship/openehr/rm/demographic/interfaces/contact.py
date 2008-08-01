# -*- coding: utf-8 -*-
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
__Contributors__ = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import List,Object

from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from oship.openehr.rm.datatypes.quantity.interfaces.dvinterval import IDvInterval
from oship.openehr.rm.demographic.interfaces.contact import IContact

_ = MessageFactory('oship')

    
class IContact(ILocatable):
    """
    Description of a means of contacting a party.
    """
    
    timeValidity=Object(
        schema=IDvInterval,
        title=_(u"Time Validity"),
        description=_(u"Valid time interval for this contact descriptor."),
        requires=False,
    )
    
    addresses=List(
        value_type = Object(schema = IContact),
        title=_(u"Addresses"),
        description=_(u"A set of addresses for this purpose and time frame."),
        required=True,
    )
    
    def purpose():
        """
        Purpose for which this contact is used.
        Taken from the inherited 'name' attribute.        
        """
