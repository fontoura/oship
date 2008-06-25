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
__docformat__ = 'plaintext'


from zope.i18nmessageid import MessageFactory
from zope.schema import List

from openehr.rm.datatypes.text.dvtext import DvText
from openehr.rm.datatypes.quantity.datetm.dvdatetime import DvDateTime
from openehr.rm.datatypes.encapsulated.dvparsable import DvParasable
from careentry import ICareEntry

_ = MessageFactory('oship')

class IInstruction(ICareEntry):
    """
    Used to specify future actions and includes a workflow form.
    """
    
    narrative=DvText('',
        title_("Narrative"),
        description=_("Human readable version of the Instructions."),
        required=True,
    )
    
    activities=List(
        title=_("Activities"),
        description=_("List of all activities in the Instruction."),
        required=False,
    )
    
    expiryTime=DvDateTime('',
        title=_("Expiry Time"),
        description=_("Data/time when this Instruction can be assumed to have expired."),
        required=False,
    )
    
    wfDefinition=DvParsable(
        title=_("Workflow Definition"),
        description=_("Workflow engine executable expression of the Instruction."),
        required=False,
    )
    
 
