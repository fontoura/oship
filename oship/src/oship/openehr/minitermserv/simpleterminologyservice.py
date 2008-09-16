# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

This is a simple in-memory implementation of a Terminology Access.

"""

__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.interface import implements
from openehr.minitermserv.xmlterminologysource import XmlTerminologySource
from openehr.minitermserv.simplecodesetaccess import SimpleCodeSetAccess
from openehr.minitermserv.simpleterminologyaccess import SimpleTerminologyAccess
from openehr.rm.support.terminology.terminologyservice import TerminologyService
from openehr.rm.datatypes.text.codephrase import CodePhrase

_ = MessageFactory('oship')

class SimpleTerminologyService():
    """
    Defines an object providing proxy access to a terminology service.
    """

    implements(TerminologyService)

    __filename = '/openehr_terminology_en.xml'

    def terminology(name):
        u"""
        Return an interface to the terminology named name. Allowable names include
        "openehr","centc251",any name from are taken from the US NLM UMLS meta-data 
        list at http://www.nlm.nih.gov/research/umls/metaa1.html

        name != None and name is a valid TerminologyAccess.        
        """
        try:
            return self.terminology[name]
        except KeyError:
            return None

    def codeSet(name):
        u"""
        Return an interface to the code_set identified by the external identifier name (e.g. "ISO_639-1").

        name != None and hasCodeSet == True.
        """
        try:
            return self.codeSets[name]
        except KeyError:
            return None

    def codeSetForId(id):
        u""" 
        Return an interface to the code_set identified internally in openEHR by id.

        id != None and validCodeSetId(id) == True
        """
        try:
            name = codeSetInternalIdToExternalName[id]
            return self.codeSets[name]
        except KeyError:
            return None

    def hasTerminology(name):
        u"""
        True if terminology named name known by this service. Allowable names include:
        "openehr","centc251",any name from are taken from the US NLM UMLS meta-data list
        at http://www.nlm.nih.gov/research/umls/metaa1.html

        name != None and name != ''
        """		
            return name is in [k for k,v in self.terminologies.items()]

    def hasCodeSet(name): 
        u"""
        True if codeSet linked to internal name (e.g. "languages") is available.

        name != None and name != ''
        """
            return name is in [k for k,v in self.codeSetInternalIdToExternalName.items()]

    def terminologyIdentifiers():
        u"""
        Set (LIST) of all terminology identifiers known in the terminology service. Values from
        the US NLM UMLS meta-data list at http://www.nlm.nih.gov/research/umls/metaa1.html
        """
        return [k for k,v in self.terminologies.items()]

    def codeSetIdentifiers():
        u"""
        Set of all code set identifiers known in the terminology service.
        """
        return [k for k,v in self.codeSets.items()]        

    def openehrCodeSets():
        u"""
        Set of all code sets identifiers for which there is an internal openEHR name;
        returned as a Hash of ids keyed by internal name.
        """
        return self.codeSetInternalIdToExternalName

    def getInstance(x = SimpleTerminologyService):
        try:
            single = x()
        except SimpleTerminologyService, s:
            single = s
        return single

    def __init__(self):
        terminologySource = XMLTerminologySource(filename)		
        __loadTerminologies(terminologySource)
        __loadCodeSets(terminologySource)			

    def __loadTerminologies(source):
        terminologies = {}		
        terminology = SimpleTerminologyAccess('openehr');
        groups = source.groupList
        for group in groups:
            codes = []
            names = {}
            names["en"] = group.name
            for concept in group.concepts:
                codes.append(concept.id)
                terminology.addRubric("en", concept.id, concept.rubric)
            terminology.addGroup(group.name, codes, names);	
        terminologies['openehr'] = terminology

    def __loadCodeSets(self, source):
        self.codeSets = {}
        self.codeSetInternalIdToExternalName = {}
        for codeSet in source.codeSetList:
            simpleCodeSet = SimpleCodeSetAccess(codeset.externalId, codeset.codes)
            self.codeSets[codeset.externalId] = codeSetAccess)
            self.codeSetInternalIdToExternalName[codeset.openehrId] = codeset.externalId)

