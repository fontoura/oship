# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the Mozilla Public License Version 1.1 - see docs/OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

import os
import logging
import grok
from zope.exceptions import DuplicationError
from zope.i18nmessageid import MessageFactory
from openehr.atbldr import CreatePy
from oship.oeterm.oeterm import importOETerms
from oship.rxterms.createrxterms import CreateRxTerms


# Begin OSHIP Demo
class oship(grok.Application, grok.Container):
    pass    

class Index(grok.View):
    grok.context(oship)
    
    def render(self):
        grok.PageTemplate("<h1>Executing Setup.  Please Standby!</h1>")
        self.redirect(self.url('setup'))
            
    
class OshipManage(grok.View):
    grok.context(oship)
    
    
class Terms(grok.View):   
    grok.context(oship)
        
class Demos(grok.View):
    grok.context(oship)

class ATQL(grok.View):
    grok.context(oship)

class ManageICD(grok.View):
    grok.context(oship)

class ManageLOINC(grok.View):
    grok.context(oship)
    
class SetupNotice(grok.View):
    grok.context(oship)

class ManageRxTerms(grok.View):
    grok.context(oship)

class ManageSMCT(grok.View):
    grok.context(oship)


# Create the containers and initial archetypes
class Setup(grok.View):
    """
    Create the OSHIP application core, setup the containers, and create the Python source from the existing ADL files.
    """

    grok.context(oship)
    
    def render(self):

        logfile=os.getcwd()+'/src/oship/openehr/py_files/pyfile_build.log'
        #create the logfile if it doesn't exist
        f=open(logfile,'w')
        f.write("Python source file log.\n\n")
        f.close()
        
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s',
                            filename=logfile,
                            filemode='w')


        try:
            #self.context['ar'] = grok.Container() # archetype repository
            self.context['termserver'] = grok.Container() # terminology server
            self.context['aql'] = grok.Container() # AQL repository
        except DuplicationError:
            pass
        
        #fnames = getFileList()
        #try:        
            #for fname in fnames: # we have our list of ADL files
                #print "Processing: ",fname
                
                #at=CreateAT(fname) # take one ADL file and process it into a mapping

                #atname=at[0]
                
                #self.context['ar'][atname]=at[1]
        #except DuplicationError:
            #pass
         
        #print "Setup and ar ADL processing is complete.\n"
        
        
        print "\n\n\n********* Begin creating Python files. *********\n"
        
        CreatePy()
        
        print "\n\n Finished creating Python source files.\n"
        
        self.redirect("http://localhost:8080/oship/oshipmanage") # now simply redirect to the main page
            
class Emptyar(grok.View):
    """Remove all the archetypes in the repository"""
    
    grok.context(oship)
    
    def render(self):
        atnames=list(self.context['ar'].keys())

        for x in atnames:
            del self.context['ar'][x]
            
        self.redirect("http://localhost:8080/oship") # now simply redirect to the main page

"""
Start the terminology import section
"""
                
class ImportOE(grok.View):
    """Import the openEHR vocabulary into the term server."""
    grok.context(oship)

    def render(self):
        
        try:
            self.context['termserver']['oeterms'] = grok.Container()
        except DuplicationError:
            pass
        
        vocab=importOETerms() # a list of tuples consisting of 
        print len(vocab), " = # of terms to be added."
        n=len(vocab)
        x=0
        while x<n:
            try:
                term=vocab[x]
                grpconcept=term[0]
                termobj=term[1]
                print grpconcept,termobj
                
                self.context['termserver']['oeterms'][grpconcept]=termobj 
                #print "Added: # ",x, " - ",concept, termobj
            except DuplicationError:
                print "Duplication of Concept: ", grpconcept
                pass
            x+=1
                    
        print "\n\nOpenEHR Terminology Import Complete"
        self.redirect("http://localhost:8080/oship") # now simply redirect to the main page

class ImportRxTerms(grok.View):
    """Import the RxTerms vocabulary into the term server."""
    grok.context(oship)

    def render(self):
        
        
        vocab=CreateRxTerms() # a list of tuples consisting of Release, RXCUI,Term Object
        numterms=len(vocab)
        n=len(vocab)
        x=0
        release=vocab[0][0]
        try:
            self.context['termserver'][release] = grok.Container() # create the release container
        except DuplicationError:
            pass

        while x<n:
            try:
                rxcui=vocab[x][1]
                termobj=vocab[x][2]
                
                self.context['termserver'][release][rxcui]=termobj # add the term objects using rxcui as the key
                #print "Added: # ",x, " - ",concept, termobj
            except DuplicationError:
                print "Duplication of Concept: ", rxcui
                pass
            x+=1
            print "Added: ",x," of ",numterms," RXCUI= ",rxcui
            
        print "\n\nRxTerms import is complete.\n"

        self.redirect("http://localhost:8080/oship/oshipmanage") # now simply redirect to the main page

       
        


