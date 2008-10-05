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

    def __init__(self, atidstr):
        """
        atidstr is a unicode str of the full archetype ID from the ADL
        Maybe we shoudl do a regex on the full name too?        
        """
        self.__name__ = atidstr
        
        atid = atidstr.split(u'.')
        
        self.qualifiedRmEntity = atid[0]
        self.rmOriginator = atid[0].split(u'-')[0]
        self.domainConcept = atid[1]
        self.rmEntity = atid[0].split(u'-')[2]
        self.versionId = atid[2]
        self.rmName = u'openehr'  # we only use openehr archetypes
        is_spec = atid[1].find(u'-')
        if  is_spec > 0:
            self.specialisation = atid[1][is_spec+1:len(atid[1])]
        else:
            self.specialisation = u''
        
        


