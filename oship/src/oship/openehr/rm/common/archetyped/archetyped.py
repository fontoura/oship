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
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.archetyped.locatable import Locatable
from interfaces.archetyped import IArchetyped

_ = MessageFactory('oship')
        
  
class Archetyped(Locatable):
    """
    Archetypes act as the configuration basis for the particular structures of instances
    defined by the reference model. To enable archetypes to be used to create valid
    data, key classes in the reference model act as "root" points for archetyping;
    accordingly, these classes have the archetype_details attribute set. An instance of
    the class ARCHETYPED contains the relevant archetype identification information,
    allowing generating archetypes to be matched up with data instances
    """
    
    implements(IArchetyped)
            
    def __init__(self,atid,tmplid,rmver,**kw):
        self.archetypeId=atid
        self.templateId=tmplid
        self.rmVersion=rmver
        for n,v in kw.items():
            setattr(self,n,v)
        

    def archetypeIdValid():
        """ archetypeId != None """
        
    def rmVersionValid():
        """ rmVersion != None and rmVersion != '' """
