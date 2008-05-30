# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
The text data types. From the data types specification Rev 2.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.schema import Field
from zope.i18nmessageid.message import MessageFactory

from openehr.rm.datatypes.interfaces.itermmapping import ITermMapping

class TermMapping(Field):
    """
    Represents a coded term mapped to a DV_TEXT, and the relative match of the tar-
    get term with respect to the mapped item. Plain or coded text items may appear in
    the EHR for which one or mappings in alternative terminologies are required.
    Mappings are only used to enable computer processing, so they can only be
    instances of DV_CODED_TEXT.
    
    Used for adding classification terms (e.g. adding ICD classifiers to SNOMED
    descriptive terms), or mapping into equivalents in other terminologies (e.g.
    across nursing vocabularies).
    """

    implements(ITermMapping)
    
    def __init__(self,target,match,purpose):
        self.target = target       
        self.purpose = purpose
        if match in ['<','>','=','?']:
            self.match = match
        else:
            raise AttributeError, "Invalid match parameter"
        
        
    def narrower():
        return self.match == '<'
    
    def equivalent():
        return self.match == '='
    
    def broader():
        return self.match == '>'
    
    def unknown():
        return self.match == '?'
    
    def isValidMatchCode():
        " I see no purpose in this function. twc"
        return match in ['<','>','=','?']
