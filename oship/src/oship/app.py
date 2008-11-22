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
    
    def render(self):
        return "Here we'll show an Archetype"

class ARList(grok.View):
    """ Show the Archetype Repository Contents"""

    def render(self):
        return "Here we'll show a list of Archetypes"

    
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

