# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Fabricio Ferracioli <fabricioferracioli@gmail.com>'


from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from objectid import ObjectId
from interfaces.archetypeid import IArchetypeId

_ = MessageFactory('oship')

class ArchetypeId(ObjectId):
    u"""
    Identifier for archetypes. Lexical form:
    rm_originator '-' rm_name '-' rm_entity '.' concept_name { '-' specialisation }* '.v' number

    Archetype identifiers are "multi-axial", meaning that each identifier instance denotes a single 
    archetype within a multi-dimensional space. In this case, the space is essentially a 
    versioned 3-dimensional space, with the dimensions being:
           
        reference model entity, i.e. target of archetype
        domain concept
        version
       
    As with any multi-axial identifier, the underlying principle of an archetype id is that all parts of the id
    must be able to be considered immutable. This means that no variable characteristic of an archetype
    (e.g. accrediting authority, which might change due to later accreditation by another authority, or may
    be multiple) can be included in its identifier. The syntax of an ARCHETYPE_ID is as follows (EBNF):

        archetype_id: qualified_rm_entity '.' domain_concept '.' version_id
        qualified_rm_entity: rm_originator '-' rm_name '-' rm_entity
        rm_originator: V_NAME
        rm_name: V_NAME
        rm_entity: V_NAME
        domain_concept: concept_name { '-' specialisation }*
        concept_name: V_NAME
        specialisation: V_NAME
        version_id: 'v' V_NUMBER
        NUMBER: [0-9]*
        NAME: [a-z][a-z0-9()/%$#&]*

    The field meanings are as follows:
       rm_originator: id of organisation originating the reference model on which this archetype is based;
       rm_name: id of the reference model on which the archetype is based;
       rm_entity: ontological level in the reference model;
       domain_concept: the domain concept name, including any specialisations;
       version_id: numeric version identifier;
       
    Examples of archetype identifiers include:
        openehr-composition-SECTION.physical_examination.v2
        openehr-composition-SECTION.physical_examination-prenatal.v1
        hl7-rim-act.progress_note.v1
        openehr-composition-OBSERVATION.progress_note-naturopathy.v2
       
    Archetypes can also be identified by other means, such as ISO oids.
    """

    implements(IArchetypeId)

    def __init__(self, value):
        self.value = value


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value != None and self.value != ''
    
    
    def qualifiedRmEntity():
        u"""
        Globally qualified reference model entity, e.g. "openehr-composition-OBSERVATION".
        """
        return value.split('.')[0]
    
    def domainConcept():
        u"""
        Name of the concept represented by this archetype, including specialisation, e.g. "biochemistry_result-cholesterol".
        """
        return value.split('.')[1]
    
    def rmOriginator():
        u"""
        Organisation originating the reference model on which this archetype is based, e.g. "openehr", "cen", "hl7".
        """
        return value.split('.')[0].split('-')[0]
    
    def rmName():
        u"""
        Name of the reference model, e.g. "rim","ehr_rm", "en13606".
        """
        return value.split('.')[0].split('-')[1]
    
    def rmEntity():
        u"""
        Name of the ontological level within the reference model to which this archetype is targeted, e.g. for openEHR, "folder","composition", "section", "entry".
        """
        return value.split('.')[0].split('-')[2]
    
    def conceptName():
        return value.split('.')[1].split('-')[0]
    
    def specialisation():
        u"""
        Name of specialisation of concept, if this archetype is a specialisation of another archetype, e.g. "cholesterol".
        """
        if (value.split('.')[1].count('-')):
            return value.split('.')[1].split('-')[1]
        return None
        
    def versionId():
        u"""
        Version of this archetype.
        """
        return value.split('.')[2]
        
    def qualifiedRmEntityValid():
        u""" qualifiedRmEntity != None and qualifiedRmEntity != '' """
        if (self.qualifiedRmEntity != None):
            return self.qualifiedRmEntity != ''
        return self.qualifiedRmEntity == None
        

    def domainConceptValid():
        u""" domainConcept != None and domainConcept != ''  """
        if (self.domainConcept != None):
            return self.domainConcept != ''
        return self.domainConcept == None

    def rmOriginatorValid():
        u""" rmOriginator != None and rmOriginator != '' """
        if (self.rmOriginator != None):
            return self.rmOriginator != ''
        return self.rmOriginator == None

    def rmNameValid():
        u""" rmName != None and rmName != '' """
        if (self.rmName != None):
            return self.rmName != ''
        return self.rmName == None
        
    
    def rmEntityValid():
        u""" rmEntity != None and rmEntity != '' """
        if (self.rmEntity != None):
            return self.rmEntity != ''
        return self.rmEntity == None
    
    def specialisationValid():
        u""" specialisation != None and specialisation != '' """
        if (self.specialisation != None):
            return self.specialisation != ''
        return self.specialisation == None
          
    def versionIdValid():
        u""" versionId != None and versionId != '' """
        if (self.versionId != None):
            return self.versionId != ''
        return self.versionId == None

