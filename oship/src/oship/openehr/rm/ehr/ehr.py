# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

Implementations for specifications from openEHR 
EHR Information Model package Rev. 5.1.0

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.schema.interfaces import Container
from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from openehr.rm.ehr.interfaces.ehr import *


_ = MessageFactory('oship')

class Ehr(Container):
    """
    Root EHR container
    """
    
    implements(IEhr)
    
    def __init__(self,sysid,ehrid,tcreated,contribs,ehraccess,ehrstatus,dir,compos,**kwargs):
        self.systemId=sysid
        self.ehrId=ehrid
        self.timeCreated=tcreated
        self.contributions=contribs
        self.ehrAccess=ehraccess
        self.ehrStatus=ehrstatus
        self.directory=dir
        self.compositions=compos
            
class VersionedEhrAccess(VersionedObject):
    """
    Version container for EHR Access instance.
    """
    
    implements(IVersionedEhrAccess)
    
    
class EhrAccess(Locatable):
    """
    EHR-wide access control object. Contains all policies and rules for access to data in this EHR.
    """
     
    implements(IEhrAccess)
    
    def __init__(self,settings,scheme,**kwargs):
        self.settings=settings
        self.scheme=scheme
            
class VersionedEhrStatus(VersionedObject):
    """
    Version container for the EHR status instance.
    """
    
    implements(IVersionedEhrStatus)
    
class EhrStatus(Locatable):
    """
    Instance providing various EHR wide status information.
    """
    
    implements(IEhrStatus)
    
    def __init__(self,subject,query,mod,other,**kwargs):
        self.subject=subject
        self.isQueryable=query
        self.isModifiable=mod
        self.otherDetails=other
            
class VersionedComposition(Composition):
    """
    Version controlled compsoition abstraction.
    """
    
    implements(IVersionedComposition)
    
    def __init__(self,persist,**kwargs):
        self.isPersistent=persist
            
    
    
        
    
    
    
    
    
    
    
    
    
    
    
        