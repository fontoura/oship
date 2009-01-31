# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the definition package in support_im.pdf Rev. 1.6.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.rm.support.definition.interfaces.basicdefinitions import IBasicDefinitions

_ = MessageFactory('oship')


class BasicDefinitions(object):
    """ Defines globally used constant values. """
    
    implements(IBasicDefinitions)
    
    def __init__(self):
        self.cr=u"\015"
        self.lf=u"\012"
        
        
