# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

import grok
from zope.i18nmessageid import MessageFactory


class Oship(grok.Application, grok.Container):
    pass

class Index(grok.View):
    grok.context(Oship)
    
class Setup(grok.View):
    grok.context(Oship)
    try:
        def render(self):
            self.context['termserver'] = grok.Container()
            self.context['demographics'] = grok.Container()
            self.context['clinical'] = grok.Container()
            return "Setup is complete. Return to the main page"
    except DuplicationError:
        duplicate()
        
    def duplicate():
        grok.PageTemplate("Setup already executed. Return to the main page.")
        return
    
    
