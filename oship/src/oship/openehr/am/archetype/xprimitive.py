# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
These are the implementations for the am.archetype.primitive package defined in 
The Archetype Object model Rev 2.0.2
"""
__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from openehr.am.archetype.interfaces.primitive import *

class CPrimitive(Interface):
    """
    Abstract super type of all primitive types.
    """
    
    implements(ICPrimitive)
    

    def validValue(aVal):
        """
        True if aValue is valid with respect to the expressed constraint.
        """
        
class CBoolean(CPrimitive):
    """
    Boolean constraint.
    """
    
    implements(ICBoolean)
    
    

class CInteger(CPrimitive):
    """
    Constraint on integers.
    """
    
    implements(ICInteger)
    
    

class CReal(CPrimitive):
    """
    Constraints on instances of Real
    """
    
    implements(ICReal)
    

class CDate(CPrimitive):
    """
    ISO 8601 compatible constraint on instances of Date.
    """
    
    implements(ICDate)
    



    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """


class CTime(CPrimitive):
    """
    ISO 8601 compatible constraint on instances of Time.
    """
    
    implements(ICTime)
    

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """


class CDateTime(CPrimitive):
    """
    ISO 8601 compatible constraint on instances of DateTime.
    """
    
    implements(ICDateTime)
    

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """

class CDuration(CPrimitive):
    """
    Constraints on durations.  openEHR allows the 'W' indicator to be mixed in.
    """
    
    implements(ICDuration)
    
