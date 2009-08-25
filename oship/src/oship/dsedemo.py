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
try:
    from oship.dse import clips
except ImportError:
    print "\n\nYour Decision Support Engine  has not been installed.  Please see oship/src/oship/docs/dse/dse.txt\n\n"

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
        self.context['dsedemo'][immlist.keyId] = immlist



class ResultsList1(grok.View):
    """The IF/THEN Process Results"""

    grok.context(dsedemo)

    def update(self):
        # convert the form values to their proper types
        self.hepatitisB = int(self.request['form.hepatitisB'])
        self.tetravalent = int(self.request['form.tetravalent'])
        self.polio = int(self.request['form.polio'])
        self.rotavirus = int(self.request['form.rotavirus'])
        self.resultstxt = u""
        self.examDate = datetime(*(time.strptime(self.request['form.examDate'], '%Y-%m-%d')[0:6]))
        self.dob = datetime(*(time.strptime(self.request['form.dob'], '%Y-%m-%d')[0:6]))
        self.age = ( self.examDate - self.dob ).days



        # Hep B
        if self.hepatitisB == 0: # any age
            self.resultstxt += "<li>Needs Hepatitis B #1</li> "
        elif self.hepatitisB == 1 and self.age >= 30:
            self.resultstxt += "<li>Needs Hepatitis B #2</li> "
        elif self.hepatitisB == 2 and self.age >= 120:
            self.resultstxt += "<li>Needs Hepatitis B #3</li> "

        # tetravalent (DTP+Hib)
        if self.age >= 60:
            if self.tetravalent == 0:
                self.resultstxt += "<li>Needs Tetravalent (DTP+Hib) Dose #1</li> "
            elif self.tetravalent == 1 and self.age >= 120:
                self.resultstxt += "<li>Needs Tetravalent (DTP+Hib) Dose #2</li> "
            elif self.tetravalent == 2 and self.age == 180:
                self.resultstxt += "<li>Needs Tetravalent (DTP+Hib) Dose #3</li> "

        # polio
        if self.age >= 60:
            if self.polio == 0:
                self.resultstxt += "<li>Needs Polio Dose #1</li> "
            elif self.polio == 1 and self.age >= 120:
                self.resultstxt += "<li>Needs Polio Dose #2</li> "
            elif self.polio == 2 and self.age == 180:
                self.resultstxt += "<li>Needs Polio Dose #3</li> "

        #  rotavirus
        if self.age >= 60:
            if self.rotavirus == 0:
                self.resultstxt += "<li>Needs Rotavirus Dose #1</li> "
            elif self.rotavirus == 1 and self.age >= 90:
                self.resultstxt += "<li>Needs Rotavirus Dose #2</li> "


        # No Immunizations Needed at this time.
        if self.resultstxt == "":
            self.resultstxt = "<li>No Immunizations Needed at this time.</li>"
        # age check
        if self.age > 180:
            self.resultstxt = "Sorry; this child is too old to assess with this application."

    def render(self):
        return u"<html><body><ul>This child is " +unicode(self.age)+ " days old and has these immunization needs: " + self.resultstxt+"</ul></body></html>"


class ImmunizationsForm2(grok.AddForm):
    """The Inference Engine Add Form"""

    grok.context(dsedemo)
    form_fields = grok.AutoFields(ImmunizationList)

    #here we setup an alternate display form that has been customized from the original generic add form.
    #the URL though is still to /immunizationsform2 NOT to inputform2
    template = grok.PageTemplateFile('dsedemo_templates/inputform2.pt')

    @grok.action('Process')
    def add(self, **data):
        immlist = ImmunizationList()
        self.applyData(immlist, **data)
        self.context['dsedemo'][immlist.keyId] = immlist



