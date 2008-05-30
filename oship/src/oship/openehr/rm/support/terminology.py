# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Implementation for the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__version__ = '1.0.1a1'
__contributors__ = ''


from zope.interface import implements
from zope.schema import Text, TextLine, Field


class TerminologyService(OpenehrCodeSetIdentifiers,OpenehrTerminologyGroupIndentifiers):
    """
    Defines an object providing proxy access to a terminology service.
    """
    
                     
    def terminology(name):
        u"""
        Return an interface to the terminology named name. Allowable names include
        “openehr”,“centc251”,any name from are taken from the US NLM UMLS meta-data 
        list at http://www.nlm.nih.gov/research/umls/metaa1.html
        
        name != None and name is a valid TerminologyAccess.        
        """
        
    def codeSet(name):
        u"""
        Return an interface to the code_set identified by the external identifier name (e.g. “ISO_639-1”).
        
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
        “openehr”,“centc251”,any name from are taken from the US NLM UMLS meta-data list
        at http://www.nlm.nih.gov/research/umls/metaa1.html
        
        name != None and name != ''
        """
        
    def hasCodeSet(name): 
        u"""
        True if codeSet linked to internal name (e.g. “languages”) is available.

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

class TerminologyAccess(Field):
    """
    Defines an object providing proxy access to a terminology.
    """
    implements(ITerminologyAccess)

    def __init__(self,id):
        self.id=id
        
    def allCodes():
        u""" Return all codes known in this terminology """
        
    def codesForGroupId(group_id):
        u"""
        Return all codes under grouper ‘group_id’ from this terminology
        """

    def hasCodeForGroupId(group_id, a_code):
        u"""
        True if ‘a_code’ is known in group ‘group_id’ in the openEHR terminology.
        """

    def codesForGroupName(name, lang):
        u"""
        Return all codes under grouper whose name in ‘lang’ is ‘name’ from this terminology
        """

    def rubricForCode(code, lang):
        u"""
        Return all rubric of code ‘code’ in language ‘lang’.
        """

    def idExists():
        u""" True if id != None and id != '' """
        
class CodeSetAccess(Field):
    """
    Defines an object providing proxy access to a code_set.
    """

    implements(ICodeSetAccess)

    def __init__(self,id):
        self.id=id
    
    def allCodes():
        u""" Return all codes known in this code set """
        
    def hasLang(a_lang):
        u""" True if code set knows about ‘a_lang’ """
        
    def hasCode(a_code):
        u""" True if code set knows about ‘a_code’ """
        
    def idValid():
        u""" True if id != None and id != ''  """
        
class OpenehrTerminologyGroupIndentifiers(Field):
    """
    List of identifiers for groups in the openEHR terminology.
    """
    
    terminologyId = TextLine(
        title=u"Terminology ID",
        description=u"Name of openEHR’s own terminology",
        default=u"openehr",
        readonly=True,
        )
        
    groupIdAuditChangeType = TextLine(
        title=u"Group ID Audit Change",
        default=u"audit change type",
        readonly=True,
        )
    
    groupIdAttestationReason = TextLine(
        title=u"Group ID Atesstation Reason",
        default=u"attestation reason",
        readoly=True,
        )
    
    groupIdCompositionCategory = TextLine(
        title=u"Group ID Composition Category",
        default=u"composition category",
        readonly=True,
        )
        
    groupIdEventMathFunction = TextLine(
        title=u"Group Id Event Math Function",
        default=u"event math function",
        readonly=True,
        )
        
    groupIdIsmStates = TextLine(
        title=u"Group ID ISM States",
        default=u"ISM states",
        readonly=True,
        )
    
    groupIdIsmTransitions = TextLine(
        title=u"Group ID ISM Transitions",
        default=u"ISM transitions",
        readonly=True,
        )
    
    groupIdNullFlavours = TextLine(
        title=u"Group ID Null Flavours",
        default=u"null flavours",
        readonly=True,
        )
    
    groupIdMeasurableProperties = TextLine(
        title=u"Group ID Measurable Properties",
        default=u"measurable properties",
        readonly=True,
        )
        
        
    groupIdParticipationFunction = TextLine(
        title=u"Group ID Participation Function",
        default=u"participation function",
        readonly=True,
        )
    
    groupIdParticipationMode = TextLine(
        title=u"Group ID Participation Mode",
        default=u"participation mode",
        readonly=True,
        )
    
    groupIdRelatedPartyRelationship = TextLine(
        title=u"Group Id Related Party Relationship",
        default=u"related party relationship",
        readonly=True,
        )
        
    groupIdSetting = TextLine(
        title=u"Group ID Setting",
        default=u"setting",
        readonly=True,
        )
        
    groupIdTermMappingPurpose = TextLine(
        title=u"Group Id Term Mapping Purpose",
        default=u"term mapping purpose",
        readonly=True,
        )
        
        
    groupIdVersionLifecycleState = TextLine(
        title=u"Group Id Version Lifecycle State",
        default=u"version lifecycle state",
        readonly=True,
        )
    
    
    def validTerminologyGroupId(an_id):
        u"""
        Validity function to test if an identifier is in the set defined by this class.
        """
        
class OpenehrCodeSetIdentifiers(Field):
    u""" List of identifiers for code sets in the openEHR terminology. """
        
    
    codeSetIdCharacterSets = TextLine(
        title=u"Code Set Id Character Sets",
        default=u"character sets",
        readonly=True,
        )
        
    codeSetIdCompressionAlgorithms = TextLine(
        title=u"Code Set Id Compression Algorithms",
        default=u"compression algorithms",
        readonly=True,
        )
    
    codeSetIdCountries = TextLine(
        title=u"Code Set Id Countries",
        default=u"countries",
        readonly=True,
        )
    
    codeSetIdIntegrityCheckAlgorithms = TextLine(
        title=u"Code Set Id Integrity Check Algorithms",
        default=u"integrity check algorithms",
        readonly=True,
        )
    
    codeSetIdLanguages = TextLine(
        title=u"Code Set Id Languages",
        default=u"languages",
        readonly=True,
        )
        
    codeSetIdMediaTypes = TextLine(
        title=u"Code Set Id Media Types",
        default=u"media types",
        readonly=True,
        )
        
    codeSetIdNormalStatuses = TextLine(
        title=u"Code Set Id Normal Statuses",
        default=u"normal statuses",
        readonly=True,
        )


    def validCodeSetId(an_id):
        u"""
        Boolean Validity function to test if an identifier is in 
        the set defined by this class.
        """
        
