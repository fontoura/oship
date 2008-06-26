# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################
from z3c.form import field, button
from z3c.formui.form import Form
from z3c.form.interfaces import DISPLAY_MODE
from z3c.pagelet.browser import BrowserPagelet
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.traversing.api import getParent, getName
from zope.traversing.browser.absoluteurl import absoluteURL

from oship.atdemo.atdemo import IATDemo

class ATDemoDisplayForm(Form):
    """A simple display form for ATDemo."""

    fields = field.Fields(IATDemo)
    mode = DISPLAY_MODE
