# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

This class contains a name and the concepts for a terminology group.

"""

__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'

from zope.schema import Object
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('oship')

class Group(Object):
    """
    a terminology group
    """

        def __init__(self, name)
            self.name =  name
            self.concepts = []

    def addConcept(self, concept):
        if concept not in concepts:
            concept.append(concept)