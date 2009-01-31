# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL License.
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

from zope.schema import Set,Bool, Object
from zope.i18nmessageid.message import MessageFactory 
from oship.openehr.am.archetype.constraintmodel.interfaces.cattribute import ICAttribute

from cdefinedobject import ICDefinedObject

_ = MessageFactory('oship')


class ICComplexObject(ICDefinedObject):
    """
    Constraint on complex objects.
    """
    
    attributes=Set(
        title=_(u"Attributes"),
        description=_(u"List of constraints on attributes of the reference model."),
        required=False,
        value_type=Object(schema=ICAttribute),
    )

    anyAllowed=Bool(
        title=_(u"Any Allowed"),
        description=_(u"True if any value of the reference model is allowed."),
        required=True,
    )
    
    def anyAllowed():
        """True if any value of the reference model is allowed.
        """