# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'


from zope.interface import implements,classProvides 
from zope.i18nmessageid.message import MessageFactory 

from openehrcodesetidentifiers import IOpenehrCodeSetIdentifiers
from openehrterminologygroupidentifiers import IOpenehrTerminologyGroupIndentifiers

_ = MessageFactory('oship')


class ITerminologyService(IOpenehrCodeSetIdentifiers, IOpenehrTerminologyGroupIndentifiers):
    u"""
    Defines an object providing proxy access to a terminology service.
    """
                      
    def terminology(name):
        u"""
        Return an interface to the terminology named name. Allowable names include
        "openehr","centc251",any name from are taken from the US NLM UMLS meta-data 
        list at http://www.nlm.nih.gov/research/umls/metaa1.html
        
        name != None and name is a valid TerminologyAccess.        
        """
    def codeSet(name):
        u"""
        Return an interface to the code_set identified by the external identifier name (e.g. "ISO_639-1").
        
        name != None and hasCodeSet == True.
        """
        
    def codeSetForId(id):
        u""" 
        Return an interface to the code_set identified internally in openEHR by id.

        id != None and validCodeSetId(id) == True
        """
        
    def hasTerminology(name):
        u"""
        True if terminology named name known by this service. Allowable names include:
        "openehr","centc251",any name from are taken from the US NLM UMLS meta-data list
        at http://www.nlm.nih.gov/research/umls/metaa1.html
        
        name != None and name != ''
        """
        
    def hasCodeSet(name): 
        u"""
        True if codeSet linked to internal name (e.g. "languages") is available.

        name != None and name != ''
        """
        
    def terminologyIdentifiers():
        u"""
        Set (LIST) of all terminology identifiers known in the terminology service. Values from
        the US NLM UMLS meta-data list at http://www.nlm.nih.gov/research/umls/metaa1.html
        """
        
    def codeSetIdentifiers():
        u"""
        Set of all code set identifiers known in the terminology service.
        """
        
        
    def openehrCodeSets():
        u"""
        Set of all code sets identifiers for which there is an internal openEHR name;
        returned as a Hash of ids keyed by internal name.
        """
