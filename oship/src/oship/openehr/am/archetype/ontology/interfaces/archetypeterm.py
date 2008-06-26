# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
From the am.archetype.ontology package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.schema.interfaces import IField
from zope.schema import Dict,TextLine

class IArchetypeTerm(IField):
    """
    Representation of any coded entity in the archetype ontology.
    """
    
    code=TextLine(
        title_(u"Code"),
        description=_(u"Code of this term."),
        required=True,
    )

    items=Dict(
        title_(u"Items"),
        description=_(u"Hash of keys (text,description) and corresponding values."),
        required=False,
    )
    
    def keys(set):
        """
        List of all keys used in this term.
        """
 