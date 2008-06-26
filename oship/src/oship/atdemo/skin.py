from z3c.formui.interfaces import IDivFormLayer

from oship.atdemo.layer import IATDemoBrowserLayer

class IATDemoBrowserSkin(IDivFormLayer,IATDemoBrowserLayer):
    """The browser skin using the div-based layout."""