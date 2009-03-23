# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

From the Data Structures Information Model
 Data Structure Package Rev. 2.1.0.

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid import MessageFactory
from zope.interface import Interface,implements
from zope.schema import TextLine,Field,List,Int,Object

import grok

from common import Locatable
from datatypes import IDvDateTime,IDvDuration,IDvCodedText,IDataValue
from support import IObjectRef

_ = MessageFactory('oship')




class IItemStructure(Interface):
    u"""
    Abstract parent class of all spatial data types.
    """
    pass

class IDataStructure(Interface):
    u"""
     Abstract parent class of all data structure types. Includes the as_hierarchy func-
    tion which can generate the equivalent CEN EN13606 single hierarchy for each
    subtype's physical representation. For example, the physical representation of an
    ITEM_LIST is List<ELEMENT>; its implementation of as_hierarchy will gener-
    ate a CLUSTER containing the set of ELEMENT nodes from the list.
    """

    
    def asHierarchy():
        u"""Hierarchical equivalent of the physical representation of each subtype, 
        compatible with CEN EN 13606 structures. Returns a List."""

class DataStructure(grok.Container):
    u"""
     Abstract parent class of all data structure types. Includes the as_hierarchy func-
    tion which can generate the equivalent CEN EN13606 single hierarchy for each
    subtype's physical representation. For example, the physical representation of an
    ITEM_LIST is List<ELEMENT>; its implementation of as_hierarchy will gener-
    ate a CLUSTER containing the set of ELEMENT nodes from the list.
    """

    implements(IDataStructure)
   
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links):
        Locatable.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)
    
    def asHierarchy():
        u"""Hierarchical equivalent of the physical representation of each subtype, 
        compatible with CEN EN 13606 structures. Returns a List."""


#Begin History package
class IEvent(Interface):
    u"""
    Defines the abstract notion of a single event in a series. This class is generic,allowing types 
    to be generated which are locked to particular spatial types, such as EVENT<ITEM_LIST> Subtypes 
    express point or interval data.
    """
    
    time=Object(
        schema=IDvDateTime,
        title=_(u'time'),
        description=_(u"""Time of this event. If the width is non-zero, it is the time point of the 
                         trailing edge of the event."""),
        required=True
    )
    
            
    data=Object(
        schema=IItemStructure,
        title=_(u'data'),
        description=_(u'The data of this event.'),
        required=True
    )
    
    state=Object(
        schema=IItemStructure,
        title=_(u'state'),
        description=_(u'Optional state information.for this event.'),
        required=False
    )
    
    parent=Object(
        schema=IObjectRef,
        title=_(u'parent'),
        description=_(u'redefinition of LOCATABLE.parent to type of History'),
        required=True
    )
    
    offset=Object(
        schema=IDvDuration,
        title=_(u'offset'),
        description=_(u'Offset of this event from origin, computed as time.diff(parent.origin)'),
        required=True
    )

    def offsetValidity(event):
        u'is the offset valid?' 

class Event(Locatable):
    u"""
    Defines the abstract notion of a single event in a series. This class is generic,allowing types 
    to be generated which are locked to particular spatial types, such as EVENT<ITEM_LIST> Subtypes 
    express point or interval data.
    """
    
    implements(IEvent)
    
    def __init__(self,time,data,state,parent,offset):
        self.time=time
        self.data=data
        self.state=state
        self.parent=parent
        self.offset=offset
    

    def offsetValidity(event):
        u"""is the offset valid?""" 
        
        
class IHistory(Interface):
    u"""
    Root object of a linear history, i.e. time series structure. For a periodic series of
    events, period will be set, and the time of each Event in the History must correspond; i.e. the EVENT.offset must be a multiple of period for each Event. Missing
    events in a period History are however allowed.
    
    NOTE: The invariants have NOT been written yet for this interface.
    """
    
    origin = Object(
        schema=IDvDateTime,
        title=_(u"origin"),
        description=_(u"Time origin of this event history. The first event is not necessarily at the origin point."),
        required=True
    )
    
    events = List(
        value_type = Object(schema=IEvent),
        title=_(u"events"),
        description=_(u"The events in the series."),
        required= False
    )
    
    
    period=Object(
        schema=IDvDuration,
        title=_(u"period"),
        description=_(u"Period between samples in this segment if periodic."),
        required=False
    )
    
    duration=Object(
        schema=IDvDuration,
        title=_(u"duration"),
        description=_(u"""Duration of the entire History; either corresponds to the duration of all 
                    the events, and/or the duration represented by the summary, if it exists."""),
        required=False
    )
    
    summary=Object(
        schema=IItemStructure,
        title=_(u"summary"),
        description=_(u"""Optional summary data expressing e.g. text or image which summarises 
                         entire History."""),
        required=False
    )
    
    def isPeriodic(): 
        u"""Indicates whether history is periodic. Returns Boolean"""
        
    def asHierarchy():
        u"""Returns CLUSTER. Generate a CEN EN13606-compatible hierarchy of the physical representation."""


        
