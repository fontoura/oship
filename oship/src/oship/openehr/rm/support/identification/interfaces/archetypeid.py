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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.identification.interfaces.objectid import IObjectId

_ = MessageFactory('oship')


class IArchetypeId(IObjectId):
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

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        default=_(u""),
        required=True)
    
    def valueExists():
        u"""        
        value != None and then not value != ''
        """
    
    
    def qualifiedRmEntity():
        u"""
        Globally qualified reference model entity, e.g. "openehr-composition-OBSERVATION".
        """
            
    def domainConcept():
        u"""
        Name of the concept represented by this archetype, including specialisation, 
        e.g. "biochemistry_result-cholesterol".
        """
    
    def rmOriginator():
        u"""
        Organisation originating the reference model on which this archetype is based, 
        e.g. "openehr", "cen", "hl7".
        """
    
    def rmName():
        u"""
        Name of the reference model, e.g. "rim","ehr_rm", "en13606".
        """
    
    def rmEntity():
        u"""
        Name of the ontological level within the reference model to which this archetype is 
        targeted, e.g. for openEHR, "folder","composition", "section", "entry".
        """
    
    def specialization():
        u"""
        Name of specialisation of concept, if this archetype is a specialisation of another 
        archetype, e.g. "cholesterol".
        """
        
    def versionId():
        u"""
        Version of this archetype.
        """
        
    def qualifiedRmEntityValid():
        u""" qualifiedRmEntity != None and qualifiedRmEntity != '' """

    def domainConceptValid():
        u""" domainConcept != None and domainConcept != ''  """

    def rmOriginatorValid():
        u""" rmOriginator != None and rmOriginator != '' """

    def rmNameValid():
        u""" rmName != None and rmName != '' """
        
    
    def rmEntityValid():
        u""" rmEntity != None and rmEntity != '' """
          
    def specialisationValid():
        u""" specialisation != None and specialisation != '' """
          
    def versionIdValid():
        u""" versionId != None and versionId != '' """

