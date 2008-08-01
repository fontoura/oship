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
from zope.schema import TextLine,Object,Int
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.interval import Interval
from oship.openehr.am.archetype.constraintmodel.interfaces.cattribute import ICAttribute
from oship.openehr.am.archetype.constraintmodel.interfaces.archetypeconstraint import IArchetypeConstraint

_ = MessageFactory('oship')


class ICObject(IArchetypeConstraint):
    """
    Abstract model of constraint on any kind of object node.
    """
    
    rmTypeName=TextLine(
        title=_(u"RM Type Name"),
        description=_(u"Reference model type that this node corresponds to."),
        required=True,
    )

    occurrences=Int(
        title=_(u"Occurrences"),
        description=_(u"Occurrences of this object node in the data."),
        required=True,
    )

    nodeId=TextLine(
        title=_(u"Node Id"),
        description=_(u"Semantic id of this node."),
        required=True,
    )

    
    parent=Object(
        schema=ICAttribute,
        title=_(u"Parent"),
        description=_(u"CAttribute that owns the CObject."),
        required=False,
    )
    
