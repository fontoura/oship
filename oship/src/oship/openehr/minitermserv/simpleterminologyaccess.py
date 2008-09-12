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
from zope.schema import Object
from openehr.rm.support.terminology.terminologyaccess import TerminologyAccess
from openehr.rm.datatypes.text.codephrase import CodePhrase

_ = MessageFactory('oship')

class SimpleTerminologyAccess(Object):
    """
    Simple in-memory implementation of a terminology access
    """

        implements(TerminologyAccess)

        def __init__(self, id)
            u"""
			groups is a dictionary of groups indexed by group id
			codeRubrics is a dictionary where the key is a language and the value is a dictionary of concept.id to concept.rubric
			groupLangNameToId is a dictionary where the key is a languagen and the value is a dictionary of group.name to groupId
				Use group.name in english as a groupId
		"""
            self.id = id;
            self.groups = {}
            self.groupLangNameToId = {}
            self.codeRubrics = {}


    def allCodes(self):
        u""" Return all codes known in this terminology """
            allCodes = []
            for k,v in groups.items():
                allCodes.extend(v)
            return allCodes      

    def codesForGroupId(self, group_id):
        u"""
        Return all codes under grouper 'group_id' from this terminology
        """
            try:
                codes = self.groups[group_id)
                return codes
                except KeyError:
                    return None

    def hasCodeForGroupId(self, group_id, a_code):
        u"""
        True if 'a_code' is known in group 'group_id' in the openEHR terminology.
        """
            try:
                group = self.groups[group_id]
                return a_code is in group
            except KeyError:
                return False

    def codesForGroupName(self, name, lang):
        u"""
        Return all codes under grouper whose name in 'lang' is 'name' from this terminology
        """
            try
                map = groupLangNameToId[lang]
                try:
                    return self.groups[map[name]]
                except KeyError:
                    return None
            except KeyError:
                return None

    def rubricForCode(self, code, lang):
        u"""
        Return all rubric of code 'code' in language 'lang'.
        """
            try:
                map = self.codeRubrics[lang]
                try:
                    return map[code]
                except KeyError:
                    return None
            except KeyError:
                return None

        def addGroup(self, groupId, codes, names):
        u"""
		 Adds a group of codes with language dependent names
	     param groupId	
	     param codes  
	     param names
        """
            group = []
                for c in codes:
                    code = CodePhrase(self.id, c)
                    group.append(code)			
                self.groups[groupId] = group
                for lang, name in names.items():
                    try:
                        nameToId = groupLangNameToId[lang]
                    except KeyError:
                        nameToId = {}
                    nameToId[name] = groupId
                    groupLangNameToId[lang] = nameToId

        def addRubric(self, lang, code, rubric):
        u"""
		 Adds a group of codes with language dependent names
	     param lang	
	     param code  
	     param rubric
        """
            try:
                map = self.codeRubrics[lang]
            except KeyError:
                map = {}
                self.codeRubrics[lang] = map
            map[code] = rubric
