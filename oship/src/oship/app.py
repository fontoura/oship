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
            self.context['ar'] = Folder() # archetype repository
            self.context['termserver'] = Folder() # terminology server
            self.context['demographics'] = Folder() # demographics space
            self.context['clinical'] = Folder() # clinical space
        except DuplicationError:
            pass
        
        atname=u'a-name' #place holder name
        fnames = getFileList()
        
        for fname in fnames: # we have our list of ADL files
            print "Processing: ",fname
            atlist=CreateAT(fname) # take one ADL file and process it into a nested list
            atname=atlist[0] # get the real archetype  name
            
         
            fldr=atlist[1] #setup a place to put the archetype in the ar
            try:            
                self.context['ar'].__setitem__(atname,fldr)
            except ValueError:   
                pass
         
        
        self.redirect("http://localhost:8080/manage") # now simply redirect to the ZMI
            