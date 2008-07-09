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

from openehr.rm.datatypes.text.dvtext import DvText
from openehr.rm.datastructures.itemstructure.representation.element import Element

def bldElement(elist,errlog):
    
    if '[' in elist[0]:
        archetypeNodeId=elist[0].strip('ITEM_TREE')
    else:
        archetypeNodeId=''
     
    if 'DV_TEXT' in elist[6]:
        return DvText('',[],'','',{},{})
    else:
        errlog.write("Unknown Data Type for Element"+repr(elist[6]))
        print "Unknown Data Type for Element",elist[6]
        return None
