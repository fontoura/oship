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

from zope.schema import Bool,Object
from zope.i18nmessageid.message import MessageFactory 

from uidbasedid import IUidBasedId
from oship.openehr.rm.support.identification.interfaces.uuid import IUid
from oship.openehr.rm.support.identification.interfaces.versiontreeid import IVersionTreeId

_ = MessageFactory('oship')


class IObjectVersionId(IUidBasedId):
    u"""
    Globally unique identifier for one version of a versioned object; lexical form:
    object_id '::' creating_system_id '::' version_tree_id
    
    An example ObjectVersionId is as follows:
    F7C5C7B7-75DB-4b39-9A1E-C0BA9BFDBDEC::87284370-2D4B-4e3d-A3F3-F303D2F4F34B::2  
    """

    objectId = Object(
        schema=IUid,
        title=_(u"Id"),
        description=_(u"Unique identifier for a single version of a logical object."),
        required=True)
    
    versionTreeId=Object(
        schema=IVersionTreeId,
        title=_(u'Version Tree Id'),
        description=_(u'Tree identifier of this version.'),
        required=True)
    
    creatingSystemId=Object(
        schema=IUid,
        title=_(u'Creating System Id'),
        description=_(u'Identifier of the system that created this version.'),
        required=True)
    
    isBranch=Bool(
        title=_(u'Is Branch'),
        description=_(u'True if this version ID represents a branch.'),
        required=True)
            
