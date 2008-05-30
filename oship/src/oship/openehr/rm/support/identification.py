# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

Implementation of the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__version__ = '1.0.1a1'
__contributors__ = ''

from zope.interface import implements
from zope.schema import Field,URI
from openehr.rm.support.interfaces.identification import *

class Uid(Field):
    u"""
    Abstract parent of classes representing unique identifiers which identify informa-
    tion entities in a durable way. UIDs only ever identify one IE in time or space and
    are never re-used.
    """
    
    implements(IUid)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        
        return self.value!=None and self.value!=''
            
        
class IsoOid(Uid):
    u"""
    Model of ISO's Object Identifier (oid) as defined by the standard ISO/IEC 8824 .
    Oids are formed from integers separated by dots. Each non-leaf node in an Oid
    starting from the left corresponds to an assigning authority, and identifies that
    authority's namespace, inside which the remaining part of the identifier is locally unique.
    """

    implements(IIsoOid)
    
    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        
        return self.value!=None and self.value!=''

        

class Uuid(Uid):
    u"""
    Model of the DCE Universal Unique Identifier or UUID which takes the form of
    hexadecimal integers separated by hyphens, following the pattern 8-4-4-4-12 as
    defined by the Open Group, CDE 1.1 Remote Procedure Call specification,
    Appendix A. Also known as a GUID.
    """

    implements(IUuid)
    
    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''

        

