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

# Begin Height/Weight Demo
class htwt(grok.Application, grok.Container ):
    pass

class Index(grok.View):
    grok.context(htwt)


class Setup(grok.View):
    grok.context(htwt)
    
    def render(self):
        try:
            self.context['demographics'] = grok.Container() # demographics space
            self.context['clinical'] = grok.Container() # clinical space
        except DuplicationError:
            pass
                 
        
        self.redirect("http://localhost:8080/htwt") # now simply redirect to the main page
            