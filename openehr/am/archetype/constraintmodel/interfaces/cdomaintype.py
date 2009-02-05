# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>'

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Object

from cdefinedobject import ICDefinedObject
from oship.openehr.am.archetype.constraintmodel.interfaces.ccomplexobject import ICComplexObject
_ = MessageFactory('oship')


class ICDomainType(ICDefinedObject):
    """
    Abstract parent of domain specific constrainer types.
    """
    
    standardEquivalent=Object(
        schema=ICComplexObject,
        title=_(u"Standard Equivalent"),
        description=_(u"Standard form of constraint."),
        required=True,
    )
    