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
from oship.utils.flatten import flatten

def bldInstruction(parsed_adl,errlog,ontology):
    definList=[]
    definObj=None
    
    #turn the parsed definition section into a list with all strings converted to unicode
    flat_adl = flatten(parsed_adl.definition)
    for x in flat_adl:
        if isinstance(x,str):
            x=unicode(x)
            
        definList.append(x)
        
    print definList
    print 'Len definList:',len(definList)
    
    #What is possible in an INSTRUCTION?
    
    nodeid = definList[0].strip('INSTRUCTION')
    print nodeid
       
    return definObj

