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

from zope.interface import Interface
from zope.i18nmessageid.message import MessageFactory 
from zope.schema import Object 

from oship.openehr.am.archetype.constraintmodel.interfaces.cattribute import ICAttribute
from oship.openehr.am.archetype.constraintmodel.interfaces.cardinality import ICardinality
_ = MessageFactory('oship')


class ICMultipleAttribute(ICAttribute):
    """
    Abstract model of constraint on any kind of attribute node.
    """
    
    cardinality=Object(
        schema=ICardinality,
        title=_(u"Cardinality"),
        description=_(u"Cardinality of this attribute constraint."),
        required=True,
    )

    def members(cobj):
        """
        List of constraints representing members of the container value of this attribute.
        """
        
