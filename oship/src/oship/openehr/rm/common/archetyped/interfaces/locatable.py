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

from zope.schema import TextLine,List
from zope.i18nmessageid import MessageFactory

from openehr.rm.support.identification.uidbasedid import UidBasedId
from openehr.rm.datatypes.text.dvtext import DvText
#from openehr.rm.common.archetyped.archetyped import Archetyped
#from openehr.rm.common.archetyped.feederaudit import FeederAudit
from pathable import IPathable

_ = MessageFactory('oship')

        
class ILocatable(IPathable):
    """
    Root class of all information model classes that can be archetyped.
    """
    

    uid = UidBasedId('',
        title=_(u"UID"),
        description=_(u"Optional globally unique object identifier for root points of archetyped structures. A UidBasedId "),
        required=False,
        )
    
    archetypeNodeId = TextLine(
        title=_("Node ID"),
        description=_(u"""Design-time archetype id of this node taken from its generating archetype;
                     used to build archetype paths. Always in the form of an “at” code, e.g. “at0005”.
                     This value enables a "standardised" name for this node to be generated, by
                     referring to the generating archetype local ontology.
                     
                     At an archetype root point, the value of this attribute is always the stringified
                     form of the archetype_id found in the archetype_details object."""),
        required=True,
        )
    
    name = DvText('','','','','','',
        title=_(u"Name"),
        description=_(u"""DvText type - Runtime name of this fragment, used to build runtime paths. 
                     This is the term provided via a clinical application or batch
                     process to name this EHR construct: its retention in the EHR 
                     faithfully preserves the original label by which this entry
                     was known to end. """),
        required=True,
        )

    """
    archetypeDetails = Archetyped(
        title=_(u"Archetype Details"),
        description=_(u"Details of archetyping used on this node."),
        required=False,
        )
    """
    archetypeDetails = TextLine(
        title=_(u"Archetype Details"),
        description=_(u"Details of archetyping used on this node."),
        required=False,
        )
    
    feederAudit = List(
        title=_(u"Feeder Audit"),
        description=_(u"""Audit trail from non-openEHR system of original commit of information 
                    forming the content of this node, or from a conversion gateway which has 
                    synthesised this node."""),
        required=False,
        )
    
    
    links = List(
        title=_(u"Links"),
        description=_(u"""Audit trail from non-openEHR system of original commit of information 
                    forming the content of this node, or from a conversion gateway which has 
                    synthesised this node."""),
        required=False,
        )
    
    
    def isArchetypeRoot():
        """True if this node is the root of an archetyped structure."""
        
    def concept():
        """
        Clinical concept of the archetype as a whole (= derived from the
       ‘archetype_node_id’ of the root node) isArchetypeRoot must be True.
       """
        
    def nameValid():
        """ name != None"""
          
    def linksValid():
        """ links != None and links != []"""
 
    def archetypedValid():
        """ isArchetypeRoot xor archetypeDetails = None """
        
    def archetypeNodeIdValid():
        """ archetypeNodeId != None and archetypeNodeId != '' """
