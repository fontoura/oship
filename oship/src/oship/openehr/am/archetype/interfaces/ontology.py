# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
These are the interfaces for the am.archetype.ontology package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

class IArchetypeOntology(Interface):
    """
    Local ontology of an archetype.
    """
    
    terminologiesAvailable=Set(
        title_("Terminologies"),
        description=_("List of terminologies in this ontology."),
        required=True,
    )

    specialisationDepth=Int(
        title_("Specialisation Depth"),
        description=_("Specialisation depth of this archetype."),
        required=True,
    )
    
    termCodes=List(
        title_("Term Codes"),
        description=_("List of all term codes in this archetype."),
        required=True,
    )

    constraintCodes=List(
        title_("Constraint Codes"),
        description=_("List of all constraint codes in this archetype."),
        required=True,
    )
    
    termAttributeNames=List(
        title_("Term Attribute Names"),
        description=_("List of attribute names in this archetype ontolgy."),
        required=True,
    )
    
    parentArchetype=Archetype(
        title_("Parent"),
        description=_("Archetype which owns this ontology."),
        required=True,
    )

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
        
class IArchetypeTerm(Interface):
    """
    Representation of any coded entity in the archetype ontology.
    """
    
    code=TextLine(
        title_("Code"),
        description=_("Code of this term."),
        required=True,
    )

    items=Dict(
        title_("Items"),
        description=_("Hash of keys (text,description) and corresponding values."),
        required=False,
    )
    
    def keys(set):
        """
        List of all keys used in this term.
        """
        
        


    
    