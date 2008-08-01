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
import logging
import datetime

from oship.openehr.rm.datastructures.itemstructure.representation.element import Element


def bldElement(elist):
    typeDict={
        u'DV_TEXT':mkDvText,
        u'DV_DATE':mkDvDate,
        u'C_DV_QUANTITY':mkCDvQuantity,
        u'DV_CODED_TEXT':mkDvCodedText,
        u'DV_BOOLEAN':mkDvBoolean,
        u'DV_DATE_TIME':mkDvDateTime,
        u'DV_DURATION':mkDvDuration,
        u'DV_COUNT':mkDvCount,
        u'DV_INTERVAL':mkDvInterval,
        u'DV_QUANTITY':mkDvQuantity,
        u'DV_URI':mkDvUri
        }
        
    elem=None
    
    # What kind of element are we adding?
    print '\nElement List:',elist
    for a in elist:
        if typeDict.has_key(a):    
            elem=typeDict[a](elist)
            print "Making: ",a
            break                          
                          
    if '[at' in elist[0]:
        archetypeNodeId=elist[0].strip('ELEMENT')
    else:
        archetypeNodeId=''
        
    elemObj=Element(elem,{},archetypeNodeId,'','','','','')
    
    return elemObj

def mkDvText(elist):
    from oship.openehr.rm.datatypes.text.dvtext import DvText
    elem=DvText('',[],'','',{},{})
    
def mkDvDate(elist):
    from oship.openehr.rm.datatypes.quantity.datetime.dvdate import DvDate
    elem=DvDate((datetime.date.today()).isoformat()) # today as an ISO string   
    
def mkCDvQuantity(elist):
    from oship.openehr.rm.datatypes.text.codephrase import CodePhrase
    from oship.openehr.am.openehrprofile.datatypes.quantity.cdvquantity import CDvQuantity
    elem=CDvQuantity([],CodePhrase('',''))    
    
def mkDvCodedText(elist):
    from oship.openehr.rm.datatypes.text.dvcodedtext import DvCodedText
    elem=DvCodedText({})    
    
def mkDvBoolean(elist):
    from oship.openehr.rm.datatypes.basic.dvboolean import DvBoolean
    elem=DvBoolean(False)    
    
def mkDvDateTime(elist):
    from oship.openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime
    elem=DvDateTime((datetime.datetime.today()).isoformat()) # now as an ISO string 
    
def mkDvDuration(elist):
    from oship.openehr.rm.datatypes.quantity.datetime.dvduration import DvDuration
    elem=DvDuration('')     
    
def mkDvCount(elist):
    from oship.openehr.rm.datatypes.quantity.dvcount import DvCount
    elem=DvCount(0)
    
def mkDvInterval(elist):
    from oship.openehr.rm.datatypes.quantity.dvinterval import DvInterval
    elem=DvInterval(0,0)
    
def mkDvQuantity(elist):
    from oship.openehr.rm.datatypes.quantity.dvquantity import DvQuantity
    elem=DvQuantity(0,'',0)
     
def mkDvUri(elist):
    from oship.openehr.rm.datatypes.uri.dvuri import DvUri
    elem=DvUri('')



