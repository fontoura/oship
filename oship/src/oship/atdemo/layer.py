from z3c.form.interfaces import IFormLayer
from z3c.layer.pagelet import IPageletBrowserLayer

class IATDemoBrowserLayer(IFormLayer, IPageletBrowserLayer):
    """ATDemo browser layer with form support."""
