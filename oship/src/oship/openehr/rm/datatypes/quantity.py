# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

These are the quantity data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'restructuredtext'

from zope.i18nmessageid.message import MessageFactory 
from zope.schema import *

from openehr.rm.datatypes.interfaces.quantity import *
from openehr.rm.datatypes.basic import *
from openehr.rm.datatypes.text import *

_ = MessageFactory('oship')

class DvOrdered(DataValue):
    """
    Purpose:           
    Abstract class defining the concept of ordered values, which includes ordinals as
    well as true quantities. It defines the functions ‘<’ and is_strictly_comparable_to,
    the latter of which must evaluate to True for instances being compared with the
    ‘<’ function, or used as limits in the DV_INTERVAL<T> class.

    Use:    
    Data value types which are to be used as limits in the DV_INTERVAL<T> class
    must inherit from this class, and implement the function
    is_strictly_comparable_to to ensure that instances compare meaningfully. For
    example, instances of DV_QUANTITY can only be compared if they measure the
    same kind of physical quantity.
    """
    
    def __init__(self, normalRange, otherReferenceRanges, normalStatus):
        self.normalRange = normalRange
        self.otherReferenceRanges = otherReferenceRanges
        self.normalStatus = normalStatus
                
    def __cmp__(self,other):
        isStrictlyComparableTo(other)
        
                
    def __lt__(self, other):
        if isinstance(other,self.__class__):
            return self.__dict__ < other.__dict__
        else:
            return False
        
    def isStrictlyComparableTo(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
        

    def isNormal(self):
        """ 
        Value is in the normal range, determined by comparison of the value to the normalRange 
        if present, or by the normalStatus marker if present.

        isNormal: Boolean
        require
        normalRange /= Void or normalStatus /= Void
        ensure
        normalRange /= Void implies Result = normalRange.has(Current)
        normalStatus /= Void implies normal_status.code_string.is_equal(“N”)
        """
        
        if self.normalStatus.codeString == "N":
            return True
        else:
            return self.value in self.normalRange # but we don't have a value in this abstract class in the specs
        
        
    def isSimple(self):
        """
        is_simple: Boolean 
        True if this quantity has no reference ranges.
        """
        if (self.normalRange is None or self.normalRange is []) \
           and (self.otherReferenceRanges is None or self.otherReferenceRanges is []):
            return True
        else:
            return False
                  
        
          
class DvInterval(DataValue):
    """
    Used to define intervals of dates, times, quantities (whose units match) and so on.
    The type parameter, T, must be a descendant of the type DV_ORDERED, which is
    necessary (but not sufficient) for instances to be compared (strictly_comparable
    is also needed).
    Without the DV_INTERVAL class, quite a few more DV_ classes would be needed
    to express logical intervals, namely interval versions of all the date/time classes,
    and of quantity classes. Further, it allows the semantics of intervals to be stated in
    one place unequivocally, including the conditions for strict comparison.
    The basic semantics are derived from the class INTERVAL<T>, described in the
    support RM.

    """
    
    pass 

class ReferenceRange(DvOrdered):
    """
    Defines a named range to be associated with any ORDERED datum. Each such
    range is particular to the patient and context, e.g. sex, age, and any other factor
    which affects ranges.
    May be used to represent normal, therapeutic, dangerous, critical etc ranges.
    """
    
    def __init__(self, meaning, range,**kwargs):
        self.meaning = meaning
        self.range = range
        Field.__init__(self,**kwargs)


    def isInRange(val):
        """
        Indicates if the value ‘val’ is inside the range
        """
        

            
        
class DvOrdinal(DvOrdered):
    """
    Models rankings and scores, e.g. pain, Apgar values, etc, where there is a)
    implied ordering, b) no implication that the distance between each value is con-
    stant, and c) the total number of values is finite.

    Used for recording any clinical datum which is customarily recorded using sym-
    bolic values. Example: the results on a urinalysis strip, e.g. {neg, trace, +,
    ++, +++} are used for leucocytes, protein, nitrites etc; for non-haemolysed
    blood {neg, trace, moderate}; for haemolysed blood {neg, trace,
    small, moderate, large}.
    """

    def __init__(self,value,symbol,**kwargs):
        self.value=value
        self.symbol=symbol
        Field.__init__(self,**kwargs)

    def referenceRange():
        """
        limits of the ordinal enumeration, to allow
        comparison of an ordinal value to its limits.
        Returns DvOrdinal.
        """

    def isStrictlyComparableTo(self, other):
        """        
        True if symbols come from same vocabulary,assuming the vocabulary is a 
        subset or value range, e.g. “urine:protein”.
        
        (other: like Current): Boolean 
        ensure
        symbol.is_comparable (other.symbol) implies Result
        """
             
class DvQuantified(DvOrdered):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """

    def __init__(self,magnitude,magnitudeStatus,**kwargs):
        self.magnitude=magnitude
        self.magnitudeStatus=magnitudeStatus
        self.magnitudeExists=magnitude!=None       
        Field.__init__(self,**kwargs)

    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """
        magnitudeStatusValid=(val in self.magnitudeStatus)
        return magnitudeStatusValid


class DvAmount(DvQuantified):
    """   
    Abstract class defining the concept of relative quantified ‘amounts’. For relative
    quantities, the ‘+’ and ‘-’ operators are defined (unlike descendants of
    DV_ABSOLUTE_QUANTITY, such as the date/time types).
    """
    
    implements(IDvAmount)
    
    def __init__(self,accuracy,accuracyIsPercent,**kwargs):
        self.accuracy=accuracy
        self.accuracyIsPercent=accuracyIsPercent
        Field.__init__(self,**kwargs)

    
    def validPercentage(val):
        """
        Test whether a number is a valid percentage,i.e. between 0 and 100.
        ensure
        Result implies val >= 0.0 and val <= 100.0
        """
        
        return val>=0 and val<=100
                
    
class DvQuantity(DvAmount):
    """
    Quantitified type representing “scientific” quantities, i.e. quantities expressed as a
    magnitude and units.
    Units were inspired by the Unified Code for Units of Measure (UCUM), devel-
    oped by Gunther Schadow and Clement J. McDonald of The Regenstrief Institute.
        
    Can also be used for time durations, where it is more convenient to treat these as
    simply a number of seconds rather than days, months, years.
    """
    
    implements(IDvQuantity)
    
    def __init__(self,magnitude,units,precision,**kwargs):
        self.magnitude=magnitude
        self.units=units
        self.precision=precision
        Field.__init__(self,**kwargs)

    def isIntegral():
        """True if precision = 0; quantity represents an integral number."""
        return precision==0

    
    def isStrictlyComparableTo(other):
        """
        Test if two instances are strictly comparable by ensuring that the measured 
        property is the same, achieved using the Measurement service function units_equivalent.
        """
        return self.units==other.units and self.magnitude==other.magnitude
      
class DvCount(DvAmount):
    """        
    Purpose: Countable quantities
         
             Used for countable types such as pregnancies and steps (taken by a physiotherapy
    Use:     patient), number of cigarettes smoked in a day.

    Misuse:  Not used for amounts of physical entities (which all have units)
    """
    
    implements(IDvCount)
    
    def __init__(self,magnitude,**kwargs):
        self.magnitude=magnitude
        Field.__init__(self,**kwargs)

class DvProportion(DvAmount):
    """
              Models a ratio of values, i.e. where the numerator and denominator are both pure
    Purpose:  numbers.
    
              Used for recording titers (e.g. 1:128), concentration ratios, e.g. Na:K (unitary
      Use:    denominator), albumin:creatinine ratio, and percentages, e.g. red cell distirbution
              width (RDW).
        
              Should not be used to represent things like blood pressure which are often written
              using a ‘/’ character, giving the misleading impression that the item is a ratio,
    MisUse:   when in fact it is a structured value. E.g. visual acuity “6/24” is not a ratio.
              Should not be used for formulations.
    """

    implements(IDvProportion)
    
    def __init__(self, numerator, denominator, type, precision,**kwargs):
        if isinstance(numerator, float) or isinstance(numerator, int):
            self.numerator = numerator
        else:
            raise AttributeError, "Invalid numerator value."
        
        if isinstance(denominator, float) or isinstance(denominator,int):
            self.denominator = denominator
        else:
            raise AttributeError, "Invalid denominator value."
        
        self.type = type
        
        if precision != None:
            if isinstance(precision,int):
                self.precision = precision
            else:
                raise AttributeError, "Invalid precision value."
        Field.__init__(self,**kwargs)
            
            
    def isIntegral():
        """
        True if the numerator and denominator values are integers, i.e. if the precision is 0.
        """
        return isinstance(self.numerator,int) and isinstance(self.denominator,int) 

    def magnitude():
        """
        Effective magnitude represented by ratio.
        Result = numerator / denominator
        """  
        return self.numerator / self.denominator
    
class ProportionKind(Field):
    """
    Class of enumeration constants defining types of proportion for the
    DV_PROPORTION class.
    """
    def __init__(self,**kwargs):
        self.pkRatio = 0
        self.pkUnitary = 1
        self.pkPercent = 2
        self.pkFraction = 3
        self.pkIntegerFraction = 4
        Field.__init__(self,**kwargs)

    def validProportionKind(n):
        """
        True if n is one of the defined types.
        """
        return n in (pkRatio,pkUnitary,pkPercent,pkFraction,pkIntegerFraction)
        
        
class DvAbsoluteQuantity(DvQuantified):
    """
    Abstract class defining the concept of quantified entities whose values are abso-
    lute with respect to an origin. Dates and Times are the main example.
    """
    
    implements(IDvAbsoluteQuantity)
    
    def __init__(self,accuracy,**kwargs):
        self.accuracy=accuracy
        Field.__init__(self,**kwargs)

 