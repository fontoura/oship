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
import os
import grok

def CreatMSW():
    """ read the file and return a code structure"""
    
    mswfile=open(os.getcwd()+"/src/oship/msw/MSW3.csv",'r')
    linecnt=0
    mswdict={}
    keytest={}
    keylist=[]
    mammal={}
    for line in mswfile.readlines():
        line=line.replace('[','<')
        line=line.replace(']','>')
        mswlist= unicode(line,'latin1').split(';')
        if linecnt == 0:  # headers
            headlist=mswlist
            mswlist=[]
            linecnt+=1
        else:
            unikey=mswlist[5] # Mammal Code
            print linecnt, "Processing Mammal Code - ", unikey
            for x in headlist:
                mswdict[x]=mswlist[headlist.index(x)]
                mammal[unikey]=mswdict
            linecnt+=1
                
    return mammal    
        
if __name__ == '__main__':
    CreatMSW()
    
    
