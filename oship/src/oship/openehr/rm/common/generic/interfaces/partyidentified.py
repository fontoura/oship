# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the generic package as described in the 
Common Information Model Rev. 2.1.0 

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.schema import TextLine,List,Object
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.common.generic.interfaces.partyproxy import IPartyProxy
from oship.openehr.rm.datatypes.basic.interfaces.dvidentifier import IDvIdentifier

_ = MessageFactory('oship')

    
class IPartyIdentified(IPartyProxy):
    u"""
    Proxy data for an identified party other than the subject of the record, 
    minimally consisting of human-readable identifier(s), such as name, formal 
    (and possibly computable) identifiers such as NHS number, and an optional 
    link to external data. There must be at least one of name, identifier or 
    external_ref present.
        
    Used to describe parties where only identifiers may be known, and there is 
    no entry at all in the demographic system (or even no demographic system). 
    Typically for health care providers, e.g. name and provider number of an 
    institution.

    Should not be used to include patient identifying information.
    """
    
    name = TextLine(
        title=_(u'Name'),
        description=_(u"""Optional human-readable name (in String form)."""),
        required=False,
        )
    
    identifiers = List(
        value_type=Object(schema=IDvIdentifier),
        title=_(u'Identifiers'),
        description=_(u"""One or more formal identifiers (possiblycomputable).
                    List<DvIdentifier>"""),
        required=False,
        )

    def basicValid(obj):
        u"""name None or identifiers != None or external_ref != None"""            
        
    def nameValid():
        u"""name != None and name != '' """
        
    def identifiersValid():
        u"""identifiers != none and identifiers != '' """
