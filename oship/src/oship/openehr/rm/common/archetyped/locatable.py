# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the archetyped package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.i18nmessageid import MessageFactory
from zope.schema import Field

from openehr.rm.common.archetyped.pathable import Pathable
from interfaces.locatable import ILocatable

_ = MessageFactory('oship')
       
class Locatable(Pathable):
    """
    Root class of all information model classes that can be archetyped.
    """

    implements(ILocatable)
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links,**kw):
        self.uid=uid
        self.archetypeNodeId=atnodeid
        self.name=name
        self.archetypeDetails=atdetails
        self.feederAudit=fdraudit
        self.links=links
        for n,v in kw.items():
            setattr(self,n,v)
           
    def isArchetypeRoot():
        """True if this node is the root of an archetyped structure."""
        
    def concept():
        """
        Clinical concept of the archetype as a whole (= derived from the
       'archetype_node_id' of the root node) isArchetypeRoot must be True.
       """
        
    def nameValid():
        """ name != None"""
          
    def linksValid():
        """ links != None and links != []"""
 
    def archetypedValid():
        """ isArchetypeRoot xor archetypeDetails = None """
        
    def archetypeNodeIdValid():
        """ archetypeNodeId != None and archetypeNodeId != '' """
