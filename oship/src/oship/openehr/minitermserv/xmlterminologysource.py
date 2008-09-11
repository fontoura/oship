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
from xml.minidom import minidom
import sys

_ = MessageFactory('oship')

class XMLTerminologySource():
    """
    Defines an object providing proxy access to a terminology service.
    """
    
	def __init__(self, filename)
		try:
			self.codeSetList = []
			self.groupList = []
			__loadTerminologyFromXML(filename)
		except (IOError, OSError):
			raise IOError('file not found')

	
	def __loadTerminologyFromXML(self, filename):	
		try:
			sys.setdefaultencoding('utf-8')
			input = open(filename) 
			doc = minidom.parse(input)
			root = doc.firstChild()
			codesets = root.getElementsByTagName('codeset')
			
			for element in codesets:
				self.codeSetList.append(__loadCodeSet(element))
			
			groups = root.getElementsByTagName('group')
			for group in codesets:
				self.groupList.append(loadGroup(element))
		finally:
			input.close();
	
	def __loadCodeSet(element):
	"""
		Loads a code set from XML element
	"""
		codeset = CodeSet(element.attributes['openehr_id'], element.attributes['external_id'], element.attributes['code'])
		children = element.getElementsByTagName('code')
		for code in children:
			codeset.append(code.attributes['value'])
		return codeset;
	
	def __loadGroup(element):
	"""
		Loads a concept group from XML element
	"""
		group = Group(element.attributes['name'])
		children = element.getElementsByTagName('concept');
		for item in children:
			group.addConcept(Concept(item.attributes['id'], item.attributes['rubric']))
		return group
	