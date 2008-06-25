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

from zope.interface import implements
from zope.schema import Container
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class Ehr(Container):
    """
    Root EHR container
    """
    
    systemId=HeirObjectId('',
        title=_("System Id"),
        description=_("Id of system where this EHR was created."),
        required=True,
    )
    
    ehrId=HeirObjectId('',
        title=_("EHR ID"),
        description=_("Id of this EHR."),
        required=True,
    )
    
    timeCreated=DvDateTime('',
        title=_("Created"),
        description=_("Creation data/time"),
        required=True,
    )
    
    contributions=List(
        title=_("Contributions"),
        description=_("List of contributions causing changes to this EHR."),
        required=True,
    )
    
    ehrAccess=ObjectRef(
        title=_("EHR Access"),
        description=_("A reference to the EHR Access object."),
        required=True,
    )
    
    ehrStatus=ObjectRef(
        title=_("EHR Status"),
        description=_("A reference to the EHR Status object."),
        required=True,
    )
    
    directory=ObjectRef(
        title_("Directory"),
        description=_("Optional directory structure."),
        required=False,
    )
    
    compositions=List(
        title=_("Compositions"),
        description=_("Master list of all compositions references."),
        required=True,
    )
