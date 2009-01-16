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
from zope.schema import Int,Set,List,Object, TextLine, Dict, Tuple
from zope.schema.interfaces import Interface

from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef
from oship.openehr.am.archetype.ontology.interfaces.archetypeterm import IArchetypeTerm

_ = MessageFactory('oship')

class IArchetypeOntology(Interface):
    """
    Local ontology of an archetype.
    """
    
    terminologiesAvailable=List(
        title=_(u"Terminologies"),
        description=_(u"List of terminologies in this ontology."),
        required=True,
        value_type=TextLine(),
    )

    specialisationDepth=Int(
        title=_(u"Specialisation Depth"),
        description=_(u"Specialisation depth of this archetype."),
        required=True,
    )
    
    termCodes=List(
        title=_(u"Term Codes"),
        description=_(u"List of all term codes in this archetype."),
        required=True,
        value_type=TextLine(),
    )

    constraintCodes=List(
        title=_(u"Constraint Codes"),
        description=_(u"List of all constraint codes in this archetype."),
        required=True,
        value_type=TextLine(),
    )
    
    termAttributeNames=List(
        title=_(u"Term Attribute Names"),
        description=_(u"List of attribute names in this archetype ontology."),
        required=True,
        value_type=TextLine(),
    )

    parentArchetype=Object(
        schema=IObjectRef,  
        title=_(u"Parent"),
        description=_(u"Archetype which owns this ontology."),
        required=False,
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
        