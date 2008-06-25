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

from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from openehr.rm.datatypes.text.dvtext import DvText
from openehr.rm.common.archetyped.interfaces.locatable import ILocatable

_ = MessageFactory('oship')


class IPartyIdentity(ILocatable):
    """
    An identity owned by a party.
    """
    
    details=ItemStructure(
        title=_("Details"),
        description=_("The value of the identitiy"),
        required=False,
    )
    
    purpose=Dvtext(
        title=_("Purpose"),
        description=_("Purpose fo this identitiy."),
        required=True,
    )
    
    def asString():
        """
        Indentity in the form of a string.
        """
