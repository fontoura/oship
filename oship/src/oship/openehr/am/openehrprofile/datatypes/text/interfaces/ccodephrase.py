# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
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

from zope.interface import Interface
from zope.schema import List,TextLine
from zope.i18nmessageid.message import MessageFactory 

from openehr.am.archetype.constraintmodel.interfaces.cdomaintype import ICDomainType
from openehr.rm.support.identification.interfaces.terminologyid import ITerminologyId

_ = MessageFactory('oship')

class ICCodePhrase(ICDomainType):
    u"""
    Express constraints on instances of CODE_PHRASE. The terminology_id attribute
    may be specified on its own to indicate any term from a specified terminology;
    the code_list attribute may be used to limit the codes to a specific list.
    """
    
    terminologyId = Object(
        schema=ITerminologyId,
        title=_(u"Terminology ID"),
        description=_(u"""Syntax string expressing constraint on allowed primary terms."""),
        required=False,
        )

    codeList = List(
        value_type=TextLine(),
        title=_(u"Code List"),
        description=_(u"""List of allowed codes.  If empty it means any code is allowed."""),
        required=False,
    )
    
    