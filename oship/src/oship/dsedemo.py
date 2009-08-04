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
from datetime import date, datetime
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
        resultsText=u'No Results'
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


       
class ImmunizationsForm1(grok.AddForm):   
    """The IF/THEN Add Form"""
    grok.context(dsedemo)
    form_fields = grok.AutoFields(ImmunizationList)
    
    #here we setup an alternate display form that has been customized from the original generic add form.
    #the URL though is still to /immunizationsform1 NOT to inputform1
    template = grok.PageTemplateFile('dsedemo_templates/inputform1.pt') 
        
    @grok.action('Process')
    def add(self, **data):
        immlist = ImmunizationList()
        self.applyData(immlist, **data)
        self.context[name] = immlist.keyId
        

        
class ResultsList1(grok.View):
    """The IF/THEN Process Results"""
    
    grok.context(dsedemo)
       
    def update(self):
        # convert the form values to their proper types
        self.examDate = datetime(*(time.strptime(self.request['form.examDate'], '%Y-%m-%d')[0:6]))
        self.dob = datetime(*(time.strptime(self.request['form.dob'], '%Y-%m-%d')[0:6]))
        self.age = ( self.examDate - self.dob ).days
        self.hepatitisB = int(self.request['form.hepatitisB'])
        self.tetravalent = int(self.request['form.tetravalent'])
        self.polio = int(self.request['form.polio'])
        self.rotavirus = int(self.request['form.rotavirus'])
        self.resultstxt = u"" 
        
        
            
        # Hep B
        if self.hepatitisB == 0: # any age
            self.resultstxt += "<li>Needs Hepatitis B #1</li> "
            
        elif self.age >= 30 and self.age < 120 and self.hepatitisB == 1:
            self.resultstxt += "<li>Needs Hepatitis B #2</li> "
                                    
        elif self.age >= 120 and self.age < 180 and self.hepatitisB == 2:
            self.resultstxt += "<li>Needs Hepatitis B #3</li> "
            
        # tetravalent (DTP+Hib)
        if self.age >= 60:
            if self.age < 90 and self.tetravalent == 0:
                self.resultstxt += "<li>Needs Tetravalent (DTP+Hib) Dose #1</li> "
            elif self.age < 120 and self.tetravalent < 2:
                self.resultstxt += "<li>Needs Tetravalent (DTP+Hib) Dose #"+str(self.tetravalent+1)+"</li> "
            elif self.age < 180 and self.tetravalent < 3:
                self.resultstxt += "<li>Needs Tetravalent (DTP+Hib) Dose #"+str(self.tetravalent+1)+"</li> "
            
        # polio
        if self.age >= 60:
            if self.age < 90 and self.polio == 0:
                self.resultstxt += "<li>Needs Polio Dose #1</li> "
            elif self.age < 120 and self.polio < 2:
                self.resultstxt += "<li>Needs Polio Dose #"+str(self.polio+1)+"</li> "
            elif self.age < 180 and self.polio < 3:
                self.resultstxt += "<li>Needs Polio Dose #"+str(self.polio+1)+"</li> "
                
        #  rotavirus
        if self.age >= 60:
            if self.age < 90 and self.rotavirus == 0:
                self.resultstxt += "<li>Needs Rotavirus Dose #1</li> "
            elif self.age < 180 and self.rotavirus < 2:
                self.resultstxt += "<li>Needs Rotavirus Dose #"+str(self.rotavirus+1)+"</li> "
        
        
        # No Immunizations Needed at this time.
        if self.resultstxt == "":
            self.resultstxt = "<li>No Immunizations Needed at this time.</li>"
        # age check
        if self.age > 180:
            self.resultstxt = "Sorry; this child is too old to assess with this application."
        
    def render(self):
        return u"<html><body><ul>This child is " +unicode(self.age)+ " days old and has these immunization needs: " + self.resultstxt+"</ul></body></html>"
    
        

    """
    Vaccination schedule from birth to 6 months (180 days) old [A](1),(2),(3)
   
   Calculation of age:
   Age in days [B] = Date of admission [C] – Date of birth [D]
   
   Evaluation:
   [E] = dose order of the vaccination already given (values = 0, 1, 2 or 3)
   
   Actions:
   [F] = dose order of the vaccination that is needed (values = 1, 2 or 3)
   [G] = when the action is “no need for this specific vaccination”
   
   Vaccination type: Hepatitis B
   IF (([B] < 30) AND ([E] = 0)) THEN ([F] = 1), ELSE = [G]
   IF ((30 ≤ [B] < 120) AND ([E] < 2)) THEN ([F] = ([E] + 1)), ELSE = [G]
   IF ((120 ≤ [B] < 180) AND ([E] < 3)) THEN ([F] = ([E] + 1)), ELSE = [G]
   
   Vaccination types: tetravalent (DTP+Hib) and Polio
   If ([B] < 60) THEN [G]
   IF ((60 ≤ [B] < 90) AND ([E] = 0)) THEN ([F] = 1), ELSE = [G]
   IF ((90 ≤ [B] < 120) AND ([E] < 2)) THEN ([F] = ([E] + 1)), ELSE = [G]
   IF ((120 ≤ [B] < 180) AND ([E] < 3)) THEN ([F] = ([E] + 1)), ELSE = [G]
   
   Vaccination type: Rotavirus
   If ([B] < 60) THEN [G]
   IF ((60 ≤ [B] < 90) AND ([E] = 0)) THEN ([F] = 1), ELSE = [G]
   IF ((90 ≤ [B] < 180) AND ([E] < 2)) THEN ([F] = ([E] + 1)), ELSE = [G]
   
   Footnotes:
   (1) Those decision rules are based on WHO recommendations and may vary from country to country and within regions of the same country depending on national and local vaccination policies. 
   (2) Based on WHO recommendations found on WHO and other related websites on July 7th, 2009 and subjected to change at any time.
   (3) This demo is supposed to act as a technical example of the implementation of decision support systems using OSHIP and should never be used as a decision-making tool for the vaccination recommendation of real cases.
    """