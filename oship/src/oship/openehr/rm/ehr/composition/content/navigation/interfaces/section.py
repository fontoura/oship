# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the navigation package from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = u'Renato Pesca <rpesca@gmail.com>'


from zope.i18nmessageid import MessageFactory
from zope.schema import List,Object

from oship.openehr.rm.ehr.composition.content.interfaces.contentitem import IContentItem

_ = MessageFactory('oship')

class ISection(IContentItem):
    """
    Represents a heading in a heading structure or 'section tree'.
    """
    
    items=List(
        title=_(u"Items"),
        description=_(u"Ordered list of content items that may include more SECTIONs or ENTRYs."),
	value_type=Object(schema=IContentItem),
        required=False,
    )
    
    
    
