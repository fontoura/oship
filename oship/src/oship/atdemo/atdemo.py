# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

from zope.schema import Text
from persistent import Persistent
from zope.interface import Interface,implements
from zope.schema.fieldproperty import FieldProperty

class IATDemo(Interface):
    """ Just a demo"""
    
    adl_version=Text(
        title=u"ADL Version",
        required=True)
    
    archetype_id=Text(
        title=u"Archetype ID",
        required=True)
    
    concept=Text(
        title=u"Concept",
        required=True)
    
    parent_archetype_id=Text(
        title=u"Parent Archetype ID",
        required=False)
    
    definition=Text(
        title=u"Definition",
        required=True)
    
    ontology=Text(
        title=u"Ontology",
        required=True)
    
    invariants=Text(
        title=u"Invariants",
        required=False)
    
    rev=Text(
        title=u"Revision history",
        required=False)
    
    
    

class ATDemo(Persistent):
    """As a demo """
    
    implements(IATDemo)
    
    def __init__(self,adl_version,archetype_id,concept,parent_archetype_id,definition,ontology,invariants,rev):
        
        self.adl_version = adl_version
        self.archetype_id = archetype_id
        self.concept = concept
        self.parent_archetype_id = parent_archetype_id
        self.definition = definition
        self.ontology = ontology
        self.invariants = invariants
        self.rev = rev
        
    
    
       