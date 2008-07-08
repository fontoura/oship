# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

These are the interface specifications from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements,classProvides
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.archetyped.locatable import Locatable

_ = MessageFactory('oship')

    
class EhrStatus(Locatable):
    """
    Instance providing various EHR wide status information.
    """
    
    pass
