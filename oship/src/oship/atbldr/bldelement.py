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

from openehr.rm.datastructures.itemstructure.representation.element import Element

#called from bldCluster
def bldElement(elist):
    elem=None
    elemObj=None
    if '[' in elist[0]:
        archetypeNodeId=elist[0].strip('ELEMENT')
    else:
        archetypeNodeId=''
     
    if u'DV_TEXT' in elist[6]:
        from openehr.rm.datatypes.text.dvtext import DvText
        elem=DvText('',[],'','',{},{})
    elif u'DV_CODED_TEXT' in elist[6]:
        from openehr.rm.datatypes.text.dvcodedtext import DvCodedText
        elem=DvCodedText({})
    elif u'DV_DATE_TIME' in elist[6]:
        from openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime
        elem=DvDateTime('')
    elif u'DV_DURATION' in elist[6]:
        from openehr.rm.datatypes.quantity.datetime.dvduration import DvDuration
        elem=DvDuration('')        
    elif u'DV_COUNT' in elist[6]:
        from openehr.rm.datatypes.quantity.dvcount import DvCount
        elem=DvCount(0)
    elif u'DV_QUANTITY' in elist[6]:
        from openehr.rm.datatypes.quantity.dvquantity import DvQuantity
        elem=DvQuantity(0,'',0)
    elif u'C_DV_QUANTITY' in elist[6]:
        from openehr.am.archetype.openehrarchetypeprofile.quantity.cdvquantity import CDvQuantity
        elem=CDvQuantity()
    else:
        print '\nElement List: ',elist
        print "\nUnknown Data Type for Element: ",elist[6]
        return None
    
    elemObj=Element(elem,{},archetypeNodeId)
    
    return elemObj
