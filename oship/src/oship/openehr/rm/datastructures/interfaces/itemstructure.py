# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


u"""

These are the interface specifications from Data Structures Information Model
 Item Structure Package Rev. 2.1.0.

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


from openehr.rm.datastructures.interfaces.datastructure import IDataStructure
from openehr.rm.datastructures.representation import Element

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')



class IItemStructure(IDataStructure):
    u"""
    Abstract parent class of all spatial data types.
    """

class IItemSingle(IItemStructure):
    u"""
    Logical single value data structure.
    Used to represent any data which is logically a single value, such as a person’s height or weight.   
    """
    
    item = Element(
        title=_(u"""item"""),
        description=_(u"""Single item."""),
        required=True
    )
    
    def asHierarchy():
        u"""
        Generate a CEN EN13606-compatible hierarchy consisting of a single ELEMENT.
        """
    
class IItemList(IItemStructure):
    u"""
    Logical list data structure, where each item has a value and can be referred to by a name 
    and a positional index in the list. The list may be empty.
    """
    
    items = List(
        title=_(u"""items"""),
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
        
class IItemTable(IItemStructure):
    u"""
        Logical relational database style table data structure, in which columns are
        named and ordered with respect to each other.
        Implemented using Cluster-per-row encoding. Each row Cluster must have an
        identical number of Elements, each of which in turn must have identical names
        and value types in the corresponding postions in each row.
        Some columns may be designated ‘key’ columns, containing key data for each
        row, in the manner of relational tables. This allows row-naming, where each row
        represents a body site, a blood antigen etc. All values in a column have the same
        data type.
        Used to represent any data which is logically a table of values, such as blood
        pressure, most protocols, many blood tests etc.
        Not used for time-based data, which should be represented with the temporal
        class HISTORY.. The table may be empty.
    """
        
    rows = List(
        title=_(u"""rows"""),
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

class IItemTree(IItemStructure):
    u"""
    Logical tree data structure. The tree may be empty. Used to represent data which are 
    logically a tree such as audiology results, microbiology results, biochemistry results.
    """
    
    items = List(
        title=_(u"""items"""),
        description=_(u"""Physical representation of the tree."""),
        required=False
    )
    
    
    def hasElementPath(a_path):
        u"""Return True if a_path is a valid leaf element path."""
        
    def elementAtPath(a_path):
        u"""Return the leaf element at the path; a_path."""
           
    def asHierarchy():
        u"""Generate a CEN EN13606-compatible hierarchy consisting of a single CLUSTER containing the ELEMENTs of this list."""
    
