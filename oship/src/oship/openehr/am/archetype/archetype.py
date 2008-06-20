# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
From the archetype object model specification Rev 2.0.1
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'


from zope.interface import implements
from zope.schema import TextLine,Set
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.common.authoredresource import IAuthoredResource,AuthoredResource
from openehr.rm.support.archetypeid import ArchetypeId
from openehr.rm.support.objectid import ObjectId
from openehr.am.archetype.ccomplexobject import CComplexObject
from openehr.am.archetype.archetypeontology import ArchetypeOntology

_ = MessageFactory('oship')


class IArchetype(IAuthoredResource):
    """
    Archetype equivalent to ARCHETYPED class in Common reference model.
    Defines semantics of identfication, lifecycle, versioning, composition 
    and specialisation.
    """
    
    adlVersion = TextLine(
        title = _(u"adlVersion"),
        description = _(u"""ADL version if archteype was read in from 
                        an ADL sharable archetype."""),
        required = False,
        default = None
    )
    
    archetypeId=ArchetypeId(
        title=_(u"Archetype Id"),
        description=_(u"Multi-axial identifier of this archetype."),
        required=True,
    )
    
    uid=HierObjectId(
        title=_(u"UID"),
        description=_(u"OID of this archetype."),
        required=False,
    )
    
    concept=TextLine(
        title=_(u"Concept"),
        description=_(u"The normative meaning of archetype as a whole."),
        required=True,
    )
    
    parentArchetypeId=ArchetypeId(
        title=_(u"Parent Archetype Id"),
        description=_(u"Identifier of the specialsation parent of this archetype."),
        required=False,
    )
    
    definition=CComplexObject(
        title=_(u"Definition"),
        description=_(u"Root node of this archetype."),
        required=True,
    )

    ontology=ArchetypeOntology(
        title=_(u"Ontology"),
        description=_(u"The ontology of the archetype"),
        required=True,
    )

    invariants=Set(
        title=_(u"Invariants"),
        description=_(u"FOPL invariant statements"),
        required=False,
    )

    def version():
        """
        Version string extracted from id.
        """
        
    def previousVersion():
        """
        Version of predecessor if any.
        """
        
    def shortConceptName():
        """
        String extracted from id.
        """
        
    def conceptName():
        """
        Concept string extracted from the ontology.
        """
    
    def physicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        """
        
    def logicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        except the nodeIds are replaced by their meanings from the ontology.
        """
        
    def isSpecialised():
        """
        True if this archetype is a specialisation of another.
        Otherwise it returns False.
        """
        
    def specialisationDepth():
        """
        Return ontology.specialisationDepth
        """
    
    def nodeIdsValid():        
        """
        Return True if every CObject.nodeId is found
        in the ontolgy.termCodes
        """
        
    def internalReferencesValid():
        """
        True if every ArchetypeInternalRef.targetPath
        refers to a legitimate node in the archetype definition.
        """
        
    def constraintReferencesValid():
        """
        True if every ConstraintRef.reference found in CObject nodes
        definition is found in ontology.constraintCodes
        """
        
    def isValid():
        """
        Return True if the archetype is overall valid.
        """

class Archetype(AuthoredResource):
    """
    Archetype equivalent to ARCHETYPED class in Common reference model.
    Defines semantics of identfication, lifecycle, versioning, composition 
    and specialisation.
    """
    
    implements(IArchetype)
    
    def __init__(self,adlver,atid,uid,concept,paid,descr,defin,ont,inv,revhist,**kw):
        self.adlVersion=adlver
        self.archetypeId=atid
        self.uid=uid
        self.concept=concept
        self.parentArchetypeId=paid
        self.description=descr
        self.definition=defin
        self.ontology=ont
        self.invariants=inv
        self.revisionHistory=revhist
        for n,v in kw.items():
            setattr(self,n,v)
    
    def version():
        """
        Version string extracted from id.
        """
        
    def previousVersion():
        """
        Version of predecessor if any.
        """
        
    def shortConceptName():
        """
        String extracted from id.
        """
        
    def conceptName():
        """
        Concept string extracted from the ontology.
        """
    
    def physicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        """
        
    def logicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        except the nodeIds are replaced by their meanings from the ontology.
        """
        
    def isSpecialised():
        """
        True if this archetype is a specialisation of another.
        Otherwise it returns False.
        """
        
    def specialisationDepth():
        """
        Return ontology.specialisationDepth
        """
    
    def nodeIdsValid():        
        """
        Return True if every CObject.nodeId is found
        in the ontolgy.termCodes
        """
        
    def internalReferencesValid():
        """
        True if every ArchetypeInternalRef.targetPath
        refers to a legitimate node in the archetype definition.
        """
        
    def constraintReferencesValid():
        """
        True if every ConstraintRef.reference found in CObject nodes
        definition is found in ontology.constraintCodes
        """
        
    def isValid():
        """
        Return True if the archetype is overall valid.
        """
