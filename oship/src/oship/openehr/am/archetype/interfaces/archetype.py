# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
The archetypes interfaces. 
From the archetype object model specification Rev 2.0.1
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.schema import TextLine,Set
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.support.identification.archetypeid import ArchetypeId
from openehr.rm.support.identification.hierobjectid import HierObjectId
from openehr.am.archetype.constraintmodel.ccomplexobject import CComplexObject
from openehr.am.archetype.ontology.archetypeontology import ArchetypeOntology
from openehr.rm.common.resource.interfaces.authoredresource import IAuthoredResource

_ = MessageFactory('oship')


class IArchetype(IAuthoredResource):
    """
    Archetype equivalent to ARCHETYPED class in Common reference model.
    Defines semantics of identfication, lifecycle, versioning, composition 
    and specialisation.
    """
    
    adlVersion = TextLine(
        title = _("adlVersion"),
        description = _("""ADL version if archteype was read in from 
                        an ADL sharable archetype."""),
        required = False,
        default = None
    )
    
    archetypeId=ArchetypeId('',
        title=_("Archetype Id"),
        description=_("Multi-axial identifier of this archetype."),
        required=True,
    )
    
    uid=HierObjectId(
        title=_("UID"),
        description=_("OID of this archetype."),
        required=False,
    )
    
    concept=TextLine(
        title=_("Concept"),
        description=_("The normative meaning of archetype as a whole."),
        required=True,
    )
    
    parentArchetypeId=ArchetypeId('',
        title=_("Parent Archetype Id"),
        description=_("Identifier of the specialsation parent of this archetype."),
        required=False,
    )
    
    definition=CComplexObject(
        title=_("Definition"),
        description=_("Root node of this archetype."),
        required=True,
    )

    ontology=ArchetypeOntology('','','','','','',
        title=_("Ontology"),
        description=_("The ontology of the archetype"),
        required=True,
    )

    invariants=Set(
        title=_("Invariants"),
        description=_("FOPL invariant statements"),
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
