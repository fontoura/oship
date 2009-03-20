# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2009, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates Python structures to convert the | delimited file into an object for the termserver.
"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


import os
import grok

from zope.interface import Interface,implements
from zope.schema import Tuple, TextLine,Bool
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')
 

def CreateRxTerms():
    """ read the file and return a code structure"""
    
    
    vocab=[]
    release="RxTerms200903" #change this with each new update.
    
    rxfile=open(os.getcwd()+"/src/oship/rxterms/"+release+".txt",'r')
    print "Processing RxTerms Models. Please be patient ....."
    
    linecnt=0
    for line in rxfile.readlines():
        rxterm= unicode(line,'latin1').split('|')
        if linecnt > 0:  # the zero line is the headers so we skip it.
            rxcui=rxterm[0]
            genericRxcui=rxterm[1]
            tty=rxterm[2]
            fullName=rxterm[3]
            rxnDoseForm=rxterm[4]
            fullGenericName=rxterm[5]
            brandName=rxterm[6]
            displayName=rxterm[7]
            route=rxterm[8]
            newDoseForm=rxterm[9]
            strength=rxterm[10]
            suppressFor=rxterm[11]
            displayNameSynonym=rxterm[12]
            isRetired=rxterm[13]
            rxModel=RxTerm(rxcui,genericRxcui,tty,fullName,rxnDoseForm,fullGenericName,brandName,displayName,route,newDoseForm,strength,suppressFor,displayNameSynonym,isRetired)
            vocab.append((release,rxcui,rxModel))
        linecnt+=1 
    
    return vocab   
    


class IRxTerm(Interface):
    """Schema definition an RxTerm"""
    
    rxcui=TextLine(
        title=_(u"RXCUI"),
        description=_(U"""the RxNorm unique identifier for the clinical drug, which can be one of the following term types:
                        * Semantic Clinical Drug (SCD) e.g. Azithromycin 250 MG Oral Capsule.
                        * Semantic Branded Drug (SBD) e.g. Azithromycin 250 MG Oral Capsule [Zithromax].
                        * Branded Pack (BPCK) e.g. {6 (Azithromycin 250 MG Oral Tablet [Zithromax]) } Pack [Z-PAKS].""")
    )
    
    genericRxcui=TextLine(
        title=_(u"Generic RXCUI"),
        description=_(u"this is the corresponding generic clinical drug for SBD and BPCK (null for SCD).")
    )
    
    tty=TextLine(
        title=_(u"TTY"),
        description=_(u"""term type in RxNorm.""")
    )
    
    fullName=TextLine(
        title=_(u"Full Name"),
        description=_(u"""the full RxNorm name of the clinical drug.""")
    )
        
    rxnDoseForm=TextLine(
        title=_(u"RXN Dose Form"),
        description=_(u"dose form and intended route information from RxNorm.")
    )
    
    fullGenericName=TextLine(
        title=_(u"Full Generic Name"),
        description=_(u"""the generic part of the full RxNorm name.""")
    )
    
    brandName=TextLine(
        title=_(u"Brand Name"),
        description=_(u"""the brand name part of the full RxNorm name (null for SCD). 
                      Brand names are in all uppercase to distinguish them from generic names.""")
    )
    
    displayName=TextLine(
        title=_(u"Display Name"),
        description=_(u"""drug name (either generic or brand name) and intended route e.g. INDERAL (Oral-pill).""")
    )
    
    route=TextLine(
        title=_(u"Route"),
        description=_(u"""intended route derived from RXN_DOSE_FORM.""")
    )
    
    newDoseForm=TextLine(
        title=_(u"New Dose Form"),
        description=_(u"""dose form derived from RXN_DOSE_FORM.""")
    )
    
    strength=TextLine(
        title=_(u"Strength"),
        description=_(u"""strength information parsed from the RxNorm full name.""")
    )
    
    suppressFor=TextLine(
        title=_("Suppress For"),
        description=_(u"""to flag drug names deemed not likely to be useful for data entry. 
                      For example, long generic drug names with multiple ingredients 
                      (e.g. Bacitracin/Hydrocortisone/Neomycin/Polymyxin B) are suppressed because 
                      they are almost always prescribed by their brand names (e.g. CORTISPORIN OINTMENT). 
                      Any non-null value means that a row should be suppressed.""")
    )
    
    displayNameSynonym=TextLine(
        title=_("Display Name Synonym"),
        description=_(u"""commonly used synonyms or abbreviations for the drug e.g. MOM for Milk of Magnesia.""")
    )
    
    isRetired=TextLine(
        title=_(u"Is Retired"),
        description=_(u"""to flag records that existed in earlier versions but not in the latest version.""")
    )
    
    
class RxTerm(grok.Model):
    """
    The fields DISPLAY_NAME, DISPLAY_NAME_SYNONYM, NEW_DOSE_FORM and STRENGTH are probably the most useful. 
    We advise you to exclude rows that are suppressed or retired (i.e. rows with non-null values in 
    SUPPRESS_FOR or IS_RETIRED).
    """
            
    implements(IRxTerm)
    
    def __init__(self,rxcui,genericRxcui,tty,fullName,rxnDoseForm,fullGenericName,brandName,displayName,route,newDoseForm,strength,suppressFor,displayNameSynonym,isRetired):
        self.rxcui=rxcui
        self.genericRxcui=genericRxcui
        self.tty=tty
        self.fullName=fullName
        self.rxnDoseForm=rxnDoseForm
        self.fullGenericName=fullGenericName
        self.brandName=brandName
        self.displayName=displayName
        self.route=route
        self.newDoseForm=newDoseForm
        self.strength=strength
        self.suppressFor=suppressFor
        self.displayNameSynonym=displayNameSynonym
        self.isRetired=isRetired
        
        
        
        
        
        
        
    
    
