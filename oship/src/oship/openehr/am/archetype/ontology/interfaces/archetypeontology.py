# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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
from zope.schema import Int,Set,List
from zope.interface import Interface

from openehr.am.archetype.archetype import Archetype

_ = MessageFactory('oship')

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
        