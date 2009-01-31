# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.i18nmessageid.message import MessageFactory 

_ = MessageFactory('oship')


class OpenehrCodeSetIdentifiers():
    u""" 
    List of identifiers for code sets in the openEHR terminology. 
    """

    CodeSetIdCharacterSets='character sets'
    CodeSetIdCompressionAlgorithms='compression algorithms'
    CodeSetIdCountries='countries'
    CodeSetIdIntegrityCheckAlgorithms='integrity check algorithms'
    CodeSetIdLanguages='languages'
    CodeSetIdMediaTypes='media types'
    CodeSetIdNormalStatuses='normal statuses'
    values=(CodeSetIdCharacterSets, CodeSetIdCompressionAlgorithms, CodeSetIdCountries, CodeSetIdIntegrityCheckAlgorithms, CodeSetIdLanguages, CodeSetIdMediaTypes, CodeSetIdNormalStatuses)
    
def validCodeSetId(anId):
    u"""
    Boolean Validity function to test if an identifier is in 
    the tuple defined by class OpenehrCodeSetIdentifiers.
    """
    return anId in OpenehrCodeSetIdentifiers.values
