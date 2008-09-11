# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

This class represent a concept in a terminology group.

"""

__author__  = u'Sergio Miranda Freire <sergio@lampada.uerj.br>'
__docformat__ = 'plaintext'

from zope.schema import Object
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')

class Concept(Object):
    """
    a concept in a terminology group
    """

	def __init__(self, id, rubric, description=None)
		self.id = id
		self.rubric = rubric
		self.description = description