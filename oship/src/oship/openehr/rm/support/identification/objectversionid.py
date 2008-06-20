# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements
from zope.schema import Bool
from zope.i18nmessageid.message import MessageFactory 

import uidbasedid
import uid
import versiontreeid

_ = MessageFactory('oship')


class IObjectVersionId(IUidBasedId):
    u"""
    Globally unique identifier for one version of a versioned object; lexical form:
    object_id '::' creating_system_id '::' version_tree_id
    
    An example ObjectVersionId is as follows:
    F7C5C7B7-75DB-4b39-9A1E-C0BA9BFDBDEC::87284370-2D4B-4e3d-A3F3-F303D2F4F34B::2  
    """

    objectId = Uid(
        title=_(u"Id"),
        description=_(u"Unique identifier for a single version of a logical object."),
        required=True)
    
    versionTreeId=VersionTreeId(
        title=_(u'Version Tree Id'),
        description=_(u'Tree identifier of this version.'),
        required=True)
    
    creatingSystemId=Uid(
        title=_(u'Creating System Id'),
        description=_(u'Identifier of the system that created this version.'),
        required=True)
    
    isBranch=Bool(
        title=_(u'Is Branch'),
        description=_(u'True if this version ID represents a branch.'),
        required=True)
            

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

    def __init__(self,objectId,versionTreeId,creatingSystemId,isBranch,**kw):
        self.objectId=objectId
        self.versionTreeId=versionTreeId
        self.creatingSystemId=creatingSystemId
        self.isBranch=isBranch
        for n,v in kw.items():
            setattr(self,n,v)

