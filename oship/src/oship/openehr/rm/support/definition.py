# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

Implementation for the definition package in support_im.pdf Rev. 1.6.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__version__ = '1.0.1a1'
__contributors__ = ''

from zope.interface import implements
from zope.schema import Text, TextLine, Field

class BasicDefinitions(Field):
    """ Defines globally used constant values. """
    
    implements(IBasicDefinitions)

class OpenehrDefinitions(BasicDefinitions):
    """ Inheritance class to provide access to constants defined in other packages."""
    
    implements(IOpenehrDefinitions)