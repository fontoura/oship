# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

The interface specifications for the entry package from openEHR 
EHR Information Model package Rev. 5.1.0

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__Contributors__ = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import List,Object

from oship.openehr.rm.datatypes.text.interfaces.dvtext import IDvText
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvdatetime import IDvDateTime
from oship.openehr.rm.datatypes.encapsulated.interfaces.dvparsable import IDvParsable
from oship.openehr.rm.ehr.composition.content.entry.interfaces.activity import IActivity
from oship.openehr.rm.ehr.composition.content.entry.interfaces.careentry import ICareEntry

_ = MessageFactory('oship')

class IInstruction(ICareEntry):
    """
    Used to specify future actions and includes a workflow form.
    """
    
    narrative=Object(
        schema=IDvText,
        title=_(u"Narrative"),
        description=_(u"Human readable version of the Instructions."),
        required=True,
    )
    
    activities=List(
        value_type = Object(schema = IActivity),
        title=_(u"Activities"),
        description=_(u"List of all activities in the Instruction."),
        required=False,
    )
    
    expiryTime=Object(
        schema=IDvDateTime,
        title=_(u"Expiry Time"),
        description=_(u"Data/time when this Instruction can be assumed to have expired."),
        required=False,
    )
    
    wfDefinition=Object(
        schema=IDvParsable,
        title=_(u"Workflow Definition"),
        description=_(u"Workflow engine executable expression of the Instruction."),
        required=False,
    )
    
 
