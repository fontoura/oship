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

from zope.schema.interfaces import IContainer


from openehr.rm.datastructures.interfaces.datastructure import IDataStructure
from openehr.rm.support.indentification import HeirObjectId
from openehr.rm.datastructures.representation import *


from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class IEhr(IContainer):
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
    
class IVersionedEhrAccess(IVersionedObject):
    """
    Version container for EHR Access instance.
    """
    
class IEhrAccess(ILocatable):
    """
    EHR-wide access control object. Contains all policies and rules for access to data in this EHR.
    """
        
    settings=AccessControlSettings(
        title=_("Settings"),
        description=_("Access control settings for this EHR."),
        required=False,
    )
    
    scheme=TextLine(
        title=_("Scheme"),
        description=_("Name of the access control scheme."),
        required=True,
    )
    
class IVersionedEhrStatus(IVersionedObject):
    """
    Version container for the EHR status instance.
    """
    
    
class IEhrStatus(ILocatable):
    """
    Instance providing various EHR wide status information.
    """
    
    subject=PartySelf(
        title=_("Subject"),
        description=_("The subject of this EHR."),
        required=True,
    )
     
    isQueryable=Bool(
        title=_("Queryable"),
        description=_("True if this EHR can be included in population wide queries."),
        required=True,
        default=True,
    )
    
    isModifiable=Bool(
        title=_("Modifiable"),
        description=_("True if this EHR can be written to."),
        required=True,
        default=True,
    )
    
    otherDetails=ItemStructure('',
        title=_("Other Details"),
        description=_("Any other details of the EHR summary."),
        required=False,
    )
    
class IVersionedComposition(IComposition):
    """
    Version controlled compsoition abstraction.
    """
    
    isPersistent=Bool(
        title=_("Persistent"),
        description=_("Indicates whether this compsoition set is persistent."),
        required=True,
        default=True,
    )
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
        