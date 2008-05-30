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


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class ISection(IContentItem):
    """
    Represents a heading in a heading structure or 'section tree'.
    """
    
    items=List(
        title=_("Items"),
        description=_("Ordered list of content items that may include more SECTIONs or ENTRYs."),
        required=False,
    )
    
    
    