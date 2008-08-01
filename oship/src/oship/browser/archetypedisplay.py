from z3c.form import form, field, button
from z3c.form.interfaces import DISPLAY_MODE
from oship.openehr.am.archetype.interfaces.archetype import IArchetype

class ArchetypeDisplayForm(form.Form):
    """A simple display form for contacts."""

    fields = field.Fields(IArchetype)
    mode = DISPLAY_MODE
