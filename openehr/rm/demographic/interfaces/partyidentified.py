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
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import Object
from zope.interface import Interface

from oship.openehr.rm.datastructures.itemstructure.interfaces.itemstructure import IItemStructure
from oship.openehr.rm.datatypes.text.interfaces.dvtext import IDvText
from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable

_ = MessageFactory('oship')


class IPartyIdentified(ILocatable):
    """
    An identity owned by a party.
    """
    
    details=Object(
        schema=IItemStructure,
        title=_(u"Details"),
        description=_(u"The value of the identitiy"),
        required=False,
    )
    
    purpose=Object(
        schema=IDvText,
        title=_(u"Purpose"),
        description=_(u"Purpose fo this identitiy."),
        required=True,
    )
    
    def asString():
        """
        Indentity in the form of a string.
        """
