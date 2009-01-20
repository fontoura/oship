# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the interfaces for the am.archetype.constraint package defined in 
The Archetype Object model Rev 2.0.2
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'
__contributors__ = 'Roger Erens <roger.erens@e-s-c.biz>', u'Roberto Cunha <roliveiracunha@yahoo.com.br>', u'Sergio Miranda Freire sergio@lampada.uerj.br', u'Andre Goncalves <goncalves.aluiz@gmail.com'

from zope.i18nmessageid.message import MessageFactory 
from zope.interface import implements

from interfaces.ccomplexobject import ICComplexObject
from cdefinedobject import CDefinedObject

_ = MessageFactory('oship')

class CComplexObject(CDefinedObject):
    """
    Constraint on complex objects.
    """
    
    implements(ICComplexObject)
   
    
    def __init__(self,attributes,assumedValue,rmTypeName,occurrences,nodeId,parent):
        CDefinedObject.__init__(assumedValue,rmTypeName,occurrences,nodeId,parent)
        self.attributes=attributes
        
        
    def anyAllowed():
        if not self.attributes is None:
            return (len(self.attributes) == 0)
        else:
            return (False)
    

