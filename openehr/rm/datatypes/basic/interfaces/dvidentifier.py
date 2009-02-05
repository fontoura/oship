# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the data types specification Rev 2.1.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements 
from zope.schema import Text
from zope.i18nmessageid.message import MessageFactory 

from datavalue import IDataValue

_ = MessageFactory('oship')
    
class IDvIdentifier(IDataValue):
    """
    Type for representing identifiers of real-world entities. Typical identifiers include
    drivers licence number, social security number, veterans affairs number, prescrip-
    tion id, order id, and so on.
    
    DV_IDENTIFIER is used to represent any identifier of a real thing, issued by
    some authority or agency.

    DV_IDENTIFIER is not used to express identifiers generated by the infrastruc-
    ture to refer to information items; the types OBJECT_ID and OBJECT_REF and
    subtypes are defined for this purpose.
    """
    
    issuer = Text(
        title = _(u"Issuer"),
        description = _(u"""Authority which issues the kind of id used in the id field  
                      of this object."""),
        required = True,
        )
    
    assignor = Text(
        title = _(u"Assignor"),
        description = _(u"""Organisation that assigned the id to the item being identified."""),
        required = True
        )
    
    id = Text(
        title = _(u"Id"),
        description = _(u""" The identifier value. Often structured, according to the 
                      definition of the issuing authority's rules."""),
        required = True
        )
    
    type = Text(
        title = _(u"Type"),
        description = _(u"""The identifier type, such as "prescription",or "SSN". 
                      One day a controlled vocabulary might be possible for this."""),
        required = True
        )
    