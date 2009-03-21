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
from zope.schema import TextLine
from zope.interface import implements,Interface

from oship.openehr.demographic import Person,IPerson

_ = MessageFactory('oship')


# Begin Blood Pressure Tracker Demo
class bptrack(grok.Application, grok.Container ):
    pass

class Index(grok.View):
    grok.context(bptrack)

class Setup(grok.View):
    grok.context(bptrack)
    
    def render(self):
        try:
            self.context['demographics'] = grok.Container() # demographics space
            self.context['clinical'] = grok.Container() # clinical space
        except DuplicationError:
            pass
                 
        
        self.redirect("http://localhost:8080/oship") # now simply redirect to the main page
        
       
    
    
class CreatePerson(grok.AddForm):
    """Create a new person.  All of these people will only have the role of 'Patient'"""
    grok.context(bptrack)
    grok.name('createperson')
    
    form_fields = grok.AutoFields(IPerson)
    
    
    label = "Create a person."

    @grok.action('Add Person')
    def add(self, **data):
        person=Person()
        self.applyData(person, **data)
        import datetime
        name = str(datetime.datetime.now()).replace(' ','-')
        self.context['demographics'][name] = person
        return self.redirect(self.url(self.context['demographics'][name]))

    
class BPEntry(grok.View):
    pass
