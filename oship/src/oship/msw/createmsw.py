# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2009, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates Python structures to convert the semi-colon delimited file into an object for the termserver.
"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'


import os
import grok

from zope.interface import Interface,implements
from zope.schema import Tuple, TextLine,Bool
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')
 

def CreatMSW():
    """ read the file and return a code structure"""
    
    
    vocab=[]

    mswfile=open(os.getcwd()+"/src/oship/msw/MSW3.csv",'r')
    
    linecnt=0
    for line in mswfile.readlines():
        line=line.replace('[','<')
        line=line.replace(']','>')
        mswlist= unicode(line,'latin1').split(';')
        if linecnt > 0:  # the zero line is the headers so we skip it.
            """ Create  a unique Id for each mammal from the class codes"""
            mswlist[5]=mswlist[7]+mswlist[9]+mswlist[11]+mswlist[13]+mswlist[15]+mswlist[17]+mswlist[19]+mswlist[21]+mswlist[23]+mswlist[25]
            vocab.append((mswlist[5],Mammal(mswlist))) # go build one mammal instance, append it to a list 
        linecnt+=1 
    
    return vocab   
    


class IMammal(Interface):
    """Interface for mammals"""
    
    popNamesPt=TextLine(
        title=_(u"Portuguese Popular Name"),
        description=_(u"Popular names in Portuguese")
    )
    genPopNPt=TextLine(
        title=_(u"Portuguese Popular Name"),
        description=_(u"Generic popular name in Portuguese")
    )
    popNamesEn=TextLine(
        title=_(u"English Popular Name"),
        description=_(u"Popular names in English")
    )
    genPopNEn=TextLine(
        title=_(u"English Popular Name"),
        description=_(u"Generic popular name in English")
    )
    risk=TextLine(
        title=_(u"Rabies Risk Factor"),
        description=_(u"Risk of rabies transmission (1 = high; 2 = moderate; 3 = none)")
    )
    codMam=TextLine(
        title=_(u"Unique Mammal Code"),
        description=_(u"Mammal code")
    )
    order=Tuple(
        title=_(u"Order"),
        description=_(u"A tuple consisting of the 'order' and the order code segment")
    )
    #cod01-Code fraction for order
    suborder=Tuple(
        title=_(u"Suborder"),
        description=_(u"A tuple consisting of the 'suborder' and the suborder code segment")
    )
    #cod02-Code fraction for suborder
    infraOrder=Tuple(
        title=_("InfraOrder"),
        description=_("A tuple consisting of the 'infraorder' and the infraorder code segment")
    )
    #cod03-Code fraction for infraorder
    superFamily=Tuple(
        title=_("Super Family"),
        description=_("A tuple consisting of the 'superfamily' and the superfamily code segment")
    )
    #cod04-Code fraction for superfamily
    family=Tuple(
        title=_("Family"),
        description=_("A tuple consisting of the 'family' and the family code segment")
    )
    #cod05-Code fraction for family
    subFamily=Tuple(
        title=_(u"Subfamily"),
        description=_(u"A tuple consisting of the 'subfamily' and the subfamily code segment")
    )
    #cod06-Code fraction for subfamily
    tribe=Tuple(
        title=_(u"Tribe"),
        description=_(u"A tuple consisting of the 'tribe' and the tribe code segment")
    )
    #cod07-Code fraction for tribe
    genre=Tuple(
        title=_(u"Genre"),
        description=_(u"A tuple consisting of the 'genre' and the genre code segment")
    )
    #cod08-Code fraction for genre
    subGenre=Tuple(
        title=_(u"Subgenre"),
        description=_(u"A tuple consisting of the 'subgenre' and the subgenre code segment")
    )
    #cod09-Code fraction for subgenre
    species=Tuple(
        title=_(u"Species"),
        description=_(u"A tuple consisting of the 'species' and the species code segment")
    )
    #cod10-Code fraction for species
    
    
    #popNamePt01-(not used in OSHIP)
    #popNamePt02-(not used in OSHIP)
    #popNamePt03-(not used in OSHIP)
    #popNameEn01-(not used in OSHIP)
    #popNameEn02-(not used in OSHIP)
    #popNameEn03-(not used in OSHIP)
    #popNameEn04-(not used in OSHIP)

    
    linkWikiEn=TextLine(
        title=_(u"WWW Link"),
        description=_(u"Link for the mammal on Wikipedia or alternative sites")
    )
    stdLink=Bool(
        title=_(u"Standard Link"),
        description=_(u"If TRUE then this is a Wikipedia link.")
    )
    
    #seqId-(not used in OSHIP)
    #count-(not used in OSHIP)

class Mammal(grok.Model):
    """Mammals in the terminology"""
    
    implements(IMammal)
    
    def __init__(self,mswlist):
        
        popNamesPt=mswlist[0]
        genPopNPt=mswlist[1]
        popNamesEn=mswlist[2]
        genPopNEn=mswlist[3]
        risk=mswlist[4]
        codMam=mswlist[5]
        order=Tuple(
            title=_("Order"),
            description=_("A tuple consisting of the 'order' and the order code segment")
        )
        order=(mswlist[7],mswlist[6])
        #cod01
        suborder=(mswlist[9],mswlist[8])
        #cod02
        infraOrder=(mswlist[11],mswlist[10])

        #cod03
        superFamily=(mswlist[13],mswlist[12])

        #cod04
        family=(mswlist[15],mswlist[14])

        #cod05
        subFamily=(mswlist[17],mswlist[16])

        #cod06
        tribe=(mswlist[19],mswlist[18])
        #cod07
        genre=(mswlist[21],mswlist[20])        
        #cod08
        subGenre=(mswlist[23],mswlist[22])
        #cod09
        species=(mswlist[25],mswlist[24])
        #cod10
        #popNamePt01
        #popNamePt02
        #popNamePt03
        #popNameEn01
        #popNameEn02
        #popNameEn03
        #popNameEn04
        linkWikiEn=mswlist[34]
        stdLink=bool(int(mswlist[35]))
        #seqId
    

    
