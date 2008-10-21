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
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

from zope.schema import Field,TextLine
from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class TerminologyAccess(Field):
    u"""
    Defines an object providing proxy access to a terminology.
    """
    
    id_ = TextLine(
        description=_(u'Identification of this Terminology'),
        required = True,
        )
    
    def allCodes():
        u""" Return all codes known in this terminology """
        
    def codesForGroupId(group_id):
        u"""
        Return all codes under grouper 'group_id' from this terminology
        """

    def hasCodeForGroupId(group_id, a_code):
        u"""
        True if 'a_code' is known in group 'group_id' in the openEHR terminology.
        """

    def codesForGroupName(name, lang):
        u"""
        Return all codes under grouper whose name in 'lang' is 'name' from this terminology
        """

    def rubricForCode(code, lang):
        u"""
        Return all rubric of code 'code' in language 'lang'.
        """

    def idExists():
        u""" True if id != None and id != '' """
