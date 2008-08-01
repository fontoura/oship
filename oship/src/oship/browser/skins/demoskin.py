import z3c.formui.interfaces

from oship.browser.layers.demolayer import IDemoarchetypeBrowserLayer

class IDemoarchetypeBrowserSkin(z3c.formui.interfaces.IDivFormLayer,IDemoarchetypeBrowserLayer):
    """The browser skin using the div-based layout."""
