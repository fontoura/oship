# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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

from zope.schema import TextLine
from zope.schema.interfaces import IField
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class IBasicDefinitions(IField):
    """ Defines globally used constant values. """
    
    cr = TextLine(
        title=_(u"CR"),
        description=_(u"Carriage Return Character"),
        readonly=True,
        )
    
    
    lf = TextLine(
        title=_(u"LF"),
        description=_(u"Line Feed Character"),
        readonly=True,
        )

