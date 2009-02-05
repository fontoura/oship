# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the archetyped package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.app.container.contained import Contained
from zope.schema import Field
from zope.i18nmessageid import MessageFactory

from interfaces.pathable import IPathable

_ = MessageFactory('oship')

class Pathable(Contained):
    """
    Abstract parent of all classes whose instances are reachable by paths, and which
    know how to locate child object by paths. The parent feature may be implemented 
    as a function or attribute.
    
    The two attributes required for locatable in ZCA is __parent__ and __name__.  
    We inherit those from Location.
    
    The functionality to get paths and find children is contained in the traversal mechanism.
    """
    
    implements(IPathable)
        
    
    def pathOfItem(an_item):
        """
        The path to an item relative to the root of this archetyped structure.
        
        getPath is from the Traversal API.
        """
                       
    def itemAtPath(a_path):
        """
        The item at a path (relative to this item);only valid for unique paths, i.e. paths
        that resolve to a single item.
        a_path is a string.
        Return a_path != None and pathUnique(a_path)
        
        If the path is not unique or not found then a TraversalError is raised.
        """       
        
        
    def itemsAtPath(a_path):
        """
        List of items corresponding to a non-unique path.
        a_path is a List
        Return a_path != None and pathUnique(a_path)
        """
        
 
    def pathExists(a_path):
        """
        True if the path exists in the data with respect to the current item.
        Return a_path != None and a_path != '' 
        """
        
        
    def pathUnique(a_path):
        """
        True if the path corresponds to a single item in the data.
        Return a_path != None and pathExists(a_path)
        """
 