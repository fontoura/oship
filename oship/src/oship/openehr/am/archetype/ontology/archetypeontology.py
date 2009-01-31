# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
From the am.archetype.ontology package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from zope.schema import Field

from oship.openehr.am.archetype.ontology.interfaces.archetypeontology import IArchetypeOntology

_ = MessageFactory('oship')
   
class ArchetypeOntology(object):
    """
    Local ontology of an archetype.
    """
    
    implements(IArchetypeOntology)
    
    # assign the attributes to their schema definitions
    terminologiesAvailable = FieldProperty(IArchetypeOntology['terminologiesAvailable'])
    specialisationDepth = FieldProperty(IArchetypeOntology['specialisationDepth'])
    termCodes = FieldProperty(IArchetypeOntology['termCodes'])
    constraintCodes = FieldProperty(IArchetypeOntology['constraintCodes'])
    termAttributeNames = FieldProperty(IArchetypeOntology['termAttributeNames'])
    parentArchetype = FieldProperty(IArchetypeOntology['parentArchetype'])
    
    
    
    def hasLanguage(aLang):
        """
        True if aLang is present in ontology.
        """
        
    def hasTerminology(aTermId):
        """
        True if ontology has aTermId, terminology Id.
        """
        
    def hasTermCode(tcode):
        """
        True if tcode is in termCodes.
        """
        
    def hasConstraintCode(ccode):
        """
        True if ccode is in constraintCodes.
        """
        
    def constraintDefinition(aLang,aCode):
        """
        Constraint definition for aCode expressed in aLang.
        """
        
    def termBinding(aTermId,aCode):
        """
        Return a CodePhrase for aCode in aTermId.
        """
        
    def constraintBinding(aTermId,aCode):
        """
        Return a string that describes the constraint aCode in aTermId usually in the form of a query expression.
        """
