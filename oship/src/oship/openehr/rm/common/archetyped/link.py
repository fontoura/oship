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

from zope.interface import implements,Interface
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory

from openehr.rm.common.locatable import Locatable,ILocatable
from openehr.rm.datatypes.dvtext import DvText
from openehr.rm.datatypes.dvehruri import DvEhrUri

_ = MessageFactory('oship')
        
class ILink(ILocatable):
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
    
    meaning = DvText(
        title=_(u"Meaning"),
        description=_(u"""Used to describe the relationship, usually in clinical terms, such as 
                    “in response to” (the relationship between test results and an order),
                    “follow-up to” and so on. Such relationships can represent any clinically 
                    meaningful connection between pieces of information. Values for meaning 
                    include those described in Annex C, ENV 13606 pt 2 [11] under the categories 
                    of “generic”, “documenting and reporting”,“organisational”,“clinical”,
                    “circumstancial”, and “view management”.  """),
        required=True,
        )
    
    type = DvText(
        title=_(u"Type"),
        description=_(u"""The type attribute is used to indicate a clinical or domain-level meaning 
                    for the kind of link, for example “problem” or “issue”. If type values are 
                    designed appropriately, they can be used by the requestor of EHR extracts to 
                    categorise links which must be followed and which can be broken when the extract 
                    is created. """),
        required=True,
        )
    
    target = DvEhrUri(
        title=_(u"Target"),
        description=_(u"""The logical “to” object in the link relation, as target: 
                    per the linguistic sense of the meaning attribute."""),
        required=True,
        )
    
    def meaningValid():
        """Return meaning != None """
        
    def typeValid():
        """Return type != None """
        
    def targetValid():
        """Return target != None """

        
        
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
    
    def __init__(self,meaning,type,target,**kw):
        self.meaning=meaning
        self.type=type
        self.target=target
        for n,v in kw.items():
            setattr(self,n,v)
     
    def meaningValid():
        """Return meaning != None """
        
    def typeValid():
        """Return type != None """
        
    def targetValid():
        """Return target != None """

