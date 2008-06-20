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
from zope.schema import Text, TextLine, Field

class ICObject(Interface):
    """
    Abstract model of constraint on any kind of object node.
    """
    
    rmTypeName=TextLine(
        title=_("RM Type Name"),
        description=_("Reference model type that this node rcorresponds to."),
        required=True,
    )

    occurences=Interval(
        title=_("Occurences"),
        description=_("Occurences of this object node in the data."),
        required=True,
    )

    nodeId=TextLine(
        title=_("Node Id"),
        description=_("Semantic id of this node."),
        required=True,
    )

    parent=CAttribute(
        title=_("Parent"),
        description=_("CAttribute that owns the CObject."),
        required=False,
    )

class CObject(Field):
    """
    Abstract model of constraint on any kind of object node.
    """
    
    implements(ICObject)