class ResultsList2(grok.View):
    """The Inference Engine Process Results"""

    grok.context(dsedemo)



    def update(self):
        # convert the form values to their proper types
        self.hepatitisB = int(self.request['form.hepatitisB'])
        self.tetravalent = int(self.request['form.tetravalent'])
        self.polio = int(self.request['form.polio'])
        self.rotavirus = int(self.request['form.rotavirus'])
        self.resultstxt = u""
        self.examDate = datetime(*(time.strptime(self.request['form.examDate'], '%Y-%m-%d')[0:6]))
        self.dob = datetime(*(time.strptime(self.request['form.dob'], '%Y-%m-%d')[0:6]))
        self.age = ( self.examDate - self.dob ).days
        try:
            clips.Clear() # MUST issue a clear before any setup begins.

            clips.DebugConfig.ActivationsWatched = True
            """
            Since this demo is for developers we are going to print everything out to the console
            """


            #build and fill the data template
            tmplt=clips.BuildTemplate("immunizations", """
                                        (slot age (type INTEGER))
                                        (slot HepB (type INTEGER))
                                        (slot tetra (type INTEGER))
                                        (slot polio (type INTEGER))
                                        (slot rota (type INTEGER))
            """, "template for child immunizations")


            immlist = clips.Fact(tmplt)  # tell Python that this is a CLIPS Fact template

            # assign the form data to the template
            immlist.Slots['age'] = self.age
            immlist.Slots['HepB'] = self.hepatitisB
            immlist.Slots['tetra'] = self.tetravalent
            immlist.Slots['polio'] = self.polio
            immlist.Slots['rota'] = self.rotavirus

            # we need to reset the fact list on each pass. This also Asserts the first fact and insures the program will begin execution.
            clips.Reset()

            immlist.Assert() # assert the facts in the template

            # Build the rules
            ageRule = clips.BuildRule("age-rule", "(immunizations (age ?x&:(< 180 ?x)))", "(assert (too_old))", "The age Limit Rule.")
            hepatitisB1Rule = clips.BuildRule("hepatitisB1-rule", "(immunizations (HepB ?x&:(= 0 ?x)))", "(assert (hepatitisB1))", "The HepatitisB Dose #1 Rule")
            hepatitisB2Rule = clips.BuildRule("hepatitisB2-rule", "(immunizations (HepB ?x&:(= 1 ?x)) (age ?y&:(<= 30 ?y)))", "(assert (hepatitisB2))","The HepatitisB Dose #2 Rule")
            hepatitisB3Rule = clips.BuildRule("hepatitisB3-rule", "(immunizations (HepB ?x&:(= 2 ?x)) (age ?y&:(<= 120 ?y)))", "(assert (hepatitisB3))","The HepatitisB Dose #3 Rule")
            tetra1Rule = clips.BuildRule("tetra1-rule", "(immunizations (tetra ?x&:(= 0 ?x)) (age ?y&:(<= 60 ?y)))", "(assert (tetra1))","The tetra Dose #1 Rule")
            tetra2Rule = clips.BuildRule("tetra2-rule", "(immunizations (tetra ?x&:(= 1 ?x)) (age ?y&:(<= 120 ?y)))", "(assert (tetra2))","The tetra Dose #2 Rule")
            tetra3Rule = clips.BuildRule("tetra3-rule", "(immunizations (tetra ?x&:(= 2 ?x)) (age ?y&:(= 180 ?y)))", "(assert (tetra3))","The tetra Dose #3 Rule")
            polio1Rule = clips.BuildRule("polio1-rule", "(immunizations (polio ?x&:(= 0 ?x)) (age ?y&:(<= 60 ?y)))", "(assert (polio1))","The polio Dose #1 Rule")
            polio2Rule = clips.BuildRule("polio2-rule", "(immunizations (polio ?x&:(= 1 ?x)) (age ?y&:(<= 120 ?y)))", "(assert (polio2))","The polio Dose #2 Rule")
            polio3Rule = clips.BuildRule("polio3-rule", "(immunizations (polio ?x&:(= 2 ?x)) (age ?y&:(= 180 ?y)))", "(assert (polio3))","The polio Dose #3 Rule")
            rota1Rule = clips.BuildRule("rota1-rule", "(immunizations (rota ?x&:(= 0 ?x)) (age ?y&:(<= 60 ?y)))", "(assert (rota1))","The rotavirus Dose #1 Rule")
            rota2Rule = clips.BuildRule("rota2-rule", "(immunizations (rota ?x&:(= 1 ?x)) (age ?y&:(<= 90 ?y)))", "(assert (rota2))","The rotavirus Dose #2 Rule")


            print "\nThe Agenda is: "
            clips.PrintAgenda()

            clips.Run()
            clips.SaveFacts("immlist.txt")
        except NameError:
            self.redirect(self.application_url()+"/dsenotinstalled")

    def render(self):
        f=open("immlist.txt",'r')
        for line in f.readlines():
            if "(initial-fact)" not in line and "(immunizations" not in line:
                if "(too_old)" in line:
                    return u"<html><body>This patient is " +unicode(self.age)+ " days old and cannot be evaluated with this application.</body></html>"
                else:
                    self.resultstxt += "<li>"+ line +"</li>"

        return u"<html><body><ul>This patient is " +unicode(self.age)+ " days old and has these immunization needs: " + self.resultstxt+"</ul></body></html>"

class DseNotInstalled(grok.View):
    grok.context(dsedemo)


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
    IF ((60 ≤ [B] < 120) AND ([E] = 0)) THEN ([F] = 1), ELSE = [G]
    IF ((120 ≤ [B] < 180) AND ([E] < 2)) THEN ([F] = ([E] + 1)), ELSE = [G]
    IF (([B] = 180) AND ([E] < 3)) THEN ([F] = ([E] + 1)), ELSE = [G]

    Vaccination type: Rotavirus
    If ([B] < 60) THEN [G]
    IF ((60 ≤ [B] < 90) AND ([E] = 0)) THEN ([F] = 1), ELSE = [G]
    IF ((90 ≤ [B] < 180) AND ([E] < 2)) THEN ([F] = ([E] + 1)), ELSE = [G]

    Footnotes:
    (1) Those decision rules are based on WHO recommendations and may vary from country to country and within regions of the same country depending on national and local vaccination policies.
    (2) Based on WHO recommendations found on WHO and other related websites on July 7th, 2009 and subjected to change at any time.
    (3) This demo is supposed to act as a technical example of the implementation of decision support systems using OSHIP and should never be used as a decision-making tool for the vaccination recommendation of real cases.

    """
