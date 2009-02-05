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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Fabricio Ferracioli <fabricioferracioli@gmail.com>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.identification.objectid import ObjectId
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef
from oship.openehr.rm.support.identification.interfaces.archetypeid import IArchetypeId
import re

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

    AXIS_SEPARATOR = u'.'
    SECTION_SEPARATOR = u'-'   
    NAME_PATTERN = r"[a-zA-Z][a-zA-Z0-9()_/%$#&]*"
    VERSION_PATTERN = r"[a-zA-Z0-9]+"
    
    def __init__(self, atidstr):
        """
        atidstr is a unicode str of the full archetype ID from the ADL       
        """
        self.value = atidstr
        tokens = atidstr.split(self.AXIS_SEPARATOR)
        if len(tokens) != 3:
            raise ValueError, 'bad format, wrong number of sections'
        self.__qualifiedRmEntity = tokens[0]
 
        self.__domainConcept = tokens[1]
        self.__version = tokens[2]
        self.__validateVersionId(self.__version)
        
        tokens = self.__qualifiedRmEntity.split(self.SECTION_SEPARATOR)
        if len(tokens) != 3:
            raise ValueError, 'bad format, wrong number of sections in ' + self.value
        self.__rmOriginator = tokens[0]
        self.__validateName(self.__rmOriginator, 'rm_originator')
        self.__rmName = tokens[1]
        self.__validateName(self.__rmName, 'rm_name')
        self.__rmEntity = tokens[2]
        self.__validateName(self.__rmEntity, 'rm_entity')

        tokens = self.__domainConcept.split(self.SECTION_SEPARATOR)
        if len(tokens) < 1:
            raise ValueError, 'bad format, too few sections for domainConcept in ' + self.value
        self.__conceptName = tokens[0]    
        self.__validateName(self.__conceptName, 'concept_name')
        if len(tokens) > 1:
            self.__specialisation = tokens[-1]
            self.__validateName(self.__specialisation, 'specialisation')
        else:
            self.__specialisation = None
 
    def __validateName(self, value, label):
        match = re.compile(self.NAME_PATTERN).match(value)
        if (match is None) or (match.end() < len(value)):
            raise ValueError, 'wrong format of ' + label + ': ' + value

    def __validateVersionId(self, version):
        match = re.compile(self.VERSION_PATTERN).match(version)
        if (match is None) or (match.end() < len(version)):
            raise ValueError, 'wrong format of versionId: ' + version
 
    def qualifiedRmEntity(self):
        u"""
        Globally qualified reference model entity, e.g. "openehr-composition-OBSERVATION".
        """
        return self.__qualifiedRmEntity

    def domainConcept(self):
        u"""
        Name of the concept represented by this archetype, including specialisation, 
        e.g. "biochemistry_result-cholesterol".
        """
        return self.__domainConcept

    def rmOriginator(self):
        u"""
        Organisation originating the reference model on which this archetype is based, 
        e.g. "openehr", "cen", "hl7".
        """
        return self.__rmOriginator

    def rmName(self):
        u"""
        Name of the reference model, e.g. "rim","ehr_rm", "en13606".
        """
        return self.__rmName

    def rmEntity(self):
        u"""
        Name of the ontological level within the reference model to which this archetype is 
        targeted, e.g. for openEHR, "folder","composition", "section", "entry".
        """
        return self.__rmEntity

    def specialisation(self): 
        u"""
        Name of specialisation of concept, if this archetype is a specialisation of another 
        archetype, e.g. "cholesterol".
        """
        return self.__specialisation;
    
    def versionId(self):
        u"""
        Version of this archetype.
        """
        return self.__version
      


