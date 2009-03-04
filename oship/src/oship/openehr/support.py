# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

Support Information Model Rev. 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
import copy

from zope.interface import Interface, implements
from zope.schema import TextLine,Object,Field,URI 
from zope.schema.interfaces import IContainer
from zope.i18nmessageid import MessageFactory

import grok

_ = MessageFactory('oship')

__author__ = u'Fabricio Ferracioli <fabricioferracioli@gmail.com>'
__contributors__ = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'



#Begin Definition package
class IBasicDefinitions(Interface):
    """ Defines globally used constant values. """

    cr = TextLine(
        title=_(u"CR"),
        description=_(u"Carriage Return Character"),
        readonly=True,
    )


    lf = TextLine(
        title=_(u"LF"),
        description=_(u"Line Feed Character"),
        readonly=True,
    )

class BasicDefinitions(grok.Model):
    """ Defines globally used constant values. """

    implements(IBasicDefinitions)

    def __init__(self):
        self.cr=u"\015"
        self.lf=u"\012"


class IOpenehrDefinitions(Interface):
    """ Inheritance class to provide access to constants defined in other packages."""

    pass

class OpenehrDefinitions(BasicDefinitions):
    """ Inheritance class to provide access to constants defined in other packages."""

    implements(IOpenehrDefinitions)

    pass

#Begin Indentification package


class IObjectId(Interface):
    u"""
    Ancestor (abstract) class of identifiers of informational objects. Ids may be completely
    meaningless, in which case their only job is to refer to something, or may carry
    some information to do with the identified object.
    Object ids are used inside an object to identify that object. To identify another
    object in another service, use an OBJECT_REF, or else use a UID for local objects
    identified by UID. If none of the subtypes is suitable, direct instances of this class
    may be used.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        required=False,
    )

class ObjectId(grok.Model):
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

    def __init__(self, value):
        self.value = value




class IObjectRef(Interface):
    u"""
    Class describing a reference to another object, which may exist locally or be
    maintained outside the current namespace, e.g. in another service. Services are
    usually external, e.g. available in a LAN (including on the same host) or the inter-
    net via Corba, SOAP, or some other distributed protocol. However, in small sys-
    tems they may be part of the same executable as the data containing the Id.
    """

    refId = Object(
        schema=IObjectId,
        title = _(u'Id'),
        description = _(u'Globally unique id of an object (of type ObjectId), regardless of where it is stored.'),
        required = False,
    )

    refNameSpace = TextLine(
        title = _(u"Namespace"),
        description = _(u"""Namespace to which this identifier belongs in
                        the local system context (and possibly in any
                        other openEHR compliant environment) e.g.
                        "terminology", "demographic". These names
                        are not yet standardised. Legal values for the
                        namespace are
                        "local" | "unknown" | "[a-zA-
                        Z][a-zA-Z0-9_-:/&+?]*" """),
        required = False,
    )


    refType = TextLine(
        title = _(u"Type"),
        description = _(u"""Name of the class (concrete or abstract) of object to which this 
                        identifier type refers, e.g."PARTY", "PERSON", "GUIDELINE" etc.
                        These class names are from the relevant reference model. 
                        The type name "ANY" can be used to indicate that any type is accepted 
                        (e.g. if the type is unknown). """),
        required = False,
    )

class ObjectRef(grok.Model):
    u"""
    Class describing a reference to another object, which may exist locally or be
    maintained outside the current namespace, e.g. in another service. Services are
    usually external, e.g. available in a LAN (including on the same host) or the inter-
    net via Corba, SOAP, or some other distributed protocol. However, in small sys-
    tems they may be part of the same executable as the data containing the Id.
    """

    implements(IObjectRef)

    def __init__(self,refId,refNameSpace,refType):        
        self.refId=refId
        self.refNameSpace=refNameSpace
        self.refType=refType

    def __eq__(self, other):
        if not isinstance(other,  ObjectRef):
            return False
        if self.refId != other.refId:
            return False
        if self.refNameSpace != other.refNameSpace:
            return False
        return self.refType == other.refType


class IAccessGroupRef(Interface):
    u""" Reference to access group in an access control service. """  

    type = TextLine(
        title = _(u"Type"),
        description = _(u"""Name of the class (concrete or abstract) of object to which this 
                        identifier type refers, e.g."PARTY", "PERSON", "GUIDELINE" etc.
                        These class names are from the relevant reference model. 
                        The type name "ANY" can be used to indicate that any type is accepted 
                        (e.g. if the type is unknown). """),

    )

    #@invariant
    #def validateType(self):
            #return self.type in ["PERSON","PARTY","GUIDELINE"]

class AccessGroupRef(ObjectRef):
    u""" Reference to access group in an access control service. """

    implements(IAccessGroupRef)

    def __init__(self,id,nameSpace,type):
        self.id=id
        self.nameSpace=nameSpace
        self.type=type     

    def validateType(self):
        u"""
        type is in "ACCESS_GROUP"
        """
        return self.type == 'ACCESS_GROUP'






