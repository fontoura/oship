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

from bldactivity import bldActivity

def bldInstruction(parsed_adl,errlog,ontology):
    nodeid=parsed_adl.definition[0][0].strip('INSTRUCTION')
    if 'ACTIVITY' in parsed_adl.definition[0][2][0][0][3][0][0][0]:
        activities=parsed_adl.definition[0][2][0][0][3]
        actObj=bldActivity(activities,errlog,ontology)
    else:
        errlog.write("Unknown class: ",parsed_adl.definition[0][2][0][0][3][0][0][0])
    
    
    
    return parsed_adl.definition[0]

