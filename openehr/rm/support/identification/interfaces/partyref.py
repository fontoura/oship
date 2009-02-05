# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef

_ = MessageFactory('oship')


class IPartyRef(IObjectRef):
    u"""
    Identifier for parties in a demographic or identity service. There are typically a
    number of subtypes of the PARTY class, including PERSON, ORGANISATION, etc.

    Abstract supertypes are allowed if the referenced object is of a type not known by
    the current implementation of this class (in other words, if the demographic model
    is changed by the addition of a new PARTY or ACTOR subtypes, valid
    PartyRefs can still be constructed to them).
    """

    type = TextLine(
        title = _(u"Type"),
        description = _(u"""Name of the class (concrete or abstract) of object to which this 
                        identifier type refers, e.g."PARTY", "PERSON", "GUIDELINE" etc.
                        These class names are from the relevant reference model. 
                        The type name "ANY" can be used to indicate that any type is accepted 
                        (e.g. if the type is unknown). """),
        required = True,
        #constraint = validateType
        )
    