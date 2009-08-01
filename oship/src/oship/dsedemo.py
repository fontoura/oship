# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the Mozilla Public License Version 1.1 - see docs/OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

import uuid
import grok
from datetime import date
import time

from zope.exceptions import DuplicationError
from zope.interface import Interface,implements
from zope.schema import Date,Int,TextLine
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')


"""
Begin the Decision Support Engine Demo Code
"""

# constraint for valid entries.
def validNums(value):
    return value in [0,1,2,3]


class dsedemo(grok.Application, grok.Container): 
    """
    Decision Support Demo
    """
        
    pass


class IImmunizationList(Interface):
    
    keyId=TextLine(
        title=_(u"Key ID"),
    )
    
    resultsText=TextLine(
        title=_(u"Key ID"),
    )
        
    dob=Date(
        title=_(u"DOB"),
        description=_(u"Date of Birth"),
        default=date.today()
    )
    
    examDate=Date(
        title=_(u"Exam Date"),
        description=_(u"Date of the examination."),
        default=date.today()
    )
    
    hepatitisB=Int(
        title=_(u"Hepatitis B"),
        description=_(u"Hepatitis B vaccination"),
        constraint=validNums,
        default=0
    )
    
    tetravalent=Int(
        title=_(u"tetravalent (DTP+Hib)"),
        description=_(u"tetravalent (DTP+Hib) vaccination"),
        constraint=validNums,
        default=0
    )
    
    polio=Int(
        title=_(u"Polio"),
        description=_(u"Polio vaccination"),
        constraint=validNums,
        default=0
    )
    
    rotavirus=Int(
        title=_(u"Rotavirus"),
        description=_("Rotavirus vaccination"),
        constraint=validNums,
        default=0
    )
    
    
class ImmunizationList(grok.Model):
    """A class for one examination for current immunization status."""
    
    implements(IImmunizationList)
    grok.context(dsedemo)
            
    #setup an __init__ with defaults
    def __init__(self):        
        keyId=unicode(uuid.uuid4())
        resultsText=u''
        dob=date.today()
        examDate=date.today()
        hepatitisB=0
        tetravalent=0
        polio=0
        rotavirus=0
        
        
class Index(grok.View):
    grok.context(dsedemo)
    
    def render(self):
        try:
            self.context['dsedemo'] = grok.Container() # demo container
        except DuplicationError:
            pass
        
        self.redirect(self.application_url()+"/dsemain")
        
# Main view  
class DseMain(grok.View):
    grok.context(dsedemo)

# Setup Viewletmanagers
class Header(grok.ViewletManager):
    grok.name('header')
    grok.context(dsedemo)
    
class Footer(grok.ViewletManager):
    grok.name('footer')
    grok.context(dsedemo)
    
class Results(grok.ViewletManager):
    grok.name('results')
    grok.context(dsedemo)

class InputArea(grok.ViewletManager):
    grok.name('inputarea')
    grok.context(dsedemo)

# Define the viewlets
class PageTitle(grok.Viewlet):
    grok.context(dsedemo)
    grok.viewletmanager(Header)
    grok.order(1)
    
class FooterText(grok.Viewlet):
    grok.context(dsedemo)
    grok.viewletmanager(Footer)
    grok.order(1)
    
    
class InputForm(grok.Viewlet):
    grok.context(dsedemo)
    grok.viewletmanager(InputArea)
    grok.order(1)
    
    
class CheckResults(grok.Viewlet):
    grok.context(dsedemo)
    grok.viewletmanager(Results)
    grok.order(1)
    
    def render(self):
        return "Results are here."
    
    
class WarningText(grok.Viewlet):
    grok.context(dsedemo)
    grok.viewletmanager(Results)
    grok.order(2)
    
        
#class ImmunizationsForm(grok.AddForm):   
    #grok.context(dsedemo)
    #form_fields = grok.AutoFields(ImmunizationList)
    
    ##here we setup an alternate display form that has been customized from the original generic add form.
    ##the URL though is still to /immunizationsform NOT to immadd.
    #template = grok.PageTemplateFile('dsedemo_templates/immadd.pt') 
    
    #def setUpWidgets(self):
        #super(ImmunizationsForm, self).setUpWidgets()
        #self.widgets['hepatitisB'].displayWidth = 1
        #self.widgets['tetravalent'].displayWidth = 1
        #self.widgets['polio'].displayWidth = 1
        #self.widgets['rotavirus'].displayWidth = 1
        
    
    
    #@grok.action('Process')
    #def add(self, **data):
        #immlist = ImmunizationList()
        #self.applyData(immlist, **data)
        ##self.context[name] = immlist
        ##return self.redirect(self.url(self.context[name]))

                
#class Edit(grok.EditForm):   
    #grok.context(dsedemo)
    #form_fields = grok.AutoFields(ImmunizationList)
    #label = "Childhood Immunizations Checkup Demo"
    
    
            
    
#class immCalc(grok.View):
    #""" This view demonstrates the typical if/elif construct for making these decisions."""
    
    #grok.context(dsedemo)

    #def update(self):
        #""" Note that everything in self.request is a string so conversions are required."""
        
        #examDate = datetime(*(time.strptime(self.request['form.examDate'], '%Y-%m-%d')[0:6]))
        #dob = datetime(*(time.strptime(self.request['form.dob'], '%Y-%m-%d')[0:6]))
        #self.age = ( examDate - dob ).days
        #self.hepatitisB = int(self.request['form.hepatitisB'])
        #self.tetravalent = int(self.request['form.tetravalent'])
        #self.polio = int(self.request['form.polio'])
        #self.rotavirus = int(self.request['form.rotavirus'])
        #self.resultstxt = "" # info for physcian
            
        ## Hep B
        #if self.hepatitisB == 0: # any age
            #self.resultstxt += "Needs Hepatitis B #1; "
            
        #elif self.age >= 30 and self.age < 60 and self.hepatitisB == 1:
            #self.resultstxt += "Needs Hepatitis B #2; "
                                    
        #elif self.age >= 120 and self.age < 180 and self.hepatitisB == 2:
            #self.resultstxt += "Needs Hepatitis B #3; "
            
            
        ## No Immunizations Needed at this time.
        #if self.resultstxt == "":
            #self.resultstxt = "No Immunizations Needed at this time."
        ## age check
        #if self.age > 180:
            #self.resultstxt = "Sorry this child is too old to assess with this application."

    
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
            