class IArchetypeId(Interface):
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



    def __init__(self, value):
        ObjectId.__init__(self, value)

        #AXIS_SEPARATOR = u'.'
        #SECTION_SEPARATOR = u'-'   
        #NAME_PATTERN = r"[a-zA-Z][a-zA-Z0-9()_/%$#&]*"
        #VERSION_PATTERN = r"[a-zA-Z0-9]+"
        #"""
        #value is a unicode str of the full archetype ID from the ADL       
        #"""
        #self.value = value
        #tokens = value.split(self.AXIS_SEPARATOR)
        #if len(tokens) != 3:
                #raise ValueError, 'bad format, wrong number of sections'
        #self.__qualifiedRmEntity = tokens[0]

        #self.__domainConcept = tokens[1]
        #self.__version = tokens[2]
        #self.__validateVersionId(self.__version)

        #tokens = self.__qualifiedRmEntity.split(self.SECTION_SEPARATOR)
        #if len(tokens) != 3:
                #raise ValueError, 'bad format, wrong number of sections in ' + self.value
        #self.__rmOriginator = tokens[0]
        #self.__validateName(self.__rmOriginator, 'rm_originator')
        #self.__rmName = tokens[1]
        #self.__validateName(self.__rmName, 'rm_name')
        #self.__rmEntity = tokens[2]
        #self.__validateName(self.__rmEntity, 'rm_entity')

        #tokens = self.__domainConcept.split(self.SECTION_SEPARATOR)
        #if len(tokens) < 1:
                #raise ValueError, 'bad format, too few sections for domainConcept in ' + self.value
        #self.__conceptName = tokens[0]    
        #self.__validateName(self.__conceptName, 'concept_name')
        #if len(tokens) > 1:
                #self.__specialisation = tokens[-1]
                #self.__validateName(self.__specialisation, 'specialisation')
        #else:
                #self.__specialisation = None

    def __validateName(self, value, label):
        match = re.compile(self.NAME_PATTERN).match(value)
        if (match is None) or (match.end() < len(value)):
            raise ValueError, 'wrong format of ' + label + ': ' + value

    def __validateVersionId(self, version):
        match = re.compile(self.VERSION_PATTERN).match(version)
        if (match is None) or (match.end() < len(version)):
            raise ValueError, 'wrong format of versionId: ' + version

    def qualifiedRmEntity(self):
        u"""
        Globally qualified reference model entity, e.g. "openehr-composition-OBSERVATION".
        """
        return self.__qualifiedRmEntity

    def domainConcept(self):
        u"""
        Name of the concept represented by this archetype, including specialisation, 
        e.g. "biochemistry_result-cholesterol".
        """
        return self.__domainConcept

    def rmOriginator(self):
        u"""
        Organisation originating the reference model on which this archetype is based, 
        e.g. "openehr", "cen", "hl7".
        """
        return self.__rmOriginator

    def rmName(self):
        u"""
        Name of the reference model, e.g. "rim","ehr_rm", "en13606".
        """
        return self.__rmName

    def rmEntity(self):
        u"""
        Name of the ontological level within the reference model to which this archetype is 
        targeted, e.g. for openEHR, "folder","composition", "section", "entry".
        """
        return self.__rmEntity

    def specialisation(self): 
        u"""
        Name of specialisation of concept, if this archetype is a specialisation of another 
        archetype, e.g. "cholesterol".
        """
        return self.__specialisation;

    def versionId(self):
        u"""
        Version of this archetype.
        """
        return self.__version





class IGenericId(Interface):
    u"""
    Generic identifier type for identifiers whose format is othterwise unknown to openEHR. 
    Includes an attribute for naming the identification scheme (which may well be local).
    """

    scheme = TextLine(
        title = _(u"Scheme"),
        description = _(u"Name of the scheme to which this identifier conforms."),
        required = True
    )

class GenericId(ObjectId):
    u"""
    Generic identifier type for identifiers whose format is othterwise unknown to openEHR. 
    Includes an attribute for naming the identification scheme (which may well be local).
    """

    implements(IGenericId)

    def __init__(self,scheme):
        self.scheme=scheme

    def __eq__(self, other):
        if not isinstance(other,  GenericId):
            return False
        if self.value != other.value:
            return False
        return self.scheme == other.scheme    