class InternetId(URI):
    u"""
    Model of a reverse internet domain, as used to uniquely identify an internet
    domain. In the form of a dot-separated string in the reverse order of a domain
    name specified by IETF RFC1034 (http://www.ietf.org/rfc/rfc1034.txt).
    """
    
    implements(IInternetId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''

        
class ObjectId(Field):
    u"""
    Ancestor (abstract) class of identifiers of informational objects. Ids may be completely
    meaningless, in which case their only job is to refer to something, or may carry
    some information to do with the identified object.
    Object ids are used inside an object to identify that object. To identify another
    object in another service, use an OBJECT_REF, or else use a UID for local objects
    identified by UID. If none of the subtypes is suitable, direct instances of this class
    may be used.
    """

    implements(IObjectId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''

class UidBasedId(ObjectId):
    u"""
    Abstract model of UID-based identifiers consisting of a root part and an optional
    extension; lexical form: root '::' extension
    """

    implements(IUidBasedId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''


    def root():
        u"""
        The identifier of the conceptual namespace in which the object exists, within 
        the identification scheme.
        Returns the part to the left of the first '::' separator, if any, or else the whole string.
        """


    def extension():
        u"""
        Optional local identifier of the object within the context of the root identifier.
        Returns the part to the right of the first '::' separator if any, or else any empty String.
        """


    def hasExtension():
        u""" True if extension != None """

        
    def rootValid():
        u""" True if root != None """
        
    def extensionValidity():
        u""" True if extension != None """
        
        
    def hasExtensionValidity():
        """ extension == '' xor hasExtension() """

       
class HierObjectId(UidBasedId):
    u"""
    Concrete type corresponding to hierarchical identifiers of the form defined by UID_BASED_ID.
    """

    implements(IHierObjectId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''

    def root():
        u"""
        The identifier of the conceptual namespace in which the object exists, within 
        the identification scheme.
        Returns the part to the left of the first '::' separator, if any, or else the whole string.
        """

    def extension():
       u"""
       Optional local identifier of the object within the context of the root identifier.
       Returns the part to the right of the first '::' separator if any, or else any empty String.
       """
       
    def hasExtension():
        u""" True if extension != None """
        
    def rootValid():
        u""" True if root != None """
        
    def extensionValidity():
        u""" True if extension != None """
        
    def hasExtensionValidity():
        u""" extension == '' xor hasExtension() """

        
class ObjectVersionId(UidBasedId):
    u"""
    Globally unique identifier for one version of a versioned object; lexical form:
    object_id '::' creating_system_id '::' version_tree_id
    
    The string form of an OBJECT_VERSION_ID stored in its value attribute consists of 
    three segments separated by double colons ("::"), i.e. (EBNF):
      
    value:      object_id '::' creating_system_id '::' version_tree_id
    object_id:  uid  (see UID below)
    creating_system_id:
    
    An example ObjectVersionId is as follows:
    F7C5C7B7-75DB-4b39-9A1E-C0BA9BFDBDEC::87284370-2D4B-4e3d-A3F3-F303D2F4F34B::2  
    """

    implements(IObjectVersionId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''

    def root():
        u"""
        The identifier of the conceptual namespace in which the object exists, within 
        the identification scheme.
        Returns the part to the left of the first '::' separator, if any, or else the whole string.
        """

    def extension():
       u"""
       Optional local identifier of the object within the context of the root identifier.
       Returns the part to the right of the first '::' separator if any, or else any empty String.
       """
       
    def hasExtension():
        u""" True if extension != None """
        
    def rootValid():
        """ True if root != None """
        
    def extensionValidity():
        u""" True if extension != None """
        
    def hasExtensionValidity():
        u""" extension == '' xor hasExtension() """


    def objectId():
        u"""
        Unique identifier for logical object of which this identifier identifies one version;
        normally the object_id will be the unique identifier of the version container contain-
        ing the version referred to by this OBJECT_VERSION_ID instance.
        """
        
    def versionTreeId():
        u"""
        Tree identifier of this version with respect to other versions in the same version tree,
        VERSION_TREE_ID as either 1 or 3 part dot-separated numbers, e.g. "1", "2.1.4".
        """
        
    def creatingSystemId():
        u"""
        Identifier of the system that created the Version corresponding to this Object version id.
        """
        
    def isBranch():
        u""" True if this version identifier represents a branch. """
        
    def objectValid():
        u""" True if objectId != None. """
        
    def versionTreeIdValid():
        u""" True if versionTreeId != None. """
        
    def creatingSystemIdValid():
        u""" True if creatingSystemId != None. """



class VersionTreeId(Field):
    u"""
    Version tree identifier for one version. Lexical form:
    trunkVersion [ '.' branchNumber '.' branchVersion ]
    """
    
    implements(IVersionTreeId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueValid(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''
        
    def trunkVersion():
        u"""
        Returns a string of the trunk version number; numbering starts at 1.     
        """
        
    def branchVersion():
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """

    def isBranch():
        u"""
        Returns True if this version identifier represents a branch,
        i.e. has branchNumber and branchVersion parts.
        """
    
    def isFirst():
        u"""
        True if this version identifier corresponds to the
        first version, i.e. trunkVersion == "1"
        """
        
    def trunkVersionValid():
        u"""
        trunkVersion != None and isinstance(trunkVersion, int) and trunkVersion >= 1
        """

    def branchNumberValid():
        """
        branchNumber != None and isinstance(branchNumber, int) and branchNumber >= 1
        """
    
    def branchVersionValid():
        u"""
        branchVersion != None and isinstance(branchVersion, int) and branchVersion >= 1
        """
        
    def branchValidity():
        u"""
        (branchNumber == None and branchVersion == None ) xor
        (branchNumber != None and branchVersion != None )
        """
        
    def isBranchValidity():
        u""" isBranch xor (branchNumber == None) """
        
    def isFirstValidity():
        u""" not isFirst xor trunkVersion == "1" """


class ArchetypeId(ObjectId):
    u"""
    Identifier for archetypes. Lexical form:
    rm_originator '-' rm_name '-' rm_entity '.' concept_name { '-' specialisation }* '.v' number

    Archetype identifiers are "multi-axial", meaning that each identifier instance denotes a single 
    archetype within a multi-dimensional space. In this case, the space is essentially a 
    versioned 3-dimensional space, with the dimensions being:
           
      •  reference model entity, i.e. target of archetype
      •  domain concept
      •  version
       
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
       • openehr-composition-SECTION.physical_examination.v2
       • openehr-composition-SECTION.physical_examination-prenatal.v1
       • hl7-rim-act.progress_note.v1
       • openehr-composition-OBSERVATION.progress_note-naturopathy.v2
       
    Archetypes can also be identified by other means, such as ISO oids.
    """

    implements(IArchetypeId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''
    
    
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

        
        
class TemplateId(ObjectId):
    u""" Identifier for templates. Lexical form to be determined. """
    
    implements(ITemplateId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''
    
class TerminologyId(ObjectId):
    u"""
    Identifier for terminologies such accessed via a terminology query service. In this
    class, the value attribute identifies the Terminology in the terminology service,
    e.g. "SNOMED-CT". A terminology is assumed to be in a particular language,
    which must be explicitly specified.
    
    The value if the id attribute is the precise terminology id identifier, including
    actual release (i.e. actual "version"), local modifications etc; e.g. "ICPC2".
    Lexical form: name [ '(' version ')' ]
    """

    implements(ITerminologyId)

    def __init__(self, value,**kwargs):
        self.value = value
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''

    def name():
        u"""
        Return the terminology id (which includes the "version" in some cases). 
        Distinct names correspond to distinct (i.e. non-compatible) terminologies.
        Thus the names "ICD10AM" and "ICD10" refer to distinct terminologies.
        """
        
    def versionId():
        u""" Version of this terminology, if versioning supported, else the empty string."""
        
    
    def nameValid():
        u""" name != None and name != '' """

    def versionIdValid():
        u""" versionId != None """
        
class GenericId(ObjectId):
    u"""
    Generic identifier type for identifiers whose format is othterwise unknown to openEHR. 
    Includes an attribute for naming the identification scheme (which may well be local).
    """

    implements(IGenericId)

    def __init__(self,value,scheme,**kwargs):
        self.value = value
        self.scheme=scheme
        Field.__init__(self,**kwargs)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''


    def schemeValid():
        return self.scheme!=None and self.scheme!=''
        
class ObjectRef(Field):
    u"""
    Class describing a reference to another object, which may exist locally or be
    maintained outside the current namespace, e.g. in another service. Services are
    usually external, e.g. available in a LAN (including on the same host) or the inter-
    net via Corba, SOAP, or some other distributed protocol. However, in small sys-
    tems they may be part of the same executable as the data containing the Id.
    """

    implements(IObjectRef)
    
    def __init__(self,id,nameSpace,type,**kwargs):
        self.id=id
        self.nameSpace=nameSpace
        self.type=type
        Field.__init__(self,**kwargs)

        
    def idExists():
        u""" id != None """
        
    def nameSpaceExists():
        u""" nameSpace != None and nameSpace != '' """
        
    def typeExists():
        u""" type != None and type != '' """



class AccessGroupRef(ObjectRef):
    u""" Reference to access group in an access control service. """

    implements(IAccessGroupRef)
    
    def __init__(self,id,nameSpace,type,**kwargs):
        self.id=id
        self.nameSpace=nameSpace
        self.type=type     
        Field.__init__(self,**kwargs)
        
        
    def idExists():
        u""" id != None """
        
    def nameSpaceExists():
        u""" nameSpace != None and nameSpace != '' """
        
    def typeExists():
        u""" type != None and type != '' """
      
    def typeValidity():
        u""" True if type == 'ACCESS_GROUP' """
        
        
class PartyRef(ObjectRef):
    u"""
    Identifier for parties in a demographic or identity service. There are typically a
    number of subtypes of the PARTY class, including PERSON, ORGANISATION, etc.
        
    Abstract supertypes are allowed if the referenced object is of a type not known by
    the current implementation of this class (in other words, if the demographic model
    is changed by the addition of a new PARTY or ACTOR subtypes, valid
    PartyRefs can still be constructed to them).
    """

    implements(IPartyRef)
    
    def __init__(self,id,nameSpace,type,**kwargs):
        self.id=id
        self.nameSpace=nameSpace
        self.type=type     
        Field.__init__(self,**kwargs)
        
        
    def idExists():
        u""" id != None """
        
    def nameSpaceExists():
        u""" nameSpace != None and nameSpace != '' """
        
    def typeExists():
        u""" type != None and type != '' """

    
    def typeValidity():
        u"""
        type is in ["PERSON","ORGANISATION","GROUP","AGENT","ROLE","PARTY","ACTOR"]
        """
        
class LocatableRef(ObjectRef):
    u"""
    Reference to a LOCATABLE instance inside the top-level content structure inside a
    VERSION<T>; the path attribute is applied to the object that VERSION.data points to.
    """

    implements(ILocatableRef)
    
    def __init__(self,id,path,nameSpace,type,**kwargs):
        self.id=id
        self.path=path
        self.nameSpace=nameSpace
        self.type=type     
        Field.__init__(self,**kwargs)
        
    def idExists():
        u""" id != None """
        
    def nameSpaceExists():
        u""" nameSpace != None and nameSpace != '' """
        
    def typeExists():
        u""" type != None and type != '' """
    
    def asUri():
        u"""
        A URI form of the reference, created by concatenating the following:
        "ehr://" + id.value + "/" + path
        """
        
    def pathValid():
        u""" path != None and path != '' """