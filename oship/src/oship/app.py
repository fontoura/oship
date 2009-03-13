# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

import grok
from zope.exceptions import DuplicationError
from zope.i18nmessageid import MessageFactory
from zope.app.container.btree import BTreeContainer
from zope.app.folder import Folder
from oship.openehr.atbldr import CreateAT, getFileList
from oship.msw.createmsw import CreatMSW

# Begin OSHIP Demo
class oship(grok.Application, grok.Container ):
    pass

class Index(grok.View):
    grok.context(oship)


class Setup(grok.View):
    grok.context(oship)
    
    def render(self):
        try:
            self.context['ar'] = grok.Container() # archetype repository
            self.context['termserver'] = grok.Container() # terminology server
        except DuplicationError:
            pass
        
        fnames = getFileList()
        try:        
            for fname in fnames: # we have our list of ADL files
                print "Processing: ",fname
                
                at=CreateAT(fname) # take one ADL file and process it into a mapping

                atname=at[0]
                
                self.context['ar'][atname]=at[1]
        except DuplicationError:
            pass
         
        
        self.redirect("http://localhost:8080/oship") # now simply redirect to the main page
            
class Emptyar(grok.View):
    """Remove all the archetypes in the repository"""
    
    grok.context(oship)
    
    def render(self):
        atnames=list(self.context['ar'].keys())

        for x in atnames:
            del self.context['ar'][x]
            
        self.redirect("http://localhost:8080/oship") # now simply redirect to the main page
        
        
class ImportMSW(grok.View):
    """Import the mammal vocabulary into the term server."""
    grok.context(oship)

    def render(self):
        
        try:
            self.context['termserver']['msw'] = grok.Container()
        except DuplicationError:
            pass
        
        vocab=CreatMSW() # a list of tuples consisiting of an Id and a mammal model
        print len(vocab), " = # of mammals to be added."
        n=len(vocab)
        x=0
        while x<n:
            try:
                mammal=vocab[x]
                mammalid=mammal[0]
                mammalobj=mammal[1]
                self.context['termserver']['msw'][mammalid]=mammalobj 
                print "Added: # ",x, " - ",mammalid, mammalobj
            except DuplicationError:
                print "Duplication of Mammal ID: ", mammalid
                pass
            x+=1
            
        
        
        #try:
            #for x in vocab:
                #self.context['termserver']['msw'][x[0]]=x[1] 
                #print "Added: ",x[0]
        #except DuplicationError:
            #print "Duplication of Mammal ID: ", x[0]
            #pass
        

        self.redirect("http://localhost:8080/oship") # now simply redirect to the main page
            