class IUidBasedId(Interface):
    u"""
    Abstract model of UID-based identifiers consisting of a root part and an optional
    extension; lexical form: root '::' extension
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        required=True)

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



class UidBasedId(ObjectId,Field):
    u"""
    Abstract model of UID-based identifiers consisting of a root part and an optional
    extension; lexical form: root '::' extension
    """

    implements(IUidBasedId)

    def __init__(self, value,**kw):
        Field.__init__(self,**kw)
        self.value = value
        self.rootPart = None
        self.extensionPart = None

    def root(self):
        u"""
        The identifier of the conceptual namespace in which the object exists, within 
        the identification scheme.
        Returns the part to the left of the first '::' separator, if any, or else the whole string.
        """
        return self.rootPart

    def extension(self):
        u"""
        Optional local identifier of the object within the context of the root identifier.
        Returns the part to the right of the first '::' separator if any, or else any empty String.
        """
        return self.extensionPart

    def hasExtension(self):
        u""" True if extension != '' """
        return not self.extensionPart != ''


class IHierObjectId(Interface):
    u"""
    Concrete type corresponding to hierarchical identifiers of the form defined by UID_BASED_ID.
    """

    pass

class HierObjectId(UidBasedId):
    u"""
    Concrete type corresponding to hierarchical identifiers of the form defined by UID_BASED_ID.
    """

    implements(IHierObjectId)

    def __init__(self, value):
        self.__name__=''
        self.value = value
        doubleColons = value.find('::')
        # Check for root segment
        if doubleColons == 0:
            raise ValueError('bad format, missing root')

        elif doubleColons > 0:
            rootStr = value[0:doubleColons]
        else:
            rootStr = value

        matchUUID = re.compile(self.SIMPLE_UUID_PATTERN).match(rootStr)
        matchISO = re.compile(self.SIMPLE_ISOOID_PATTERN).match(rootStr)
        matchInternet = re.compile(self.SIMPLE_INTERNET_PATTERN).match(rootStr)
        if (matchUUID is not None) and (matchUUID.start() == 0) and (matchUUID.end() == len(rootStr)):
            self.rootPart = Uuid(rootStr)
        elif (matchISO is not None) and (matchISO.start() == 0) and (matchISO.end() == len(rootStr)):
            self.rootPart = IsoOid(rootStr);
        elif (matchInternet is not None) and (matchInternet.start() == 0) and (matchInternet.end() == len(rootStr)):
            self.rootPart = InternetId(rootStr);
        else:
            raise ValueError("wrong format")

        if (0 < doubleColons) and (doubleColons < (len(value) - 2)):
            self.extensionPart = value[doubleColons + 2:]
        else:
            self.extensionPart = ''

class IUid(Interface):
    u"""
    Abstract parent of classes representing unique identifiers which identify informa-
    tion entities in a durable way. UIDs only ever identify one IE in time or space and
    are never re-used.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid UID"),
        required=True
    )

class Uid(grok.Model):
    u"""
    Abstract parent of classes representing unique identifiers which identify informa-
    tion entities in a durable way. UIDs only ever identify one IE in time or space and
    are never re-used.
    """

    implements(IUid)

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other,  Uid):
            return False
        return self.value == other.value



class IInternetId(Interface):
    u"""
    Model of a reverse internet domain, as used to uniquely identify an internet
    domain. In the form of a dot-separated string in the reverse order of a domain
    name specified by IETF RFC1034 (http://www.ietf.org/rfc/rfc1034.txt).
    """

    value = URI(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid URL"),
        required=True
    )

class InternetId(Uid):
    u"""
    Model of a reverse internet domain, as used to uniquely identify an internet
    domain. In the form of a dot-separated string in the reverse order of a domain
    name specified by IETF RFC1034 (http://www.ietf.org/rfc/rfc1034.txt).
    """

    implements(IInternetId)

    def __init__(self, value):
        Uid.__init__(self,value)


