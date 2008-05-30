# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""


The Open Source Health Information Platform container. 
This is the root container for all EHRs, Demographics and Terminology Services.

"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zope.app.container.constraints import ContainerTypesConstraint
from zope.app.container.constraints import ItemTypePrecondition 
from zope.app.container.interfaces import IContained, IContainer
from zope.app.file.interfaces import IFile 

from interfaces import IOship

class Oship(BTreeContainer):
    ''' The root OSHIP class definition.'''
    implements(IOship)   
    
    # Initializer
    def __init__(self, title='Default OSHIP root.'):
        self.title = title
        super(Oship, self).__init__()
        
    def get_title(self):
        return self.title

    def test(self):
        return 'test'
