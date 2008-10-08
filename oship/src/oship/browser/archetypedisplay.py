from z3c.form import form, field, button
from z3c.form.interfaces import DISPLAY_MODE
from oship.openehr.am.archetype.interfaces.archetype import IArchetype

class ArchetypeDisplayForm(form.Form):
    """A simple example display form for archetypes."""
    
    fields=field.Fields(IArchetype['adlVersion'],IArchetype['concept'])

    mode = DISPLAY_MODE
