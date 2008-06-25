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

from openehr.rm.datastructures.itemstructure.itemstructure import ItemStructure
from entry import IEntry
from openehr.rm.support.identification.objectref import ObjectRef

_ = MessageFactory('oship')

class ICareEntry(IEntry):
    u"""
            The abstract parent of all clinical ENTRY subtypes. A CARE_ENTRY defines 
            protocol and guideline attributes for all clinical Entry subtypes.

    """

    protocol = ItemStructure(
        title=u"""protocol""",
        description=u"""Description of the method (i.e. how) the information in this 
                    entry was arrived at. For OBSERVATIONs, this is a description of the
                    method or instrument used. For EVALUATIONs, how the evaluation was 
                    arrived at. For INSTRUCTIONs, how to execute the Instruction. 
                    This may take the form of references to guidelines, including 
                    manually followed and executable; knowledge references such as a
                    paper in Medline; clinical reasons within a largercare process.""",
        required=False
    )
    
    guidelineId = ObjectRef(
        title=u"""guidelineId""",
        description=u"""Optional external identifier of guideline creating this 
                    action if relevant.""",
        required=False
    )
    
    