class History(DataStructure):
    u"""
    Root object of a linear history, i.e. time series structure. For a periodic series of
    events, period will be set, and the time of each Event in the History must correspond; i.e. the EVENT.offset must be a multiple of period for each Event. Missing
    events in a period History are however allowed.
    
    NOTE: The invariants have NOT been written yet for this interface.
    """
    
    implements(IHistory)
    
    def __init__(self,origin,events,period,duration,summary):
        self.origin=origin
        self.events=events
        self.period=period
        self.duration=duration
        self.summary=summary
            
    def isPeriodic(): 
        u"""Indicates whether history is periodic. Returns Boolean"""
        
    def asHierarchy():
        u"""Returns CLUSTER. Generate a CEN EN13606-compatible hierarchy of the physical representation."""
        
        
class IIntervalEvent(Interface):
    u""" 
    Defines a single interval event in a series.
    """
    
    width=Object(
        schema=IDvDuration,
        title=_(u"width"),
        description=_(u"""Length of the interval during which the state was true. 
                      Void if an instantaneous event. OSHIP NOTE: The specs indicate 
                      this attribute is required but the text says it is Void if instantaneous.
                      How should this conflict be resolved?"""),
        required=True
    )
    
    mathFunction=Object(
        schema=IDvCodedText,
        title=_(u"mathFunction"),
        description=_(u"""Mathematical function of the data of this event, e.g. "maximum", "mean" etc. 
                      Coded using openEHR Terminology group "event math function"."""),
        required=True
    )
    
    sampleCount=Int(
        title=_(u"sampleCount"),
        description=_(u"""Optional count of original samples to which this event corresponds."""),
        required=False
    )
    
                              
    def intervalStartTime():
        u"""Start time of the interval of this event."""
         

         
class IntervalEvent(Event):
    u""" 
    Defines a single interval event in a series.
    
    """
    
    implements(IIntervalEvent)
    
    def __init__(self,width,mfunc,scount):
        self.width=width
        self.mathFunction=mfunc
        self.sampleCount=scount
                                      
    def intervalStartTime():
        u"""Start time of the interval of this event."""
  
class IPointEvent(Interface):
    u"""
    Defines a single point event in a series.
    """    
    pass

    
class PointEvent(Event):
    u"""
    Defines a single point event in a series.
    """    
    
    implements(IPointEvent)
    
    def __init__(self,time,data,state,parent,offset):
        Event.__init__(self,time,data,state,parent,offset)
  

