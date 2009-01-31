# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from uidbasedid import UidBasedId
from versiontreeid import VersionTreeId
from hierobjectid import HierObjectId
from uuid import Uuid
from internetid import InternetId
from isooid import IsoOid
import re
from interfaces.objectversionid import IObjectVersionId

_ = MessageFactory('oship')

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
