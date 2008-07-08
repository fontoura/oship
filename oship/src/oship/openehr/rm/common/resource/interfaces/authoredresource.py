# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the resource package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
 
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema import Bool,Object

from openehr.rm.datatypes.text.interfaces.codephrase import ICodePhrase
from openehr.rm.common.resource.interfaces.translationdetails import ITranslationDetails
from openehr.rm.common.resource.interfaces.resourcedescription import IResourceDescription
from openehr.rm.common.generic.interfaces.revisionhistory import IRevisionHistory

_ = MessageFactory('oship')

class IAuthoredResource(Interface):
    u"""Abstract idea of an online resource created by a human author. """
    
    orignialLanguage=Object(
        schema=ICodePhrase,
        title=_(u"Original Language"),
        description=_(u""""""),
        required=True
    )
       
    translations=Object(
        schema=ITranslationDetails,
        title=_(u"Translations"),
        description=_(u"Translations"),
        required=False
    )
    
    
    description=Object(
        schema=IResourceDescription,
        title=_(u"Description"),
        description=_(u""""""),
        required=False
    )
       
    revisionHistory=Object(
        schema=IRevisionHistory,
        title=_(u"Revision History"),
        description=_(u""""""),
        required=False
    )
    
    isControlled=Bool(
        title=_(u"Is Controlled"),
        description=_(u""""""),
        required=True
    )
    
    def currentRevision():
        u""""""
        
    def languagesAvailable():
        u""""""
        
        
                               
    