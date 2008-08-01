# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

These are the interface specifications from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = u'Renato Pesca <rpesca@gmail.com>'

from zope.schema.interfaces import IContainer
from zope.schema import List,Object
from zope.i18nmessageid import MessageFactory

from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime
from oship.openehr.rm.support.identification.interfaces.hierobjectid import IHierObjectId
from oship.openehr.rm.support.identification.interfaces.objectref import IObjectRef

_ = MessageFactory('oship')

class IEhr(IContainer):
    """
    Root EHR container
    """
    
    systemId=Object(
        schema=IHierObjectId,
        title=_(u"System Id"),
        description=_(u"Id of system where this EHR was created."),
        required=True,
    )
    
    ehrId=Object(
        schema=IHierObjectId,
        title=_(u"EHR ID"),
        description=_(u"Id of this EHR."),
        required=True,
    )
    
    timeCreated=Object(
        schema=IDvDateTime,
        title=_(u"Created"),
        description=_(u"Creation data/time"),
        required=True,
    )
    
    contributions=List(
        title=_(u"Contributions"),
        description=_(u"List of contributions causing changes to this EHR."),
	value_type=Object(schema=IObjectRef),
        required=True,
    )
    
    ehrAccess=Object(
        schema=IObjectRef,
        title=_(u"EHR Access"),
        description=_(u"A reference to the EHR Access object."),
        required=True,
    )
    
    ehrStatus=Object(
        schema=IObjectRef,
        title=_(u"EHR Status"),
        description=_(u"A reference to the EHR Status object."),
        required=True,
    )
    
    directory=Object(
        schema=IObjectRef,
        title=_(u"Directory"),
        description=_(u"Optional directory structure."),
        required=False,
    )
    
    compositions=List(
        title=_(u"Compositions"),
        description=_(u"Master list of all compositions references."),
	value_type=Object(schema=IObjectRef),
        required=True,
    )
