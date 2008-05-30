# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

These are the interfaces for the encapsulated data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import Int,TextLine

from openehr.rm.datatypes.interfaces.idvencapsulated import IDvEncapsulated

_ = MessageFactory('oship')
            
class IDvParasable(IDvEncapsulated):
    """
    Encapsulated data expressed as a parsable String. The internal model of the data item is not 
    described in the openEHR model in common with other encapsulated types, but in this case, the 
    form of the data is assumed to be plaintext, rather than compressed or other types of large binary data.
    Used for representing values which are formal textual representations, e.g. guidelines.
    """

    size=Int(
        title=_(u"Size"),
        description=_(""" """),
        required=True,
        )

    value = TextLine(
        title=_(u"Value"),
        description=_(u"""The string, which may validly be empty in some syntaxes"""),
        required=True,
        )
    
    formalism = TextLine(
        title=_(u"Formalism"),
        description=_(u"""The name of the formalism, e.g. “GLIF 1.0”, “proforma” etc."""),
        required=True,
        )
    
    def valueValid():
        """value != None."""

    def formalismValidity():
        """formalism != None and formalism != '' """
        
