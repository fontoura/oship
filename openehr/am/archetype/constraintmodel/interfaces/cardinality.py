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


from zope.schema import Bool
from zope.interface import Interface
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.interval import Interval

_ = MessageFactory('oship')

class ICardinality(Interface):
    """
    Expresses constraints on the cardinality of container classes.
    """
    
    isOrdered=Bool(
        title=_(u"Ordered"),
        description=_(u"True if members are ordered."),
        required=True,
    )

    isUnique=Bool(
        title=_(u"Unique"),
        description=_(u"True if members are unique."),
        required=True,
    )
    
    interval=Interval(
        title=_(u"Interval"),
        description=_(u"Interval of this cardinality."),
        required=True,
    )
    
    def isBag():
        """
        Return True if this cardinality represents an unordered set.
        """
        
    def isList():
        """
        Return True if this cardinality represents an ordered, non-unique membership.
        """
        
    def isSet():
        """
        Return True if this cardinality represents an unordered, non-unique membership.
        """
        