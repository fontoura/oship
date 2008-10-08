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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'


from zope.i18nmessageid.message import MessageFactory 

from uidbasedid import IUidBasedId

_ = MessageFactory('oship')


class IObjectVersionId(IUidBasedId):
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
	
    
