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

class ResourceDescription(Field):
    u"""Defines the descriptive meta-data of a resource."""
    
    pass

    """
    originalAuthor=Dict(
        title=_(u'Original Author'),
        description=_(u""""""),
        required=True
    )
    
    otherContributors=List(
        title=_(u'Other Contributors'),
        description=_(u""""""),
        required=False
    )
    
    lifecycleState=TextLine(
        title=_(u'Lifecycle State'),
        description=_(u""""""),
        required=True
    )
    
    details=Dict(
        title=_(u'Details'),
        description=_(u""""""),
        required=True
    )
    
    resourcePackageUri=TextLine(
        title=_(u'Resource Package URI'),
        description=_(u""""""),
        required=False
    )
    
    otherDetails=Dict(
        title=_(u'Other Details'),
        description=_(u""""""),
        required=False
    )
    
    parentResource=AuthoredResource(
        title=_(u'Parent Resource'),
        description=_(u""""""),
        required=False
    )
    
    """
    
    
    
    
    
    
    
    