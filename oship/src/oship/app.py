import grok
from datetime import datetime 

from oship.openehr.am.archetype.interfaces.archetype import IArchetype

class Oship(grok.Application, grok.Container):
    pass

class Index(grok.View):
    
    def current_datetime(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M')


class ATView(grok.View):
    grok.context(IArchetype) # register the context for all archetypes.
    form_fields = grok.Fields(IArchetype)
    
    pass

class ARList(grok.View):
    """ Show the Archetype Repository Contents"""
    pass