class IIsoOid(Interface):
    u"""
    Model of ISO's Object Identifier (oid) as defined by the standard ISO/IEC 8824 .
    Oids are formed from integers separated by dots. Each non-leaf node in an Oid
    starting from the left corresponds to an assigning authority, and identifies that
    authority's namespace, inside which the remaining part of the identifier is locally unique.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid UID"),
        required=True)

class IsoOid(Uid):
    u"""
    Model of ISO's Object Identifier (oid) as defined by the standard ISO/IEC 8824 .
    Oids are formed from integers separated by dots. Each non-leaf node in an Oid
    starting from the left corresponds to an assigning authority, and identifies that
    authority's namespace, inside which the remaining part of the identifier is locally unique.
    """

    implements(IIsoOid)

    def __init__(self, value):
        Uid.__init__(self,value)


class ILocatableRef(Interface):
    u"""
    Reference to a LOCATABLE instance inside the top-level content structure inside a
    VERSION<T>; the path attribute is applied to the object that VERSION.data points to.
    """

    id = Object(
        schema=IUidBasedId,
        title = _(u'Id'),
        description = _(u'Globally unique id of an object (of type UidBasedId), regardless of where it is stored.'),
        required = True
    )

    path = TextLine(
        title = _(u"Path"),
        description=_(u"""The path to an instance in question, as an absolute path 
                      with respect to the object found at VERSION.data. An empty path means that
                      the object referred to by id being specified."""),
        required = False
    )


    def asUri():
        u""" 
        A URI form of the reference, created by concatenating the following:
        "ehr://" + id.value + "/" + path
        """

class LocatableRef(ObjectRef):
    u"""
    Reference to a LOCATABLE instance inside the top-level content structure inside a
    VERSION<T>; the path attribute is applied to the object that VERSION.data points to.
    """

    implements(ILocatableRef)

    def __init__(self,id,path,refId,refNameSpace,refType):
        ObjectRef.__init__(self,refId,refNameSpace,refType)
        self.id=id
        self.path=path

    def asUri():
        u"""
        A URI form of the reference, created by concatenating the following:
        "ehr://" + id.value + "/" + path
        """
        return 'ehr://' + self.id.value + "/" + self.path

    def __eq__(self, other):
        if not isinstance(other,  LocatableRef):
            return False
        if self.id != other.id:
            return False
        return self.path == other.path




class IObjectVersionId(Interface):
    u"""
    Globally unique identifier for one version of a versioned object; lexical form:
    object_id '::' creating_system_id '::' version_tree_id
    
    An example ObjectVersionId is as follows:
    F7C5C7B7-75DB-4b39-9A1E-C0BA9BFDBDEC::87284370-2D4B-4e3d-A3F3-F303D2F4F34B::2  
    """

    def objectId():
        u"""
        Unique identifier for logical object of which this identifier identifies one version;
        normally the object_id will be the unique identifier of the version container containing
        the version referred to by this OBJECT_VERSION_ID instance.
        """
	
    def versionTreeId():
        u"""
        Tree identifier of this version with respect to other versions in the same version tree,
        as either 1 or 3 part dot-separated numbers, e.g. '1', '2.1.4'.  
        """
	
    def creatingSystemId():
        u"""
        Identifier of the system that created the Version corresponding to this Object version id.
        """
        
    def isBranch():
        u"""
        True if this version identifier represents a branch. 
        """
	
    


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

    SIMPLE_UUID_PATTERN = r"([0-9a-fA-F])+(-([0-9a-fA-F])+)*"
    SIMPLE_ISOOID_PATTERN = r"(\d)+(\.(\d)+)*"
    SIMPLE_INTERNET_PATTERN = r"(\w)+(\.(\w)+)*"

    def __init__(self,value):
        self.value=value

        # Steps for value checking:
        # 1. Check if value contains any :: or starts with ::
        doubleColons = value.find('::')
        if doubleColons <= 0:
            raise(ValueError, 'bad format, missing objectId')

        # 2. Check how many segments in the value
        splits = value.split('::')
        segments = len(splits)
        if segments < 3:
            raise(ValueError, 'bad format, missing creatingSystemId or versionTreeId')
        if segments > 4:
            raise(ValueError, 'bad format, too many segments or "::"')

        # 3. Construct objects for each segment
        # the patterns below are for sorting only, the correct syntax
        # checking is handled by the UID sublcasses.
        rootStr = splits[0]
        matchUUID = re.compile(self.SIMPLE_UUID_PATTERN).match(rootStr)
        matchISO = re.compile(self.SIMPLE_ISOOID_PATTERN).match(rootStr)
        matchInternet = re.compile(self.SIMPLE_INTERNET_PATTERN).match(rootStr)
        if (matchUUID is not None) and (matchUUID.start() == 0) and (matchUUID.end() == len(rootStr)):
            self.__objectId = Uuid(rootStr)
        elif (matchISO is not None) and (matchISO.start() == 0) and (matchISO.end() == len(rootStr)):
            self.__objectId = IsoOid(rootStr);
        elif (matchInternet is not None) and (matchInternet.start() == 0) and (matchInternet.end() == len(rootStr)):
            self.__objectId = InternetId(rootStr);
        else:
            raise ValueError('wrong format ' + rootStr)

        if (segments == 4):
            self.__creatingSystemId = HierObjectId(splits[1] + '::' + splits[2])
            self.__versionTreeId = VersionTreeId(splits[3])
        else:
            self.__creatingSystemId = HierObjectId(splits[1])
            self.__versionTreeId = VersionTreeId(splits[2])

        self.rootPart = self.objectId
        self.extensionPart = self.__creatingSystemId.value + '::' + self.__versionTreeId.value   


    def  objectId(self):
        u"""
        Unique identifier for logical object of which this identifier identifies one version;
        normally the object_id will be the unique identifier of the version container containing
        the version referred to by this OBJECT_VERSION_ID instance.
        """
        return self.__objectId

    def versionTreeId(self):
        u"""
        Tree identifier of this version with respect to other versions in the same version tree,
        as either 1 or 3 part dot-separated numbers, e.g. '1', '2.1.4'.  
        """
        return self.__versionTreeId

    def creatingSystemId(self):
        u"""
        Identifier of the system that created the Version corresponding to this Object version id.
        """
        return self.__creatingSystemId

    def isBranch():
        u"""
        True if this version identifier represents a branch. 
        """
        return self.__versionTreeId.isBranch()


class IPartyRef(Interface):
    u"""
    Identifier for parties in a demographic or identity service. There are typically a
    number of subtypes of the PARTY class, including PERSON, ORGANISATION, etc.

    Abstract supertypes are allowed if the referenced object is of a type not known by
    the current implementation of this class (in other words, if the demographic model
    is changed by the addition of a new PARTY or ACTOR subtypes, valid
    PartyRefs can still be constructed to them).
    """

    type = TextLine(
        title = _(u"Type"),
        description = _(u"""Name of the class (concrete or abstract) of object to which this 
                        identifier type refers, e.g."PARTY", "PERSON", "GUIDELINE" etc.
                        These class names are from the relevant reference model. 
                        The type name "ANY" can be used to indicate that any type is accepted 
                        (e.g. if the type is unknown). """),
        
        #constraint = validateType
        )
    

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

    def __init__(self,id,nameSpace,type):
        self.id=id
        self.nameSpace=nameSpace
        self.type=type     

    def validateType(self):
        u"""
        type is in ["PERSON","ORGANISATION","GROUP","AGENT","ROLE","PARTY","ACTOR"]
        """
        return self.type in ['PERSON','ORGANISATION','GROUP','AGENT','ROLE','PARTY','ACTOR']



class ITemplateId(Interface):
    u""" Identifier for templates. Lexical form to be determined. """
    
    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid ID"),
        
    )    


class TemplateId(ObjectId):
    u""" Identifier for templates. Lexical form to be determined. """

    implements(ITemplateId)

    def __init__(self, value):
        self.value = value


class ITerminologyId(Interface):
    u"""
    Identifier for terminologies such accessed via a terminology query service. In this
    class, the value attribute identifies the Terminology in the terminology service,
    e.g. "SNOMED-CT". A terminology is assumed to be in a particular language,
    which must be explicitly specified.
    
    The value if the id attribute is the precise terminology id identifier, including
    actual release (i.e. actual "version"), local modifications etc; e.g. "ICPC2".
    Lexical form: name [ '(' version ')' ]
    """

    def name():
        u"""
        Return the terminology id (which includes the "version" in some cases). 
        Distinct names correspond to distinct (i.e. non-compatible) terminologies.
        Thus the names "ICD10AM" and "ICD10" refer to distinct terminologies.
        """
        
    def versionId():
        u""" Version of this terminology, if versioning supported, else the empty string."""

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

    def __init__(self, name):
        self.value = name
        parts = name.partition('(')
        self.__name = parts[0]
        self.__version = parts[2].rstrip(')')

    def name(self):
        u"""
        Return the terminology id (which includes the "version" in some cases). 
        Distinct names correspond to distinct (i.e. non-compatible) terminologies.
        Thus the names "ICD10AM" and "ICD10" refer to distinct terminologies.
        """
        return self.__name

    def versionId(self):
        u""" Version of this terminology, if versioning supported, else the empty string."""
        return self.__version


class IUuid(Interface):
    u"""
    Model of the DCE Universal Unique Identifier or UUID which takes the form of
    hexadecimal integers separated by hyphens, following the pattern 8-4-4-4-12 as
    defined by the Open Group, CDE 1.1 Remote Procedure Call specification,
    Appendix A. Also known as a GUID.
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid UID"),

    )

