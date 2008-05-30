# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
The archetypes implementation. 
From the archetype object model specification Rev 2.0.1
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.i18nmessageid.message import MessageFactory
from zope.interface import implements
from openehr.am.archetype.interfaces.archetype import *

_ = MessageFactory('oship')


class Archetype(AuthoredResource):
    """
    Archetype equivalent to ARCHETYPED class in Common reference model.
    Defines semantics of identfication, lifecycle, versioning, composition 
    and specialisation.
    """
    
    implements(IArchetype)
    
    
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
        
class ValidityKind(Field):
    """
    An enumeration of three values which may commonly occur in constrint models.
    Use to indicate the validity of date/Time fields etc.
    
    """
    
    constants={'mandatory':1001,'optional':1002,'disallowed':1003}

    def validValidity():
        """
        Test if value is == to one of the constants.
        """
        

        
    

    