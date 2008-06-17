# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

Implementations for the archetyped package as described in the 
Common Information Model Rev. 2.1.0 

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.location import Location
from zope.interface import Interface
from zope.schema import Field
from zope.schema import Text
from zope.schema import TextLine
from zope.schema import List
from zope.i18nmessageid import MessageFactory

from openehr.rm.support.identification import *
from openehr.rm.datatypes.datetm import DvDateTime
from openehr.rm.datatypes.text import DvText
from openehr.rm.common.interfaces.archetyped import IPathable,ILocatable
from openehr.rm.common.interfaces.archetyped import IArchetyped

_ = MessageFactory('oship')


class Pathable(Location):
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
        
class Locatable(Pathable):
    """
    Root class of all information model classes that can be archetyped.
    """

    implements(ILocatable)
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links,**kwargs):
        self.uid-uid
        self.archetypeNodeId=atnodeid
        self.name=name
        self.archetypeDetails=atdetails
        self.feederAudit=fdraudit
        self.links=links
        Field.__init__(self,**kwargs)
           
    def isArchetypeRoot():
        """True if this node is the root of an archetyped structure."""
        
    def concept():
        """
        Clinical concept of the archetype as a whole (= derived from the
       ‘archetype_node_id’ of the root node) isArchetypeRoot must be True.
       """
        
    def nameValid():
        """ name != None"""
          
    def linksValid():
        """ links != None and links != []"""
 
    def archetypedValid():
        """ isArchetypeRoot xor archetypeDetails = None """
        
    def archetypeNodeIdValid():
        """ archetypeNodeId != None and archetypeNodeId != '' """
        
class Archetyped(Locatable):
    """
    Archetypes act as the configuration basis for the particular structures of instances
    defined by the reference model. To enable archetypes to be used to create valid
    data, key classes in the reference model act as “root” points for archetyping;
    accordingly, these classes have the archetype_details attribute set. An instance of
    the class ARCHETYPED contains the relevant archetype identification information,
    allowing generating archetypes to be matched up with data instances
    """
    
    implements(IArchetyped)
            
    def __init__(self,atid,tmplid,rmver,**kwargs):
        self.archetypeId=atid
        self.templateId=tmplid
        self.rmVersion=rmver
        Field.__init__(self,**kwargs)
        

    def archetypeIdValid():
        """ archetypeId != None """
        
    def rmVersionValid():
        """ rmVersion != None and rmVersion != '' """
        
class Link(Locatable):
    """
    The LINK type defines a logical relationship between two items, such as two
    ENTRYs or an ENTRY and a COMPOSITION. Links can be used across composi-
    tions, and across EHRs. Links can potentially be used between interior (i.e. non
    archetype root) nodes, although this probably should be prevented in archetypes.
    Multiple LINKs can be attached to the root object of any archetyped structure to
    give the effect of a 1->N link 1:1 and 1:N relationships between archetyped content 
    elements (e.g. ENTRYs) can be expressed by using one, or more than one, respectively, DV_LINKs.
    Chains of links can be used to see “problem threads” or other logical groupings of items.
    Links should be between archetyped structures only, i.e. between objects representing 
    complete domain concepts because relationships between sub-elements
    of whole concepts are not necessarily meaningful, and may be downright confusing. Sensible 
    links only exist between whole ENTRYs, SECTIONs, COMPOSITIONs and so on.
    """
    
    implements(ILink)
    
    def __init__(self,meaning,type,target,**kwargs):
        self.meaning=meaning
        self.type=type
        self.target=target
        Field.__init__(self,**kwargs)
     
    def meaningValid():
        """Return meaning != None """
        
    def typeValid():
        """Return type != None """
        
    def targetValid():
        """Return target != None """


class FeederAudit(Locatable):
    """
    Audit and other meta-data for systems in the feeder chain.
    """

    implements(IFeederAudit)
    
    def __init__(self,orgsysaudit,orgsysids,fsaudit,fsauditids,orgcontent,**kwargs):
        self.originatingSystemAudit=orgsysaudit
        self.originatingSystemItemIds=orgsysids
        self.feederSystemAudit=fsaudit
        self.feederSystemItemIds=fsauditids
        self.originalContent=orgcontent
        Field.__init__(self,**kwargs)
        
     
    def originatingSystemAuditValid():
        """ originatingSystemAudit != None """

class FeederAuditDetails(Field):
    u"""
    Audit details for any system in a feeder system chain. Audit details here means
    the general notion of who/where/when the information item to which the audit is
    attached was created. None of the attributes is defined as mandatory, however, in
    different scenarios, various combinations of attributes will usually be mandatory.
    This can be controlled by specifying feeder audit details in legacy archetypes.
    """

    implements(IFeederAuditDetails)
    
    def __init__(self,sysid,provider,location,time,subject,verid,**kwargs):
        self.systemId=sysid
        self.provider=provider
        self.location=location
        self.time=time
        self.subject=subject
        self.versionId=verid
        Field.__init__(self,**kwargs)
    
    def systemIdValid():
        u"""systemId != None and  systemId != '' """
        