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
    if '[at' in elist[0]:
        archetypeNodeId=elist[0].strip('ELEMENT')
    else:
        archetypeNodeId=''
    print elist
    
    # What kind of element are we adding?
    if isinstance(elist[6],unicode):    
        if isinstance(elist[6],unicode) and u'DV_TEXT' in elist[6]:
            from openehr.rm.datatypes.text.dvtext import DvText
            elem=DvText('',[],'','',{},{})
        elif isinstance(elist[6],unicode) and u'C_DV_QUANTITY' in elist[6]:
            from openehr.rm.datatypes.text.codephrase import CodePhrase
            from openehr.am.openehrprofile.datatypes.quantity.cdvquantity import CDvQuantity
            elem=CDvQuantity([],CodePhrase('',''))
        elif isinstance(elist[6],unicode) and u'DV_CODED_TEXT' in elist[6]:
            from openehr.rm.datatypes.text.dvcodedtext import DvCodedText
            elem=DvCodedText({})
        elif isinstance(elist[6],unicode) and u'DV_BOOLEAN' in elist[6]:
            from openehr.rm.datatypes.basic.dvboolean import DvBoolean
            elem=DvBoolean(False)
        elif isinstance(elist[6],unicode) and u'DV_DATE_TIME' in elist[6]:
            from openehr.rm.datatypes.quantity.datetime.dvdatetime import DvDateTime
            elem=DvDateTime('')
        elif isinstance(elist[6],unicode) and u'DV_DURATION' in elist[6]:
            from openehr.rm.datatypes.quantity.datetime.dvduration import DvDuration
            elem=DvDuration('')        
        elif isinstance(elist[6],unicode) and u'DV_COUNT' in elist[6]:
            from openehr.rm.datatypes.quantity.dvcount import DvCount
            elem=DvCount(0)
        elif isinstance(elist[6],unicode) and u'DV_QUANTITY' in elist[6]:
            from openehr.rm.datatypes.quantity.dvquantity import DvQuantity
            elem=DvQuantity(0,'',0)
        else:
            print "\nUnknown Data Type for Element: ",elist[6]
            logging.error("Unknown Data Type for Element: "+repr(elist[6]))
            return None
    else:
        logging.error("Could not process this element: "+repr(elist))
        print "Could not process this element: "+repr(elist)
        
    elemObj=Element(elem,{},archetypeNodeId)
    
    return elemObj
