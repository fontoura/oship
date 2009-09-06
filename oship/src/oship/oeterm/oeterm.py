# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the Mozilla Public License Version 1.1 - see docs/OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

openEHR Terminology models

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'<name> <email address>'

import os
from xml.etree.ElementTree import ElementTree,Element

from zope.interface import Interface,implements
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory
import grok

_ = MessageFactory('oship')


class IopenEHRTerminology(Interface):
    """openEHR terminology codes"""

    groupName=TextLine(
        title=_("Group Name")
    )

    conceptId=TextLine(
        title=_(u"Concept ID")
    )

    rubric=TextLine(
        title=_(u"Rubric")
    )


class openEHRTerminology(grok.Model):
    """openEHR Terminology codes"""

    implements(IopenEHRTerminology)

    def __init__(self,groupName,conceptId,rubric):
        self.groupName=groupName
        self.conceptId=conceptId
        self.rubric=rubric


def importOETerms():
    """Create a list of openEHR Terms to add to the term server."""

    termslist=[]
    #create an ElementTree instance from an XML file
    doc = ElementTree(file=os.getcwd()+"/src/oship/oeterm/openehr_terminology_en.xml")
    # now get an iterator and breakdown the Elements.
    tree=doc.getiterator()
    for x in tree:
        grouplist = x.findall('group')
        for n in grouplist:
                groupnames=n.items()
                grpname=unicode(groupnames[0][1],'utf-8')
                #print grpname
                conceptlist=n.findall('concept')
                for y in conceptlist:
                    concepts=y.items()
                    conceptId=unicode(concepts[0][1],'utf-8')
                    conceptRubric=unicode(concepts[1][1],'utf-8')
                    #print grpname, conceptId, conceptRubric
                    "grpname + concepId is required as a key because some concepIds are repeated in different groups."
                    termslist.append((grpname+' '+conceptId,openEHRTerminology(grpname,conceptId,conceptRubric)))


    #print termslist

    return termslist


