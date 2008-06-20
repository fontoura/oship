# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

From the demographic package from openEHR 
Demographic Information Model package Rev. 2.0.1

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.interface import implements
from zope.schema import Set,List
from zope.i18nmessageid import MessageFactory

import party

_ = MessageFactory('oship')

    
  
class IActor(IParty):
    """
    Ancestor of all real world types.
    """
    
    roles=Set(
        title=_(u"Roles"),
        description=_(u"Identifiers of the Version container for each Role played by this party."),
        required=False,
    )
    
    languages=List(
        title=_(u"Languages"),
        description=_(u"A list of languages to be used to communicate with this actor."),
        required=False,
    )
    def hasLegalIdentity():
        """
        Return True/False regarding a legal identiry of this Actor.
        """

   
class Actor(Party):
    """
    Ancestor of al real world types.
    """
    
    implements(IActor)
    
    def __init__(self, roles,languages,**kw):
        self.roles=roles
        self.languages=languages
        for n,v in kw.items():
            setattr(self,n,v)
    
    def hasLegalIdentity():
        """
        Return True/False regarding a legal identiry of this Actor.
        """