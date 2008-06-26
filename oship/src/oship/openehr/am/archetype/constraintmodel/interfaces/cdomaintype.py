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

from cdefinedobject import ICDefinedObject
from openehr.am.archetype.constraintmodel.ccomplexobject import CComplexObject
_ = MessageFactory('oship')


class ICDomainType(ICDefinedObject):
    """
    Abstract parent of domain specific constrainer types.
    """
    
    standardEquivalent=CComplexObject(
        title=_("Standard Equivalent"),
        description=_("Standard form of constraint."),
        required=True,
    )
    
