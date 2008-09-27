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
from openehr.minitermserv.group import Group
from openehr.minitermserv.concept import Concept
from openehr.minitermserv.codeset import CodeSet
from xml.dom import minidom

_ = MessageFactory('oship')

class XMLTerminologySource():
    """
    Defines an object providing proxy access to a terminology service.
    """

    def __init__(self, filename):
        self.codeSetList = []
        self.groupList = []
        self.__loadTerminologyFromXML(filename)
            
    def __loadTerminologyFromXML(self, filename):	
        try:
            input = open(filename) 
            try:
                encoding = sys.getdefaultencoding()
                doc = minidom.parse(input)
                root = doc.firstChild
                codesets = root.getElementsByTagName('codeset')

                for element in codesets:
                    self.codeSetList.append(self.__loadCodeSet(element))

                groups = root.getElementsByTagName('group')
                for element in groups:
                    self.groupList.append(self.__loadGroup(element))       
            finally:
                input.close()
        except (IOError, OSError):
            raise IOError('file not found')
 
    def __loadCodeSet(self, element):
        """
                Loads a code set from XML element
        """
        issuer = element.attributes['issuer']
        openehrId = element.attributes['openehr_id']
        externalId = element.attributes['external_id']
        codeset = CodeSet(issuer.value, openehrId.value , externalId.value)
        children = element.getElementsByTagName('code')
        for code in children:
            codeset.addCode(code.attributes['value'].value)
        return codeset;

    def __loadGroup(self, element):
        """
                Loads a concept group from XML element
        """
        group = Group(element.attributes['name'].value)
        children = element.getElementsByTagName('concept');
        for item in children:
            group.addConcept(Concept(item.attributes['id'].value, item.attributes['rubric'].value))
        return group
