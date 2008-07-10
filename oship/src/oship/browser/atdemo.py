# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

from z3c.form.interfaces import DISPLAY_MODE

class ATDemoDisplayForm(form.Form):
    """A simple display form for contacts."""

    fields = field.Fields(interfaces.IContact)
    mode = DISPLAY_MODE
