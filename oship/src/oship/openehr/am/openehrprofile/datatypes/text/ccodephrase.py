# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

The Archetype Profile text package. 
From the openEHR Archetype Profile specifications Rev. 1.0.0

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.i18nmessageid.message import MessageFactory 

from oship.openehr.am.archetype.constraintmodel.cdomaintype import CDomainType
from oship.openehr.am.openehrprofile.datatypes.text.interfaces.ccodephrase import ICCodePhrase

_ = MessageFactory('oship')

class CCodePhrase(CDomainType):
    u"""
    Express constraints on instances of CODE_PHRASE. The terminology_id attribute
    may be specified on its own to indicate any term from a specified terminology;
    the code_list attribute may be used to limit the codes to a specific list.
    """
    
    implements(ICCodePhrase)
    
 
    def __init__(self,termid,codelist):
        self.terminologyId=termid
        self.codeList=codelist
     
