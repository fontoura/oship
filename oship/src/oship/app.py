import grok
from datetime import datetime 

from oship.openehr.am.archetype.interfaces.archetype import IArchetype
from oship.km.openehr.ehr.cluster.checklist_item_general import ChecklistItemGeneral

class Oship(grok.Application, grok.Container):
    pass

class Index(grok.View):
    grok.context(Oship)
    def current_datetime(self):
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M')


class ATView(grok.View):
    grok.context(IArchetype) # register the context for all archetypes.
    form_fields = grok.Fields(IArchetype)
    
    def render(self):
        return "Here we'll show an Archetype"

class ARList(grok.View):
    """ Show the Archetype Repository Contents"""
    grok.context(Oship)
    pass

    #def render(self):
    #    return "Here we'll show a list of Archetypes"


class ArchetypeDetails(grok.View):
    """
    Returns a dict of attributes and its value of an object, obj
    """
    def getAttributes(self,obj):
        attributeList = [attribute for attribute in dir(obj) \
                if not callable(getattr(obj, attribute))]
        
        objAttributes = dict()
    
        for attribute in attributeList:
            objAttributes[attribute] = getattr(obj,attribute)

        return objAttributes

    """ 
    Given the path of an archetype, 
    returns a dict of its attribute and its value
    """
    def gA(self,arche_path):
        """
        Generate the archetype name from the arche_path
        """
        arche_name = ''
        for part in arche_path.rsplit('.',1)[-1].split('_'):
            arche_name = arche_name + part.capitalize()
        
        """
        Dynamic import
        This allows it to be used for other archetypes as well
        """
        module = __import__(arche_path,fromlist=[arche_name])
        
        """
        Returns the attributes of module.arche_name
        """
        return self.getAttributes(getattr(module,arche_name)())


## Currently not in used
## TODO: Put all archetype models under this container
## for easier management
## class ArchetypeRepository(grok.Container):
##    pass

class Add(grok.AddForm):
    grok.context(Oship)

    form_fields = grok.Fields(IArchetype)

    @grok.action(u"Add archetype")
    def add_archetype(self, **data):
        # create an archetype instance
        ## TODO: Find a way to determine the type of archetype
        ## and dynamically import and create its instance
        archetype = ChecklistItemGeneral()

        # assign the right attributes to fulfill IArchetype schema with
        # the form data
        self.applyData(archetype, **data)

        # Stores the instance
        # TODO: Select a better key name
        name = data['__name__']
        # Stores the instance under the var name, name
        # TODO: check for duplication of key before storing it
        # to avoid DuplicationError 
        self.context[name] = archetype

        # redirect to the newly created object
        self.redirect(self.url(archetype))
        # we don't want to display anything, as we redirect
        return ''

class Edit(grok.EditForm):
    grok.context(IArchetype)

    form_fields = grok.Fields(IArchetype)

    @grok.action(u"Edit archetype")
    def edit_archetype(self, **data):
        self.applyData(ChecklistItemGeneral(), **data)

class Display(grok.DisplayForm):
    grok.context(IArchetype)
    grok.name('index')

    form_fields = grok.Fields(IArchetype)

