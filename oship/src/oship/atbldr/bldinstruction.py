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

from datetime import datetime

from openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime
from openehr.rm.datatypes.text.dvtext import DvText
from openehr.rm.datatypes.encapsulated.dvparsable import DvParsable
from openehr.rm.ehr.composition.content.entry.instruction import Instruction

from bldactivity import bldActivity
from oship.utils.flatten import flatten

def bldInstruction(parsed_adl,errlog,ontology):
    definList=[]
    definObj=None
    
    #turn the parsed definition into a list with all strings converted to unicode
    flat_adl = flatten(parsed_adl.definition)
    for x in flat_adl:
        if isinstance(x,str):
            x=unicode(x)
            
        definList.append(x)
        
    #print definList
    
    #What is in an INSTRUCTION?    
    #narrative
    txtval=''
    map=[]
    fmt=''
    uri=''
    lang=''
    encode=''
    narrative=DvText(txtval,fmt,map,uri,lang,encode)
    
    # Activities
    actList=[]
    if 'activities' in definList[4]:
        actList=definList[4:]

    
    activities=bldActivity(actList,errlog,ontology) # list of activities

    #expires
    expires=datetime.isoformat(datetime.now())
    expiry_time=DvDateTime(expires) # Datetime string

    # workflow
    wf_definition=DvParsable(0,'','')
    
    nodeid = definList[0].strip('INSTRUCTION')
    
    # create the definition object for this Instruction archetype
    definObj=Instruction(narrative,activities,expiry_time,wf_definition,nodeid) 
    
    return definObj

