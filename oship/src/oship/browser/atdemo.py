# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

from z3c.form import form, field
from z3c.form.interfaces import DISPLAY_MODE

from oship.openehr.am.archetype.interfaces.archetype import IArchetype

class ATDemoDisplayForm(form.Form):
    """A simple display form Archetypes."""

    fields = field.Fields(IArchetype)
    mode = DISPLAY_MODE
