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
from zope.schema import Field

_ = MessageFactory('oship')

class ResourceDescriptionItem(Field):
    u"""Language-specific detail of resource description. When a resource is translated
        for use in another language environment, each RESOURCE_DESCRIPTION_ITEM
        needs to be copied and translated into the new language.
    """

    pass

    """
    language=CodePhrase('','',
        title=_(u'Language'),
        description=_(u""""""),
        required=True
    )
    
    purpose=TextLine(
        title=_(u'Purpose'),
        description=_(u""""""),
        required=True
    )
    
    keywords=List(
        title=_(u'Keywords'),
        description=_(u""""""),
        required=False
    )
    
    use=TextLine(
        title=_(u'Use'),
        description=_(u""""""),
        required=False
    )

    misuse=TextLine(
        title=_(u'Misuse'),
        description=_(u""""""),
        required=False
    )
    
    copyright=TextLine(
        title=_(u'Copyright'),
        description=_(u""""""),
        required=False
    )
    
    originalResourceUri=Dict(
        title=_(u'Original Resource URI'),
        description=_(u""""""),
        required=False
    )
    
    otherDetails=Dict(
        title=_(u'Other Details'),
        description=_(u""""""),
        required=False
    )
    
    """
    