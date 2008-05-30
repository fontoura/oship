# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Defines the interfaces for the definition package in support_im.pdf Rev. 1.6.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__version__ = '1.0.1a1'
__contributors__ = ''

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

class IBasicDefinitions(IField):
    """ Defines globally used constant values. """
    
    cr = TextLine(
        title=u"CR",
        description=u"Carriage Return Character",
        default=u"\015",
        readonly=True,
        )
    
    
    lf = TextLine(
        title=u"LF",
        description=u"Line Feed Character",
        default=u"\012",
        readonly=True,
        )


class IOpenehrDefinitions(IBasicDefinitions):
    """ Inheritance class to provide access to constants defined in other packages."""
    
