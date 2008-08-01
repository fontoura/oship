# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
From the archetype object model specification Rev 2.0.1
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Fabricio Ferracioli <fabricioferracioli@gmail.com>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'


from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.common.resource.authoredresource import AuthoredResource
from oship.openehr.am.archetype.interfaces.archetype import IArchetype

_ = MessageFactory('oship')

class Archetype(AuthoredResource):
    """
    Archetype equivalent to ARCHETYPED class in Common reference model.
    Defines semantics of identfication, lifecycle, versioning, composition 
    and specialisation.
    """
    
    implements(IArchetype)
    
    def __init__(self,adlver,atid,uid,concept,paid,defin,ont,inv,olang,trans,descr,revhist,ctrld):
        AuthoredResource.__init__(self,olang,trans,descr,revhist,ctrld)
        self.adlVersion=adlver
        self.archetypeId=atid
        self.uid=uid
        self.concept=concept
        self.parentArchetypeId=paid
        self.definition=defin
        self.ontology=ont
        self.invariants=inv
        self.__name__ = atid
        #self.olang = olang
        #self.trans = trans
        #self.descr = descr
        #self.revhist = revhist
        #self.ctrld = ctrld
        
    
    def version(self):
        """
        Version string extracted from id.
        """
        return self.archetypeId.versionId(self)
    
    def previousVersion(self):
        """
        Version of predecessor if any.
        """
        return None
    
    def shortConceptName(self):
        """
        String extracted from id.
        """
        
    
    def conceptName(self, language=None):
        """
        Concept string extracted from the ontology.
        """
        return self.archetypeId.conceptName()
    
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
        
    def isSpecialised(self):
        """
        True if this archetype is a specialisation of another.
        Otherwise it returns False.
        """
        if self.archetypeId.specialisation() == None:
            return False
        return True
        
        
    def specialisationDepth():
        """
        Return ontology.specialisationDepth
        """
        return self.ontology.specialisationDepth
    
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
