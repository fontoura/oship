##############################################################################
#
# Copyright (c) 2007 Timothy Cook and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Gnu Public License,
# Version 2.0 (GPL).  A copy of the GPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id: 
"""

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

from zope.app.container.constraints import ContainerTypeConstraint
from zope.app.container.constraints import ItemTypePrecondition
from zope.app.container.interfaces import IContained, IContainer
from zope.app.file.interfaces import IFile
