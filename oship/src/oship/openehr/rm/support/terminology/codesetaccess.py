# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the terminology package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements,classProvides
from zope.i18nmessageid.message import MessageFactory 

from interfaces.codesetaccess import ICodeSetAccess

_ = MessageFactory('oship')

class CodeSetAccess(object):
    """
    Defines an object providing proxy access to a code_set.
    """

    implements(ICodeSetAccess)
    classProvides(ICodeSetAccess)

    def id():
        u"""External identifier of this Code Set"""
    
    def allCodes():
        u""" Return all codes known in this code set """
        
    def hasLang(a_lang):
        u""" True if code set knows about 'a_lang' """
        
    def hasCode(a_code):
        u""" True if code set knows about 'a_code' """
        
    def idValid():
        u""" True if id != None and id != ''  """
        