#Begin Itemstructure package
class IItem(Interface):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """
    pass


class Item(Locatable):
    u"""
    The abstract parent of CLUSTER and ELEMENT representation classes.
    """
    
    implements(IItem)
    
    def __init__(self, uid, archetypeNodeId, name, archetypeDetails, feederAudit, links):
        Locatable.__init__(uid, archetypeNodeId, name, archetypeDetails, feederAudit, links)
 

class ItemStructure(DataStructure):
    u"""
    Abstract parent class of all spatial data types.
    """
    implements(IItemStructure)
    
    def __init__(self,uid,atnodeid,name,atdetails,fdraudit,links):
        DataStructure.__init__(self,uid,atnodeid,name,atdetails,fdraudit,links)    

class IElement(Interface):
    u"""The leaf variant of ITEM, to which a DATA_VALUE instance is attached."""
    
    value = Object(
        schema=IDataValue,
        title=_(u"value"),
        description=_(u"""Data value of this leaf."""),
        required=False
    )
    
    nullFlavor = Object(
        schema=IDvCodedText,
        title=_(u"""nullFlavor"""),
        description=_(u"""Flavor of null value, e.g. 'indeterminate', 'not asked', etc."""),
        required=False
    )
    
    def isNull():
        u"""Return True if value is unknown, etc."""
        
    def nullFlavorValid(obj):
        u"""If value is None then nullFlavor must be in the terminology code set for null flavors."""

class IItemList(Interface):
    u"""
    Logical list data structure, where each item has a value and can be referred to by a name 
    and a positional index in the list. The list may be empty.
    """
    
    items = List(
        value_type=Object(schema=IElement),
        title=_(u"items"),
        description=_(u"""Physical representation of the list."""),
        required=False
    )
    
    
    def itemCount():
        u"""Count of all items."""
        
    def names():
        u"""Return the names of all items."""
        
    def namedItem(str):
        u"""Return the named 'str'"""
        
    def ithItem(n):
        u"""Return the 'n' ith item."""
        
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""

class ItemList(ItemStructure):
    u"""
    Logical list data structure, where each item has a value and can be referred to by a name 
    and a positional index in the list. The list may be empty.
    """

    implements(IItemList)
    
    
    def __init__(self,items):
        self.item=items
      
    
    def itemCount():
        u"""Count of all items."""
        
    def names():
        u"""Return the names of all items."""
        
    def namedItem(str):
        u"""Return the named 'str'"""
        
    def ithItem(n):
        u"""Return the 'n' ith item."""
        
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""


class IItemSingle(Interface):
    u"""
    Logical single value data structure.
    Used to represent any data which is logically a single value, such as a person's height or weight.   
    """
    
    item = Object(
        schema=IElement,
        title=_(u"item"),
        description=_(u"""Single item."""),
        required=True
    )
    
    def asHierarchy():
        u"""
        Generate a CEN EN13606-compatible hierarchy consisting of a single ELEMENT.
        """
        
        
class ItemSingle(ItemStructure):
    u"""
    Logical single value data structure.
    Used to represent any data which is logically a single value, such as a person's height or weight.   
    """
    
    implements(IItemSingle)
    
    def __init__(self,item):
        self.item=item
        
    
    def asHierarchy():
        u"""
        Generate a CEN EN13606-compatible hierarchy consisting of a single ELEMENT.
        """
        
class ICluster(Interface):
    u"""
    The grouping variant of ITEM, which may contain further instances of ITEM, in an ordered list.
    """

    # the list contents should be restricted to schema = IItem,
    items = List(
        value_type=Object(schema=IItem),
        title=_(u"items"),
        description=_(u"""Ordered list of items - CLUSTER or ELEMENT objects - under this CLUSTER."""),
        required=True
    )


    
class IItemTable(Interface):
    u"""
        Logical relational database style table data structure, in which columns are
        named and ordered with respect to each other.
        Implemented using Cluster-per-row encoding. Each row Cluster must have an
        identical number of Elements, each of which in turn must have identical names
        and value types in the corresponding postions in each row.
        Some columns may be designated 'key' columns, containing key data for each
        row, in the manner of relational tables. This allows row-naming, where each row
        represents a body site, a blood antigen etc. All values in a column have the same
        data type.
        Used to represent any data which is logically a table of values, such as blood
        pressure, most protocols, many blood tests etc.
        Not used for time-based data, which should be represented with the temporal
        class HISTORY.. The table may be empty.
    """
        
    rows = List(
        value_type=Object(schema=ICluster),
        title=_(u"rows"),
        description=_(u"""Physical representation of the table as a list of CLUSTERs, 
                    each containing the data of one row of the table."""),
        required=False
    )
    
    def rowCount():
        u"""Return number of rows as an integer."""
        
    def columnCount():
        u"""Return the number of columns as an integer."""
        
    def rowNames():
        u"""Return the List of row names as DvText items."""
        
    def columnNames():
        u"""Return the List of column names as DvText items."""
        
    def ithRow(n):
        u"""Return the 'n' ith row as a Cluster."""
        
    def hasRowWithName(a_key):
        u"""Return True if a_key exists as a row name."""
        
    def hasColumnWithName(a_key):
        u"""Return True if a_key exists as a column name."""
         
        
    def namedRow(a_key):
        u"""Return the row whose first column has the name a_key."""
        
    def hasRowWithKeys(keys):
        u"""Return True if a row's first n columns contain the names of set of keys."""
        
    def rowWithKeys(keys):
        u"""Return the row whose first n columns contain the names in the set of keys."""

    def elementAtCell(i,j):
        u"""
        NOTE: In the specs this is called elementAtCellij. I think it should be changed. 
        Return the element at the intersection of column i and row j. i and j are integers.        
        """

    def elementAtNamedCell(row_key,col_key):
        u"""Return the element at the intersection or col_key and row_key """

    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""

