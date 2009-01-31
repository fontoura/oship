# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the Data Stuctures Information Model
History Package Rev. 2.1.0.

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from event import Event
from interfaces.pointevent import IPointEvent 


_ = MessageFactory('oship')

class PointEvent(Event):
    u"""
    Defines a single point event in a series.
    """    
    
    implements(IPointEvent)
    
    pass
    
