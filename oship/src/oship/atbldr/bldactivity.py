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

from blditemtree import bldItemTree
from openehr.rm.ehr.composition.content.entry.activity import Activity
from openehr.rm.datatypes.encapsulated.dvparsable import DvParsable

#called from bldInstruction
def bldActivity(activities,errlog,ontology):
    actObj=None
    description=None
    timing=''
    actionArchetypeId=[]
    
    if activities==None or activities==[]:
        errlog.write("\nERROR:No Activities list in Instruction")
        print "\nERROR:No Activities list in Instruction"
        return
    
    cardinality=(activities[2],activities[4])
    order=activities[5]
    archetypeNodeId=activities[6].strip('ACTIVITY')

    for y,x in enumerate(activities):
        if x == 'description':
            description=mkdescr(activities[y:len(activities)])
        elif x == 'allow_archetype':
            allow_archetype=activities[y+1]
            
    
    #print cardinality
    #print order
    #print nodeid
    #print description
    
    actObj=Activity(description,timing,actionArchetypeId,archetypeNodeId)
    #print '\nactlist=',activities
    #print "actObj: ",actObj
    return actObj

def mkdescr(desclist):
    descrObj=None
    valid=False
    #print 'description: ',desclist
    for y,x in enumerate(desclist):
        if isinstance(x,unicode) and 'ITEM_TREE' in x:
            descrObj=bldItemTree(desclist[y:len(desclist)])
            valid=True
            
    if not valid:
        print "\nUnknown Data Type for Description",desclist
        return None

    #print descrObj
    
    return descrObj
        