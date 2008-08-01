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

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from interfaces.openehrterminologygroupidentifiers import IOpenehrTerminologyGroupIndentifiers

_ = MessageFactory('oship')
       
class OpenehrTerminologyGroupIndentifiers(object):
    """
    List of identifiers for groups in the openEHR terminology.
    """
    
    implements(IOpenehrTerminologyGroupIndentifiers)
    
    def validTerminologyGroupId(anId):
        u"""
        Validity function to test if an identifier is in the set defined by this class.
        """
        
