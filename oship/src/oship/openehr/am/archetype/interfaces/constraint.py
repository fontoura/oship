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

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

class IArchetypeConstraint(IContent):
    """
    Archetype equivalent to Locatable class in the Common package of the reference model.
    """
    
    isSubsetOf=Bool(
        title=_("Subset"),
        description=_("True if constraints are narrower than this node."),
        required=False,
    )

    isValid=Bool(
        title=_("Valid"),
        description=_("True if this node and sub-nodes are valid for its type."),
        required=False,
    )

    def path():
        """
        Return a string containt the path of this node relative to the archetype root.
        """
        
    def hasPath(aPath):
        """
        Return True if the relative path (aPath) exists at this node.
        """
        
class ICAttribute(Interface):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    rmAttributeName=TextLine(
        title=_("RM Attribute Name"),
        description=_("Reference model attribute within the enclosed type representedby a CObject."),
        required=True,
    )
    
    existence=Interval(
        title=_("Existence"),
        description=_("Indicates whether the target object exists or not."),
        required=True,
    )

    children=List(
        title=_("Children"),
        description=_("Child constraint nodes."),
        required=False,
    )

class ICSingleAttribute(Interface):
    """
    Concrete model of constraint on a single valued attribute.
    """
    
    alternatives=List(
        title=_("Alternatives"),
        description=_("A list of alternative constraints for the single child of this attribute."),
        required=False,
    )

class ICMultipleAttribute(Interface):
    """
    Abstract model of constraint on any kind of attribute node.
    """
    
    cardinality=Cardinality(
        title=_("Cardinality"),
        description=_("Cardinality of this attribute constraint."),
        required=True,
    )

    def members(cobj):
        """
        List of constraints representing members of the container value of this attribute.
        """
        
class ICardinality(Interface):
    """
    Expresses constraints on the cardinality of container classes.
    """
    
    isOrdered=Bool(
        title=_("Ordered"),
        description=_("True if members are ordered."),
        required=True,
    )

    isUnique=Bool(
        title=_("Unique"),
        description=_("True if members are unique."),
        required=True,
    )

    interval=Interval(
        title=_("Interval"),
        description=_("Interval of this cardinality."),
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

class ICDefinedObject(ICObject):
    """
    Abstract parent of CObject subtypes that are defined by this value.
    """
    
    assumedValue=Field(
        title=_("Assumed Value"),
        description=_("Value to be assumed if none sent in data."),
        required=False,
    )

    def hasAssumedValue():
        """
        Return True if assumedValue is not equal to None.
        """
        
class ICComplexObject(ICDefinedObject):
    """
    Constraint on complex objects.
    """
    
    attributes=Set(
        title=_("Attributes"),
        description=_("List of constraints on attributes of the reference model."),
        required=False,
    )

    anyAllowed=Bool(
        title=_("Any Allowed"),
        description=_("True if any value of the reference model is allowed."),
        required=True,
    )

class ICPrimitiveObject(ICDefinedObject):
    """
    Constraint on a primitive object.
    """
    
    anyAllowed=Bool(
        title=_("Any Allowed"),
        description=_("True if any value of the type being constrained is allowed."),
        required=True,
    )
    
    item=CPrimitive(
        title=_("Item"),
        description=_("Object actually defining the constraint."),
        required=False,
    )
   
class ICDomainType(ICDefinedObject):
    """
    Abstract parent of domain specific constrainer types.
    """
    
    standardEquivalent=CComplexObject(
        title=_("Standard Equivalent"),
        description=_("Standard form of constraint."),
        required=True,
    )
    
    
class ICReferenceObject(ICObject):
    """
    Abstract parent of CObject subtypes that are defined by reference.
    """
    
class IArchetypeSlot(ICReferenceObject):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    includes=Set(
        title=_("Includes"),
        description=_("List of constraints defining other archetypes that can occur here."),
        required=False,
    )

    excludes=Set(
        title=_("Excludes"),
        description=_("List of constraints defining archetypes that cannot be include here."),
        required=False,
    )

    
class IArchetypeInternalRef(ICReferenceObject):
    """
    See the AOM reference document.
    """
    
    targetPath=TextLine(
        title=_("Target Path"),
        description=_("Reference to an object node using archetype path notation."),
        required=True,
    )

    
class IConstraintRef(ICReferenceObject):
    """
    Reference to a constraint described in the same archetype.
    """
    
    reference=TextLine(
        title=_("Reference"),
        description=_("Reference to a constraint in the archetype ontology."),
        required=True,
    )
    
    
    
    