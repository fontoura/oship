# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates in memory archetype objects from ADL files and stores them in the ZODB.        
        Parsing is performed in adl_1_4.py using Pyparsing. 
        
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from bldhistory import bldHistory
from openehr.rm.ehr.composition.content.entry.observation import Observation

def bldObservation(parsed_adl,ontology):
        dataObj=bldHistory(parsed_adl.definition[0]['body'][0][0][1][0][0],'')
        stateObj=''
        obsObj=Observation(dataObj,stateObj)
        
        return obsObj

        