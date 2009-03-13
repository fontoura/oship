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
    
    
    vocab=grok.Container()

    mswfile=open(os.getcwd()+"/src/oship/msw/MSW3.csv",'r')
    
    linecnt=0
    for line in mswfile.readlines():
        line=line.replace('[','<')
        line=line.replace(']','>')
        mswlist= unicode(line,'latin1').split(';')
        if linecnt > 0:  # the zero line is the headers so we skip it.
            vocab[mswlist[5]]=Mammal(mswlist) # go build one mammal instance
            print lintcnt, vocab[mswlist[5]]
            linecnt+=1 
        
    
    return(vocab)   
    
    
    # this commented section is the pre-grok version.
    #linecnt=0
    #mswdict={}
    #keytest={}
    #keylist=[]
    #mammal={}
    #for line in mswfile.readlines():
        #line=line.replace('[','<')
        #line=line.replace(']','>')
        #mswlist= unicode(line,'latin1').split(';')
        #if linecnt == 0:  # headers
            #headlist=mswlist
            #print headlist
            #mswlist=[]
            #linecnt+=1
        #else:
            #unikey=mswlist[5] # Mammal Code
            #print linecnt, "Processing Mammal Code - ", unikey
            #for x in headlist:
                #mswdict[x]=mswlist[headlist.index(x)]
                #mammal[unikey]=mswdict
            #linecnt+=1
                
    #return mammal    


class IMammal(Interface):
    """Interface for mammals"""
    
    popNamesPt=TextLine(
        title=_("Portuguese Popular Name"),
        description=_(" ")
    )
    genPopNPt=TextLine(
        title=_("Portuguese Popular Name"),
        description=_(" ")
    )
    popNamesEn=TextLine(
        title=_("English Popular Name"),
        description=_(" ")
    )
    genPopNEn=TextLine(
        title=_("English Popular Name"),
        description=_(" ")
    )
    risk=TextLine(
        title=_("Rabies Risk Factor"),
        description=_(" ")
    )
    codMam=TextLine(
        title=_("Unique Mammal Code"),
        description=_(" ")
    )
    order=Tuple(
        title=_("Order"),
        description=_("A tuple consisting of the 'order' and the order code segment")
    )
    #cod01
    suborder=Tuple(
        title=_("Suborder"),
        description=_("A tuple consisting of the 'suborder' and the suborder code segment")
    )
    #cod02
    infraOrder=Tuple(
        title=_("InfraOrder"),
        description=_("A tuple consisting of the 'infraorder' and the infraorder code segment")
    )
    #cod03
    superFamily=Tuple(
        title=_("Super Family"),
        description=_("A tuple consisting of the 'superfamily' and the superfamily code segment")
    )
    #cod04
    family=Tuple(
        title=_("Family"),
        description=_("A tuple consisting of the 'family' and the family code segment")
    )
    #cod05
    subFamily=Tuple(
        title=_("Subfamily"),
        description=_("A tuple consisting of the 'subfamily' and the subfamily code segment")
    )
    #cod06
    tribe=Tuple(
        title=_("Tribe"),
        description=_("A tuple consisting of the 'tribe' and the tribe code segment")
    )
    #cod07
    genre=Tuple(
        title=_("Genre"),
        description=_("A tuple consisting of the 'genre' and the genre code segment")
    )
    #cod08
    subGenre=Tuple(
        title=_("Subgenre"),
        description=_("A tuple consisting of the 'subgenre' and the subgenre code segment")
    )
    #cod09
    species=Tuple(
        title=_("Species"),
        description=_("A tuple consisting of the 'species' and the species code segment")
    )
    #cod10
    #popNamePt01
    #popNamePt02
    #popNamePt03
    #popNameEn01
    #popNameEn02
    #popNameEn03
    #popNameEn04
    linkWikiEn=TextLine(
        title=_("WWW Link"),
        description=_(" ")
    )
    stdLink=Bool(
        title=_("Standard Link"),
        description=_("If TRUE then this is a Wikipedia link.")
    )
    #seqId

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
        #cod01
        suborder=(mswlist[7],mswlist[6])
        #cod02
        infraOrder=(mswlist[9],mswlist[8])

        #cod03
        superFamily=(mswlist[11],mswlist[10])

        #cod04
        family=(mswlist[13],mswlist[12])

        #cod05
        subFamily=(mswlist[15],mswlist[14])

        #cod06
        tribe=(mswlist[17],mswlist[16])
        #cod07
        genre(mswlist[19],mswlist[18])        
        #cod08
        subGenre=(mswlist[21],mswlist[20])
        #cod09
        species=(mswlist[23],mswlist[22])
        #cod10
        #popNamePt01
        #popNamePt02
        #popNamePt03
        #popNameEn01
        #popNameEn02
        #popNameEn03
        #popNameEn04
        linkWikiEn=mswlist[31]
        stdLink=bool(mswlist[32])
        #seqId
    

    
