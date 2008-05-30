# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


from zope.interface import Interface,implements
from zope.schema import Text,TextLine
from persistent import Persistent
from zope.app.container.interfaces import IContained, IContainer
from zope.app.file.interfaces import IFile 
from zope.i18nmessageid.message import MessageFactory

_ = MessageFactory("oship")

class IATDemo(IContainer):
    """
    This is a temporary interface only for the ATBldr 'archetype' class.  
    Only to be used in demo and developement work.
    """
    
    adlVersion = TextLine(
        title = _("adlVersion"),
        description = _("""ADL version if archteype was read in from 
                        an ADL sharable archetype."""),
        required = False,
        default = None
    )
    
    archetypeId=TextLine(
        title=_("Archetype Id"),
        description=_("Multi-axial identifier of this archetype."),
        required=True,
    )
    
    uid=TextLine(
        title=_("UID"),
        description=_("OID of this archetype."),
        required=False,
    )
    
    concept=TextLine(
        title=_("Concept"),
        description=_("The normative meaning of archetype as a whole."),
        required=True,
    )
    
    parentArchetypeId=TextLine(
        title=_("Parent Archetype Id"),
        description=_("Identifier of the specialsation parent of this archetype."),
        required=False,
    )
    
    definition=Text(
        title=_("Definition"),
        description=_("Root node of this archetype."),
        required=True,
    )

    ontology=Text(
        title=_("Ontology"),
        description=_("The ontology of the archetype"),
        required=True,
    )

    invariants=Text(
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


class ATDemo(Persistent):
    
    implements(IATDemo)
    
    def __init__(self,adl_version,archetype_id,concept,parent_archetype_id,definition,ontology,invariants,rev):
        self.adl_version=adl_version
        self.archetype_id=archetype_id
        self.concept=concept
        self.parent_archetype_id=parent_archetype_id
        self.definition=definition
        self.ontology=ontology
        self.invariants=invariants
        self.rev=rev
