# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The Archetype Profile basic package. 
From the openEHR Archetype Profile specifications Rev. 1.0.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import Interface
from zope.schema import TextLine
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')

class IState(Interface):
    """        
    Abstract definition of one state in a state machine.
    """

    name = TextLine(
        title=_(u"Name"),
        description=_(u"""Name of this State."""),
        required=False,
        )
    
    
