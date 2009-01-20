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
from zope.schema import List, TextLine,Int, Object
from zope.i18nmessageid.message import MessageFactory


from oship.openehr.rm.support.interval import Interval
from archetypeconstraint import IArchetypeConstraint
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef

_ = MessageFactory('oship')


class ICAttribute(IArchetypeConstraint):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    rmAttributeName=TextLine(
        title=_(u"RM Attribute Name"),
        description=_(u"Reference model attribute within the enclosed type representedby a CObject."),
        required=True,
    )
    
    existence=Int(
        title=_(u"Existence"),
        description=_(u"Indicates whether the target object exists or not."),
        required=True,
    )

    #children=List(
        #title=_(u"Children"),
        #description=_(u"Child constraint nodes."),
        #required=False,
        #value_type=Object(schema=ICObject),
    #)
    
    children=List(
        title=_(u"Children"),
        description=_(u"Child constraint nodes."),
        required=False,
        value_type=Object(schema=IObjectRef),
    )
    

