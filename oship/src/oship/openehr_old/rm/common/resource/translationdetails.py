# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the resource package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
 
from zope.i18nmessageid import MessageFactory
from zope.interface import implements
from zope.schema import TextLine,Dict,Field

from oship.openehr.rm.datatypes.text.codephrase import CodePhrase
from interfaces.translationdetails import ITranslationDetails

_ = MessageFactory('oship')

class TranslationDetails(object):
    u""" """
    
    implements(ITranslationDetails)
    
    def __init__(self,lang,author,accred,other):
        self.language=lang
        self.author=author
        self.accreditation=accred
        self.otherDetails=other
   
