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
from zope.schema.interfaces import IField
from zope.schema import TextLine, Dict

from openehr.rm.datatypes.text.codephrase import CodePhrase


_ = MessageFactory('oship')

class ITranslationDetails(IField):
    u""""""

    language=CodePhrase('','',
        title=_(u'Language'),
        description=_(u""" """),
        required=True
    )

    author=Dict(
        title=_(u'Author'),
        description=_(u""" """),
        required=True
    )
    
    accreditation=TextLine(
        title=_(u'Accreditation'),
        description=_(u""""""),
        required=False
    )    
    
    otherDetails=Dict(
        title=_(u'Other Details'),
        description=_(u""""""),
        required=False
    )
    