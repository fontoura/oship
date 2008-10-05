from z3c.form import form, field, button
from z3c.form.interfaces import DISPLAY_MODE
from oship.openehr.am.archetype.interfaces.archetype import IArchetype

class ArchetypeDisplayForm(form.Form):
    """A simple display form for archetypes."""
    
    fields = field.Fields(IArchetype).omit('__name__', '__parent__')
    #fields=field.Fields(IArchetype['adlVersion'],IArchetype['concept'])

    mode = DISPLAY_MODE
