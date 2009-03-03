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
            self.context['termserver'] = Folder() # terminology server
        except DuplicationError:
            pass
        
        fnames = getFileList()
        try:        
            for fname in fnames: # we have our list of ADL files
                print "Processing: ",fname
                
                at=CreateAT(fname) # take one ADL file and process it into a mapping

                atname=at[u"className"]
                
                self.context['ar'][atname]=at
        except DuplicationError:
            pass
         
        
        self.redirect("http://localhost:8080/manage") # now simply redirect to the ZMI
            