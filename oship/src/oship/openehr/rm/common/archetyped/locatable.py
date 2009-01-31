# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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
__contibutors__ = u'Fabricio Ferracioli <fabricioferracioli@gmail.com>'

from zope.interface import implements
from zope.i18nmessageid import MessageFactory
from zope.schema import Field

from oship.openehr.rm.common.archetyped.pathable import Pathable
from oship.openehr.rm.common.archetyped.interfaces.locatable import ILocatable
from operator import xor

_ = MessageFactory('oship')
       
class Locatable(Pathable):
    """
    Root class of all information model classes that can be archetyped.
    """

    implements(ILocatable)
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links):
        self.uid=uid
        self.archetypeNodeId=self.__name__=atnodeid
        self.name=name
        self.archetypeDetails=atdetails
        self.feederAudit=fdraudit
        self.links=links
           
    def isArchetypeRoot():
        """True if this node is the root of an archetyped structure. At specification there's a requiment for archetypeDetails in all root points in data
        """
        return self.archetypeDetails != None
        
    def concept():
        """
        Clinical concept of the archetype as a whole (= derived from the
       'archetype_node_id' of the root node) isArchetypeRoot must be True.
       """
        if (self.isArchetypeRoot()):
            return DvText(self.archetypeDetails.archetypeId.conceptName())
        raise TypeError('Not root node')
        
    def nameValid():
        """ name != None"""
        return self.name != None
          
    def linksValid():
        """ links != None and links != []"""
        if self.links != None:
            return self.links != []
        return self.links == None
 
    def archetypedValid():
        """ isArchetypeRoot xor archetypeDetails = None """
        return xor(self.isArchetypeRoot(), self.archetypeDetails == None)
        
    def archetypeNodeIdValid():
        """ archetypeNodeId != None and archetypeNodeId != '' """
        if(self.archetypeNodeId != None):
            return self.archetypeNodeId != ''
        return self.archetypeNodeId == None
