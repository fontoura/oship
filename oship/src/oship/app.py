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

# Begine OSHIP Demo
class oship(grok.Application, grok.Container ):
    pass

class Index(grok.View):
    grok.context(oship)


class Setup(grok.View):
    grok.context(oship)
    
    try:
        def render(self):
            self.context['ar'] = Folder()
            self.context['termserver'] = Folder()
            self.context['demographics'] = Folder()
            self.context['clinical'] = Folder()
            atname=u'a-name'
            fnames = getFileList()
            for fname in fnames:
                atlist=CreateAT(fname)
                atname=atlist[0]
                fldr=atlist[1]
                try:
                    self.context['ar'].__setitem__(atname,fldr)
                except DuplicationError:
                    break
                
            self.redirect("http://localhost:8080/oship/ar/@@contents.html")
            
    except DuplicationError:
        pass