class Uuid(Uid):
    u"""
    Model of the DCE Universal Unique Identifier or UUID which takes the form of
    hexadecimal integers separated by hyphens, following the pattern 8-4-4-4-12 as
    defined by the Open Group, CDE 1.1 Remote Procedure Call specification,
    Appendix A. Also known as a GUID.
    """

    implements(IUuid)

    def __init__(self, value):
        self.value = value

class IVersionTreeId(Interface):
    u"""
    Version tree identifier for one version. Lexical form:
    trunkVersion [ '.' branchNumber '.' branchVersion ]
    """

    value = TextLine(
        title=_(u"Value"),
        description=_(u"String form of this Version Tree identifier."),
    )

    def trunkVersion():
        u"""
        Returns a string of the trunk version number; numbering starts at 1.     
        """

    def branchNumber():
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """

    def branchVersion():
        u"""
        Version of the branch; numbering starts at 1.
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

class VersionTreeId(grok.Model):
    u"""
    Version tree identifier for one version. Lexical form:
    trunkVersion [ '.' branchNumber '.' branchVersion ]
    """

    implements(IVersionTreeId)

    PATTERN = r"[1-9](\d)*(\.(\d)+\.(\d)+)?"    

    def __init__(self, value):
        self.__branchNumber = None
        self.__branchVersion = None
        match = re.compile(self.PATTERN).match(value)
        if (match is None) or (match.start() != 0) or (match.end() != len(value)):
            raise(ValueError, 'wrong format')

        branch = value.find('.')
        if branch < 0: # no branch, just trunk
            self.__trunkVersion = value;
            self.value = value;
        else:
            entries = value.split(r".")
            self.__validateValues(int(entries[0]), int(entries[1]), int(entries[2]))
            self.__trunkVersion = entries[0]
            # never set branchNo or branchV to 0
            if int(entries[1]) > 0:
                self.__branchNumber = entries[1]
                self.__branchVersion = entries[2]
                self.value = value;
            else:
                self.value = entries[0]

    def __validateValues(self, trunk, branchNo, branchV):
        if (trunk < 1) or (branchNo < 0) or (branchV < 0):
            raise(ValueError, 'version number smaller than 0')

        # 0 for branchNo or branchV is special case,
        # where both must be 0 to indicate no branch
        if (branchNo == 0) or (branchV == 0):
            if branchV != branchNo:
                raise(ValueError, 'breach of branch_validity') 


    def trunkVersion(self):
        u"""
        Returns a string of the trunk version number; numbering starts at 1.     
        """
        return self.__trunkVersion


    def branchNumber(self):
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """
        return self.__branchNumber

    def branchVersion(self):
        u"""
        Number of branch from the trunk point; numbering starts at 1.
        """
        return self.__branchVersion

    def isBranch():
        u"""
        Returns True if this version identifier represents a branch,
        i.e. has branchNumber and branchVersion parts.
        """
        return not self.__branchVersion is None

    def isFirst(self):
        u"""
        True if this version identifier corresponds to the
        first version, i.e. trunkVersion == "1"
        """
        return self.__trunkVersion == '1' and  (not self.isBranch())

    def __loadValue(self, value):
        match = re.compile(self.PATTERN).match(value)
        if (match is None) or (match.start() != 0) or (match.end() != len(value)):
            raise(ValueError, 'wrong format')

        branch = value.find('.')
        if branch < 0: # no branch, just trunk
            self.__trunkVersion = value;
            self.value = value;
        else:
            entries = value.split(r".")
            self.__validateValues(int(entries[0]), int(entries[1]), int(entries[2]))
            self.__trunkVersion = entries[0]
            # never set branchNo or branchV to 0
            if int(entries[1]) > 0:
                self.__branchNumber = entries[1]
                self.__branchVersion = entries[2]
                self.value = value;
            else:
                self.value = entries[0]

    def __validateValues(self, trunk, branchNo, branchV):
        if (trunk < 1) or (branchNo < 0) or (branchV < 0):
            raise(ValueError, 'version number smaller than 0')

        # 0 for branchNo or branchV is special case,
        # where both must be 0 to indicate no branch
        if (branchNo == 0) or (branchV == 0):
            if branchV != branchNo:
                raise(ValueError, 'breach of branch_validity') 

    def branchNumber(self):
        return self.__branchNumber

    def __eq__(self, other):
        if not isinstance(other,  VersionTreeId):
            return False
        return self.value == other.value

#Begin Measurement package
class IMeasurementService(Interface):
    """Defines an object providing proxy access to a measurement information service."""



    def isValidUnitsString(units):
        u"""
        True if the units string 'units' is a valid string according to the HL7 UCUM specification.
        units != None                   
        """

    def unitsEquivalent(units1, units2):
        u"""
        True if two units strings correspond to the same measured property.
        isValidUnitsString(units1) and isValidUnitsString(units2)
        """

class MeasurementService(grok.Model):
    """Defines an object providing proxy access to a measurement information service."""

    implements(IMeasurementService)


    def isValidUnitsString(units):
        u"""
        True if the units string 'units' is a valid string according to the HL7 UCUM specification.
        units != None                   
        """

    def unitsEquivalent(units1, units2):
        u"""
        True if two units strings correspond to the same measured property.
        isValidUnitsString(units1) and isValidUnitsString(units2)
        """


#Begin Terminology package
class CodeSetAccess(grok.Model):
    u"""
    Defines an object providing proxy access to a code_set.
    """

    def id(idStr):
        u"""External identifier of this Code Set"""

    def allCodes(codeSet):
        u""" Return all codes known in this code set as CodePhrases"""

    def hasLang(a_lang):
        u""" True if code set knows about 'a_lang' """

    def hasCode(a_code):
        u""" True if code set knows about 'a_code' """

    def idValid(idStr):
        u""" True if id != None and id != ''  """
        
        
class OpenehrCodeSetIdentifiers():
    u""" 
    List of identifiers for code sets in the openEHR terminology. 
    """

    CodeSetIdCharacterSets='character sets'
    CodeSetIdCompressionAlgorithms='compression algorithms'
    CodeSetIdCountries='countries'
    CodeSetIdIntegrityCheckAlgorithms='integrity check algorithms'
    CodeSetIdLanguages='languages'
    CodeSetIdMediaTypes='media types'
    CodeSetIdNormalStatuses='normal statuses'
    values=(CodeSetIdCharacterSets, CodeSetIdCompressionAlgorithms, CodeSetIdCountries, CodeSetIdIntegrityCheckAlgorithms, CodeSetIdLanguages, CodeSetIdMediaTypes, CodeSetIdNormalStatuses)

def validCodeSetId(anId):
    u"""
    Boolean Validity function to test if an identifier is in 
    the tuple defined by class OpenehrCodeSetIdentifiers.
    """
    return anId in OpenehrCodeSetIdentifiers.values

class OpenehrTerminologyGroupIdentifiers():
    """
    List of identifiers for groups in the openEHR terminology.
    """
    terminologyId='openehr'
    groupIdAuditChangeType='audit change type'
    groupIdAttestationReason='attestation reason'
    groupIdCompositionCategory='composition category'
    groupIdEventMathFunction='event math function'
    groupIdIsmStates='instruction states'
    groupIdIsmTransitions='instruction transitions'
    groupIdNullFlavours='null flavours'
    groupIdMeasurableProperties='property'
    groupIdParticipationFunction='participation function'
    groupIdParticipationMode='participation mode'
    groupIdRelatedPartyRelationship='related party relationship'
    groupIdSetting='setting'
    groupIdTermMappingPurpose='term mapping purpose'	
    groupIdVersionLifecycleState='version lifecycle state'	

    values=(terminologyId, groupIdAuditChangeType, groupIdAttestationReason,\
            groupIdCompositionCategory, groupIdEventMathFunction, groupIdIsmStates, \
            groupIdIsmTransitions, groupIdNullFlavours, groupIdMeasurableProperties, \
            groupIdParticipationFunction, groupIdParticipationMode, \
            groupIdRelatedPartyRelationship, groupIdSetting, groupIdTermMappingPurpose, \
            groupIdVersionLifecycleState)

def validTerminologyGroupId(anId):
    u"""
    Validity function to test if an identifier is in the tuple defined by class OpenehrTerminologyGroupIdentifiers.
    """
    return anId in OpenehrTerminologyGroupIdentifiers.values


class TerminologyAccess(grok.Model):
    u"""
    Defines an object providing proxy access to a terminology.
    """

    def id(idStr):
        u"""ID of this code set"""
        
    def allCodes(codeSet):
        u""" Return all codes known in this terminology """

    def codesForGroupId(group_id):
        u"""
        Return all codes under grouper 'group_id' from this terminology
        """

    def hasCodeForGroupId(group_id, a_code):
        u"""
        True if 'a_code' is known in group 'group_id' in the openEHR terminology.
        """

    def codesForGroupName(name, lang):
        u"""
        Return all codes under grouper whose name in 'lang' is 'name' from this terminology
        """

    def rubricForCode(code, lang):
        u"""
        Return all rubric of code 'code' in language 'lang'.
        """

    def idExists():
        u""" True if id != None and id != '' """
        
        
class TerminologyService(grok.Model):
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

# Interval() and supporting classes
class Smallest:
    """Represents the smallest value

  This type doesn't do much; it implements a pseudo-value that's smaller
  than everything but itself.

  >>> negInf = Smallest()
  >>> smallest = Smallest()
  >>> -264 < negInf
  False
  >>> -264 == negInf
  False
  >>> -264 > negInf
  True
  >>> negInf < negInf
  False
  >>> negInf == smallest
  True
  """

    def __neg__(self):
        """Returns the largest value

    The opposite of negative infinity is infinity, the largest value.

    >>> print -Smallest()
    ~
    """
        return Largest()

    def __cmp__(self, other):
        """Compares this with another object

    Always indicates that self is less than other, unless both are of 
    type Smallest, in which case they are equal.

    >>> 0 < Smallest()
    False
    >>> -9999999 < Smallest()
    False
    >>> Smallest() < -9999999
    True
    >>> Smallest() < Smallest()
    False
    >>> Smallest() == Smallest()
    True
    """
        if other.__class__ == self.__class__:
            retval = 0
        else:
            retval = -1
        return retval

    def __str__(self):
        """Returns a printable representation of this value

      The string for the smallest number is -~, which means negative infinity.

      >>> print Smallest()
      -~
      """
        return "-~"

    def __repr__(self):
        """Returns an evaluable representation of the object

    The representation of the smallest number is -Inf, which means 
    negative infinity.

    >>> Smallest()
    -Inf
    """
        return "-Inf"

    def __hash__(self):
        "Returns a value that can be used for generating hashes"
        return 0x55555555

class Largest:
    """Class representing the universal largest value

  This type doesn't do much; it implements a pseudo-value that's larger
  than everything but itself.

  >>> infinity = Largest()
  >>> greatest = Largest()
  >>> 6234 < infinity
  True
  >>> 6234 == infinity
  False
  >>> 6234 > infinity
  False
  >>> infinity > infinity
  False
  >>> infinity == greatest
  True
  """

    def __neg__(self):
        """Returns the smallest universal value

    The opposite of infinity is negative infinity, the smallest value.

    >>> print -Largest()
    -~
    """
        return Smallest()

    def __cmp__(self, other):
        """Compares object with another object

    Always indicates that self is greater than other, unless both are of
    type Largest, in which case they are equal.

    >>> 0 > Largest()
    False
    >>> Largest() < 9999999
    False
    >>> Largest() > 9999999
    True
    >>> Largest() < Largest()
    False
    >>> Largest() == Largest()
    True
    """
        if other.__class__ == self.__class__:
            retval = 0
        else:
            retval = 1
        return retval

    def __str__(self):
        """Returns a string representation of the object

      The largest number is displayed as ~ (it sort of looks like infinity...)

      >>> print Largest()
      ~
      """
        return "~"

    def __repr__(self):
        """Returns an evaluable expression representing this object

    >>> Largest()
    Inf
    """
        return "Inf"

    def __hash__(self):
        "Returns a value that can be used for generating hashes"
        return -0x55555555


class Interval(Field):
    def __init__(self, lower=Smallest(), upper=Largest(), lower_included=False, upper_included=False,**kw):
        self.__name__=''

        """Initializes an interval

      Parameters
      ==========
      - lower: The lower bound of an interval (default Smallest())
      - upper: The upper bound of an interval (default Largest())
      - lower_included: Boolean telling if the lower value of interval are included (default True).
      - upper_included: Boolean telling if the greater value of interval are included (default True)

      An Interval can represent an infinite set.

      >>> r = Interval() # All values
      >>> r.has(0)
      True

      An Interval can represent sets unbounded on an end.

      >>> r = Interval(0,5)
      >>> r.has(-1)
      True
      >>> r.has(3)
      True
      >>> r.has(5.1)
      False

      An Interval can represent a set of values up to, but not including a
      value.

      >>> r = Interval(25, 28, False)
      >>> r.has(25)
      False
      >>> r.has(28)
      True

      An Interval can represent a set of values that have an inclusive
      boundary.

      >>> r = Interval(29, 216)

      An Interval can represent a single value

      >>> r = Interval(82, 82)
      >>> r.has(82)
      True

      Intervals that are not normalized, gives an exception.

      >>> r = Interval(4, 1)

      Intervals can represent an empty set.

      >>> r = Interval(5, 5, False, False)
      """
        if (lower == None or upper == None):
            raise ValueError('lower and upper must not be None')

        if (not isinstance(lower, Smallest) and not isinstance(upper, Largest)):
            if (type(lower) != type(upper)):
                raise TypeError('lower and upper must be of the same type')
        if (not callable(getattr(lower, '__cmp__')) or not callable(getattr(upper, '__cmp__'))):
            raise NotImplementedError('Classes are not comparable. Implement __cmp__ methods')

        if (lower > upper):
            raise ValueError('lower must be less than or equal to upper')

        if (lower_included and isinstance(lower, Smallest)):
            raise ValueError('lower_included implies lower greater than -Inf')

        if(upper_included and isinstance(upper, Largest)):
            raise ValueError('upper_included implies upper greater than Inf')

        self.lower = lower 
        if (isinstance(lower, Smallest)):
            self.lower_unbounded = True
        else:
            self.lower_unbounded = False
        self.lower_included = lower_included

        self.upper = upper
        if (isinstance(upper, Largest)):
            self.upper_unbounded = True
        else:
            self.upper_unbounded = False
        self.upper_included = upper_included

    def __hash__(self):
        """Returns a hashed value of the object

    Intervals are to be considered immutable.  Thus, a 32-bit hash can
    be generated for them.
    """
        return hash((self.lower_unbounded, self.upper_unbounded, self.lower, self.upper))

    def __repr__(self):
        """Returns an evaluable expression that can reproduce the object

    >>> Interval(3, 6)
    Interval(lower=3, upper=6, lower_unbounded=False, upper_unbounded=False, lower_included=True, upper_included=True)
        """
        return "Interval(lower=%s, upper=%s, lower_unbounded=%s, upper_unbounded=%s, lower_included=%s, upper_included=%s)" % (
            repr(self.lower), repr(self.upper), repr(self.lower_unbounded), repr(self.upper_unbounded), repr(self.lower_included), repr(self.upper_included))

    def has(self, value):
        """
    Returns if a value is inside the interval
    >>> interval = Interval(0,2)
    >>> interval.has(4)
    False
    >>> interval.has(1.5)
    True

    """

        if (value == None):
            raise ValueError('value must not be None')

        if (type(value) == type(self)):
            raise TypeError('value must be of the same type as self')

        #the value is between Smallest and Largest
        if (isinstance(self.lower, Smallest) and isinstance(self.upper, Largest)):
            return True
        #Smallest is the value of self.lower and upper is finite, need to test the value of upper
        elif (isinstance(self.lower, Smallest)):
            if (value < self.upper):
                return True
            else:
                #test for the upper closed interval
                return self.upper_included and value == self.upper
        #Largest is the value of self.upper and lower is finite, need to test the value of lower
        elif (isinstance(self.upper, Largest)):
            if (value > self.lower):
                return True
            else:
                #test for the lower closed interval
                return self.lower_included and value == self.lower
        else:
            #test for intervals that upper and lower values are finite
            if (value > self.lower and value < self.upper):
                return True
            else:
            #test for closed values
                if (self.lower_included and value == self.lower):
                    return True
                elif (self.upper_included and value == self.upper):
                    return True
                else:       
                    return False 
