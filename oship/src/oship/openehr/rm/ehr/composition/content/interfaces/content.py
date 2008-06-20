# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications for the content package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from oship.openehr.rm.data_structures.interfaces import IDataStructure

from oship.openehr.rm.support.indentification import HeirObjectId

from oship.openeh.rm.data_strutures.representation import *


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class IContentItem(IContainer):
    """
    Abstract ancestor of all concrete content types.
    """
    