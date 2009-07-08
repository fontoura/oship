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
import datetime
import grok
from zope.interface import Interface,implements
from zope.schema import Date,Int
from zope.exceptions import DuplicationError
from zope.i18nmessageid import MessageFactory
from openehr.atbldr import CreatePy
from oship.oeterm.oeterm import importOETerms
from oship.rxterms.createrxterms import CreateRxTerms

_ = MessageFactory('oship')

# Begin OSHIP Demo
class oship(grok.Application, grok.Container):
    pass    

class Index(grok.View):
    grok.context(oship)
    
    # Create the containers and initial python sourcee templates for the archetypes   
    def render(self):
        logfile=os.getcwd()+'/parts/log/pyfile_build.log'
        #create the logfile if it doesn't exist
        f=open(logfile,'w')
        f.write("Python source file log.\n\n")
        
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s',
                            filename=f,
                            filemode='w')


        try:
            self.context['termserver'] = grok.Container() # terminology server
            self.context['aql'] = grok.Container() # AQL repository
        except DuplicationError:
            pass
        
        print "\n\n\n********* Begin creating Python files. *********\n"
        
        CreatePy()
        
        print "\n\n Finished creating Python source files.\n"
        
        self.redirect("http://localhost:8080/oship/oshipmanage") # now simply redirect to the main page
            
    
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
    
class ManageRxTerms(grok.View):
    grok.context(oship)

class ManageSMCT(grok.View):
    grok.context(oship)

class EditPySrc(grok.View):   
    grok.context(oship)



    
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
        self.redirect("http://localhost:8080/oship/oshipmanage") # now simply redirect to the main page

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

"""
Begin the DSS Demo Code
"""

def validNums(value):
    return value in [0,1,2,3]


class DSSDemo(grok.View):   
    grok.context(oship)

class IImmunizationList(Interface):
    
    dob=Date(
        title=_(u"DOB"),
        description=_(u"Date of Birth"),
        required=True
    )
    
    examDate=Date(
        title=_(u"Exam Date"),
        description=_(u"Date of the examination."),
        default=datetime.date.today()
    )
    
    hepatitisB=Int(
        title=_(u"Hepatitis B"),
        description=_(u"Hepatitis B vaccination"),
        constraint=validNums
    )
    
    tetravalent=Int(
        title=_(u"tetravalent (DTP+Hib)"),
        description=_(u"tetravalent (DTP+Hib) vaccination"),
        constraint=validNums
    )
    
    polio=Int(
        title=_(u"Polio"),
        description=_(u"Polio vaccination"),
        constraint=validNums
    )
    
    rotavirus=Int(
        title=_(u"Rotavirus"),
        description=_("Rotavirus vaccination"),
        constraint=validNums
    )
    
    
class ImmunizationList(grok.Model):
    """A class for one examination for current immunization status."""
    
    implements(IImmunizationList)
    
class Immunizations2(grok.View):   
    grok.context(oship)
                
        
class ImmunizationsForm(grok.AddForm):   
    grok.context(oship)
    grok.name('immunizations')
    form_fields = grok.AutoFields(ImmunizationList)
    
    @grok.action('Add Immunization List')
    def add(self, **data):
        immlist = ImmunizationList()
        self.applyData(immlist, **data)
        immCalc(immlist)    
    
def immCalc(immlist):
    age = (immlist.examDate - immlist.dob).days
    print immlist.dob
    print immlist.examDate
    print immlist.hepatitisB
    print immlist.tetravalent
    print immlist.polio
    print immlist.rotavirus
    print u"Age = ", age
    
    """
    1) Calculation of age:<br />
    Age in days [B] = Date of admission [C] – Date of birth [D]<br />
    
    
    
    Hepatitis B [a]<br />
    tetravalent (DTP+Hib) [b]<br />
    Polio [c]<br />
    Rotavirus [d]<br /><br />
    
    3) Decision Rules<br />
    If [B] < 30 then [a] (1st dose)<br />
    If 30 ≤ [B] < 60 then [a] (2nd dose)<br />
    If 60 ≤ [B] < 90 then [b] (1st dose), [c] (1st dose) and [d] (1st dose)<br />
    If 90 ≤ [B] < 120 then [b] (2nd dose), [c] (2nd dose) and [d] (2nd dose)<br />
    If 120 ≤ [B] < 180 then [a] (3rd dose), [b] (3rd dose) and [c] (3rd dose)<br />

    """
    

        


