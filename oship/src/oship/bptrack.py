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
from datetime import datetime
from zope.exceptions import DuplicationError
from zope.i18nmessageid import MessageFactory
from zope.schema import TextLine,Date,Field
from zope.interface import implements,Interface

from oship.openehr.demographic import Person,IPerson

_ = MessageFactory('oship')


# Begin Blood Pressure Tracker Demo
class bptrack(grok.Application, grok.Container ):
    pass

class Index(grok.View):
    grok.context(bptrack)
    
    def render(self):
        self.redirect(self.url('setup'))

# Main view  
class BPMain(grok.View):
    grok.context(bptrack)

# Setup Viewletmanagers
class Header(grok.ViewletManager):
    grok.name('header')
    grok.context(bptrack)
    
class Patients(grok.ViewletManager):
    grok.name('patients')
    grok.context(bptrack)
    
class DataArea(grok.ViewletManager):
    grok.name('dataarea')
    grok.context(bptrack)
    
class Footer(grok.ViewletManager):
    grok.name('footer')
    grok.context(bptrack)

# Define the viewlets
class PageTitle(grok.Viewlet):
    grok.context(bptrack)
    grok.viewletmanager(Header)
    grok.order(1)
    
class FooterText(grok.Viewlet):
    grok.context(bptrack)
    grok.viewletmanager(Footer)
    grok.order(1)
  
class PatientsHead(grok.Viewlet):
    grok.context(bptrack)
    grok.viewletmanager(Patients)
    grok.order(1)
    
class PatientsList(grok.Viewlet):
    grok.context(bptrack)
    grok.viewletmanager(Patients)
    grok.order(2)
    
    
    def render(self):
        """
        Here we create the patient listing along with a URL to their record in the clinical folder that
        points to the ehrview class so that we can list all of their previous entries as well as prepare
        to create a new entry.  
        """
        names=[]
        retstr='<ul>'
        keylist=self.context['demographics'].keys()
        for x in keylist:
            # create a tuple to append to the names list that also includes the ehrurl.
            sname=self.context['demographics'][x].surName
            gname=self.context['demographics'][x].givenName
            dob=self.context['demographics'][x].dob
            fname=gname+" "+sname
            # To get the url we have to use the parent view, then strip off that name and add the clinical container
            # and each patient's record number (ehrid). Send the full name so we can display it in the ehrview.
            ehrurl=self.view.url().strip('/bpmain')+'/ehrindex?ehrid='+self.context['demographics'][x].ehrid+'&fname='+fname+'&dob='+datetime.strftime(dob,"%Y/%m/%d")
            
            names.append((sname,gname,ehrurl))
            
        # create the display string to return to the interface.    
        for y in names:
            retstr+= '<li><a href="'+y[2]+'">'+y[0]+','+y[1]+'</a> '+'</li>'
            
        retstr+='</ul>'   
        
        if retstr == '<ul></ul>':
            retstr = "You haven't added any patients to this system. Please use the Add patient Form."
            
        return retstr
            
            
                    
        
class NewPatient(grok.Viewlet):
    grok.context(bptrack)
    grok.viewletmanager(DataArea)
    grok.order(1)
    
    
class BPData(grok.Viewlet):
    grok.context(bptrack)
    grok.viewletmanager(DataArea)
    grok.order(2)
    

# define a simple patient entry not using the openEHR demographics section

class IPatient(Interface):
    surName=TextLine(
        title=u"Surname"
    )
    
    givenName=TextLine(
        title=u"Given Name"
    )
    
    dob=Date(
        title=u"Date of Birth"
    )
    
    patid=TextLine(
        title=u"Patient ID",
    )
    
    ehrid=TextLine(
        title=u"EHR ID"
    )
    
    
class Patient(grok.Model):
    grok.context(bptrack)
    grok.implements(IPatient)

    
    def __init__(self,surName,givenName,dob):
        self.patid=unicode(uuid.uuid4())
        self.surName=surName
        self.givenName=givenName
        self.dob=datetime.strptime(dob, "%Y/%m/%d")
        self.__name__=self.patid
        self.ehrid=unicode(uuid.uuid4())
        
        

        
# define a simple EHR container; not using the openEHR specs


class Ehr(grok.Container):
    """
    The container for each individual's clinical data.
    """    
    grok.context(bptrack)
            
class EhrIndex(grok.View):
    grok.context(Interface)
        
    #def render(self):
        #ehr=None
        #ehrid=u'EHR ID Unknown'
        #fname=u'Unknown Patient Name'
        
        #if not self.request.has_key('ehrid'):
            #return "<b>No EHR ID received.</b>"
        #else:
            #ehrid=self.request['ehrid']
            #fname=self.request['fname']
        
        #ehr=self.context['clinical'].get(ehrid)
        #if ehr == None:
            #return "<i>EHR Information for record "+ehrid+" was not found.</i>"
           
        #return repr(ehr)
    
            
        
class Setup(grok.View):
    grok.context(bptrack)
    
    def render(self):
        try:
            self.context['demographics'] = grok.Container() # demographics space
            self.context['clinical'] = grok.Container() # clinical space
        except DuplicationError:
            pass
                 
        
        self.redirect(self.application_url()+"/bpmain")
       
    
class AddPatient(grok.View):
    """
    This view is called, as the action attribute, from the patient add form in newpatient.pt
    It creates a Patient obj where the patient id and ehr id are created from the current time stamp.
    These are use as the unique identifiers for the records in both the demographics and clinical containers.
    """
    
    grok.context(bptrack)

    def render(self):
        obj=Patient(self.request.form['surName'],self.request.form['givenName'],self.request.form['dob'])
        self.context['demographics'][obj.patid]=obj        
        self.context['clinical'][obj.ehrid]=Ehr() 
        self.context['clinical'][obj.ehrid]['created']=datetime.now()
        self.context['clinical'][obj.ehrid]['system']=u'OSHIP'
        
        self.redirect("http://localhost:8080/bptrack/bpmain") # now redirect to the main page
    
class AddBP(grok.View):
    """
    This view is called, as the action attribute, from the addbp form in the ehrindex.pt template.
    
    """
    
    grok.context(bptrack)

    def render(self):
        #obj=Patient(self.request.form['surName'],self.request.form['givenName'],self.request.form['dob'])
        #self.context['clinical'][obj.ehrid]=Ehr() 
        #self.context['clinical'][obj.ehrid]['created']=datetime.now()
        #self.context['clinical'][obj.ehrid]['system']=u'OSHIP'
        
        #self.redirect("http://localhost:8080/bptrack/bpmain") # now redirect back to the main page
        return "Nothing happening here yet."
    