# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the implementations for the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from openehr.am.archetype.interfaces.constraint import *

class ArchetypeConstraint(Content):
    """
    Archetype equivalent to Locatable class in the Common package of the reference model.
    """
    
    implements(IArchetypeConstraint)
    

    def path():
        """
        Return a string containt the path of this node relative to the archetype root.
        """
        
    def hasPath(aPath):
        """
        Return True if the relative path (aPath) exists at this node.
        """
        
class CAttribute(Field):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    implements(ICAttribute)
    

class CSingleAttribute(Field):
    """
    Concrete model of constraint on a single valued attribute.
    """
    
    implements(ICSingleAttribute)
    

class CMultipleAttribute(Field):
    """
    Abstract model of constraint on any kind of attribute node.
    """
    
    implements(ICMultipleAttribute)
    
    def members(cobj):
        """
        List of constraints representing members of the container value of this attribute.
        """
        
class Cardinality(Field):
    """
    Expresses constraints on the cardinality of container classes.
    """
    
    implements(ICardinality)
    
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
        

class CObject(Field):
    """
    Abstract model of constraint on any kind of object node.
    """
    
    implements(ICObject)
    

class CDefinedObject(CObject):
    """
    Abstract parent of CObject subtypes that are defined by this value.
    """
    
    implements(ICDefinedObject)
    
    def hasAssumedValue():
        """
        Return True if assumedValue is not equal to None.
        """
        
class CComplexObject(CDefinedObject):
    """
    Constraint on complex objects.
    """
    
    implements(ICComplexObject)
    

class CPrimitiveObject(CDefinedObject):
    """
    Constraint on a primitive object.
    """
    
    implements(ICPrimitiveObject)
    

   
class CDomainType(CDefinedObject):
    """
    Abstract parent of domain specific constrainer types.
    """
    
    implements(ICDomainType)
        
    
class CReferenceObject(CObject):
    """
    Abstract parent of CObject subtypes that are defined by reference.
    """
    
    implements(ICReferenceObject)
    
    
class ArchetypeSlot(CReferenceObject):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    implements(IArchetypeSlot)
    
    
    
class ArchetypeInternalRef(CReferenceObject):
    """
    See the AOM reference document.
    """
    
    implements(IArchetypeInternalRef)
    
    
class ConstraintRef(CReferenceObject):
    """
    Reference to a constraint described in the same archetype.
    """
    
    implements(IConstraintRef)
    
  
    
    
    