class ItemTable(ItemStructure):
    u"""
        Logical relational database style table data structure, in which columns are
        named and ordered with respect to each other.
        Implemented using Cluster-per-row encoding. Each row Cluster must have an
        identical number of Elements, each of which in turn must have identical names
        and value types in the corresponding postions in each row.
        Some columns may be designated 'key' columns, containing key data for each
        row, in the manner of relational tables. This allows row-naming, where each row
        represents a body site, a blood antigen etc. All values in a column have the same
        data type.
        Used to represent any data which is logically a table of values, such as blood
        pressure, most protocols, many blood tests etc.
        Not used for time-based data, which should be represented with the temporal
        class HISTORY.. The table may be empty.
    """
      
    implements(IItemTable)
    
    def __init__(self,rows):
        self.rows=rows
    
    def rowCount():
        u"""Return number of rows as an integer."""
        
    def columnCount():
        u"""Return the number of columns as an integer."""
        
    def rowNames():
        u"""Return the List of row names as DvText items."""
        
    def columnNames():
        u"""Return the List of column names as DvText items."""
        
    def ithRow(n):
        u"""Return the 'n' ith row as a Cluster."""
        
    def hasRowWithName(a_key):
        u"""Return True if a_key exists as a row name."""
        
    def hasColumnWithName(a_key):
        u"""Return True if a_key exists as a column name."""
         
        
    def namedRow(a_key):
        u"""Return the row whose first column has the name a_key."""
        
    def hasRowWithKeys(keys):
        u"""Return True if a row's first n columns contain the names of set of keys."""
        
    def rowWithKeys(keys):
        u"""Return the row whose first n columns contain the names in the set of keys."""

    def elementAtCell(i,j):
        u"""
        NOTE: In the specs this is called elementAtCellij. I think it should be changed. 
        Return the element at the intersection of column i and row j. i and j are integers.        
        """

    def elementAtNamedCell(row_key,col_key):
        u"""Return the element at the intersection or col_key and row_key """

    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""

        
class IItemTree(Interface):
    u"""
    Logical tree data structure. 
    """
    
    # the list contents should be restricted to schema = IItem,
    items = List(
        value_type=Object(schema=IItem),
        title=_(u"items"),
        description=_(u"Physical representation of the tree."),
        required=False
    )
    
    def hasElementPath(a_path):
        u"""Return True if a_path is a valid leaf element path."""
        
    def elementAtPath(a_path):
        u"""Return the leaf element at the path; a_path."""
           
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""
    

    
class ItemTree(ItemStructure):
    u"""
    Logical tree data structure. The tree may be empty. Used to represent data which are 
    logically a tree such as audiology results, microbiology results, biochemistry results.
    """
    
    implements(IItemTree)
    
    def __init__(self,uid, atnodeid,name, atdetails, fdraudit, links, items):
        ItemStructure.__init__(self, uid, atnodeid, name, atdetails, fdraudit, links)
        self.items=items
   
    def hasElementPath(a_path):
        u"""Return True if a_path is a valid leaf element path."""        
        
    def elementAtPath(a_path):
        u"""Return the leaf element at the path, a_path."""
           
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""
    


class Cluster(Item):
    u"""
    The grouping variant of ITEM, which may contain further instances of ITEM, in an ordered list.
    """

    implements(ICluster)
    
    def __init__(self,uid, archetypeNodeId, name, archetypeDetails, feederAudit, links, items):
        Locatable.__init__(uid, archetypeNodeId, name, archetypeDetails, feederAudit, links)
        self.items=items

        
        

       
 
        
class IElement(Interface):
    u"""The leaf variant of ITEM, to which a DATA_VALUE instance is attached."""
    
    value = Object(
        schema=IDataValue,
        title=_(u"value"),
        description=_(u"""Data value of this leaf."""),
        required=False
    )
    
    nullFlavor = Object(
        schema=IDvCodedText,
        title=_(u"""nullFlavor"""),
        description=_(u"""Flavor of null value, e.g. 'indeterminate', 'not asked', etc."""),
        required=False
    )
    
    def isNull():
        u"""Return True if value is unknown, etc."""
        
    def nullFlavorValid(obj):
        u"""If value is None then nullFlavor must be in the terminology code set for null flavors."""
        
        
class Element(Item):
    u"""The leaf variant of ITEM, to which a DATA_VALUE instance is attached."""
 
    implements(IElement)
   
    def __init__(self,value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links):
        self.value=value
        self.nullFlavor=nullFlavor
        self.archetypeNodeId=self.__name__=nodeid
        self.uid=uid
        self.name=name
        self.archetypeDetails=atdetails
        self.feederAudit=fdraudit
        self.links=links
       
        
        
    def isNull():
        u"""Return True if value is unknown, etc."""
        return self.value == None
        
    def nullFlavorValid(obj):
        u"""If value is None then nullFlavor must be in the terminology code set for null flavors."""
        
        
        
       
        
