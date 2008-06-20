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

from zope.interface import Interface
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory

from openehr.rm.support.identification.archetypeid import ArchetypeId
from openehr.rm.support.identification.templateid import TemplateId
from openehr.rm.common.archetyped.locatable import Locatable

_ = MessageFactory('oship')
        
class IArchetyped(Interface):
    """
    Archetypes act as the configuration basis for the particular structures of instances
    defined by the reference model. To enable archetypes to be used to create valid
    data, key classes in the reference model act as “root” points for archetyping;
    accordingly, these classes have the archetype_details attribute set. An instance of
    the class ARCHETYPED contains the relevant archetype identification information,
    allowing generating archetypes to be matched up with data instances
    """

    archetypeId = ArchetypeId(
        title=_(u"Archetype ID"),
        description=_(u"Globally unique archetype identifier."),
        required=True,
        )
    
    templateId = TemplatedId(
        title=_(u"Template ID"),
        description=_(u"""Globally unique template identifier, if a template was active at 
                    this point in the structure. Normally, a template would only be used 
                    at the top of a top-level structure, but the possibility exists for 
                    templates at lower levels."""),
        required=False,
        )
    
    rmVersion = TextLine(
        title=_(u"RM Version"),
        description=_(u"""Version of the openEHR reference model used to create this object.
                    Expressed in terms of the release version string, e.g. “1.0”, “1.2.4”. """),
        required=True,
        default=u"1.0.1",
        )
        

    def archetypeIdValid():
        """ archetypeId != None """
        
    def rmVersionValid():
        """ rmVersion != None and rmVersion != '' """

