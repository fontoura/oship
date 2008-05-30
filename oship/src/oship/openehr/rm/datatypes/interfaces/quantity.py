##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################



"""

These are the quantity data types interfaces from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import *
from zope.schema import *
from zope.schema.interfaces import IOrderable
from openehr.rm.datatypes.text import *

from openehr.rm.datatypes.interfaces.basic import *
from openehr.rm.datatypes.interfaces.text import *
from openehr.rm.datatypes.text import *
from openehr.rm.datatypes.basic import *

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')



class IDvOrdered(IOrderable):
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
    
    normalRange = List(
        title = _(u"normalRange"),
        description = _(u"""Optional normal range."""),
        required = False
        )
    
    otherReferenceRanges = List(
        title = _(u"otherReferenceRanges"),
        description = _(u"""Optional tagged other reference ranges for this value in 
                      its particular measurement context. A list of ReferenceRange types."""),
        required = False
        )
    
    normalStatus = Tuple(
        title = _(u"normalStatus"),
        description = _(u"""Optional normal status indicator of value with respect to normal 
                     range for this value. Often included by lab, even if the normal range 
                     itself is not included. Coded by ordinals in series HHH, HH, H, 
                     (nothing), L, LL, LLL; see openEHR terminology group normal status."""),
        required = False
    )
                
       
    def isStrictlyComparableTo(other):
        """Test if two instances are strictly comparable. Called by object.__cmp__"""


    def isNormal():
        """ 
        Value is in the normal range, determined by comparison of the value to the normalRange 
        if present, or by the normalStatus marker if present.

        isNormal: Boolean
        require
        normalRange /= Void or normalStatus /= Void
        ensure
        normalRange /= Void implies Result = normalRange.has(Current)
        normalStatus /= Void implies normal_status.code_string.is_equal(N)
        """
        
        
    def isSimple():
        """
        is_simple: Boolean 
        True if this quantity has no reference ranges.
        """
                  
        
          
class IDvInterval(IDataValue):
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
    


class IReferenceRange(IDvOrdered):
    """
    Defines a named range to be associated with any ORDERED datum. Each such
    range is particular to the patient and context, e.g. sex, age, and any other factor
    which affects ranges.
    May be used to represent normal, therapeutic, dangerous, critical etc ranges.
    """
    
    meaning =TextLine(
        title=_(u"meaning"),
        description=_(u"""Term whose value indicates the meaning of this range, 
                     e.g. normal, critical, therapeutic etc."""),
        required=True
        )
    
    range = List(
        title=_(u"range"),
        description=_(u"""The data range for this meaning, e.g.critical etc."""),
        required=True
        )
    

        
    

    def isInRange(val):
        """
        Indicates if the value val is inside the range
        """
        

            
        
class IDvOrdinal(IDvOrdered):
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
    
    value = Int(
        title=_(u"value"),
        description=_(u""" Ordinal position in enumeration of values. """),
        required=True
    )
    
    symbol = List(
        title=_(u"symbol"),
        description=_(u"""Coded textual representation of this 
                       value in the enumeration, which may be strings made from + symbols, 
                       or other enumerations of terms such as mild, moderate, severe,
                       or even the same number series as the values,
                       e.g. 1, 2, 3. Codes come from archetype."""),
        required=True
    )


    def referenceRange():
        """
        limits of the ordinal enumeration, to allow
        comparison of an ordinal value to its limits.
        Returns DvOrdinal.
        """

    def isStrictlyComparableTo(self, other):
        """        
        True if symbols come from same vocabulary,assuming the vocabulary is a 
        subset or value range, e.g. urine:protein.
        
        (other: like Current): Boolean 
        ensure
        symbol.is_comparable (other.symbol) implies Result
        """
             
class IDvQuantified(IDvOrdered):
    """
    Abstract class defining the concept of true quantified values, i.e. values which are
    not only ordered, but which have a precise magnitude.
    """
    
    magnitude = Float(
        title=_(u"magnitude"),
        description=_(u"""Numeric value of the quantity in canonical (i.e. single value)
                          form. Implemented as constant, function or attribute in subtypes as
                          appropriate. The type OrdereNumeric is mapped to the available 
                          appropriate type in each implementation technology."""),
        required=True
    )
      
    magnitudeStatus = List(
        title=_(u"magnitudeStatus"),
        description=_(u"""Optional status of magnitude with values:
                                = : magnitude is a point value
                                < : value is < magnitude
                                > : value is > magnitude
                                <= : value is <= magnitude
                                >= : value is >= magnitude
                                ~ : value is approximately magnitude
                                If not present, meaning is =. """),
        required=True
    )
    
           
           
    def validMagnitudeStatus(val):
        """
        Test whether a string 'val' is one of the valid values for the magnitude_status attribute.
        """


    magnitudeExists = Attribute(_(u" magnitude /= Void"))
    
    magnitudeStatusValid = Attribute(_(u"""magnitude_status /= Void implies
                                     valid_magnitude_status(magnitude_status)"""))



class IDvAmount(IDvQuantified):
    """   
    Abstract class defining the concept of relative quantified amounts. For relative
    quantities, the + and - operators are defined (unlike descendants of
    DV_ABSOLUTE_QUANTITY, such as the date/time types).
    """

    accuracy = Int(
        title=_(u"accuracy"),
        description=_(u"""Accuracy of measurement, expressed either as a half-range 
                         percent value (accuracyIsPercent = True) or a half-range
                         quantity. A value of 0 means that accuracy was not recorded."""),
        required=False
    )

  
    accuracyIsPercent = Bool(
        title=_(u"accuracyIsPercent"),
        description=_(u"""If True, indicates that when this object was created, accuracy was recorded 
                    as a percent value; if False, as an absolute quantity value."""),
        required=False
    )

    
    def validPercentage(val):
        """
        Test whether a number is a valid percentage,i.e. between 0 and 100.
        ensure
        Result implies val >= 0.0 and val <= 100.0
        """
        
        
    
class IDvQuantity(IDvAmount):
    """
    Quantitified type representing scientific quantities, i.e. quantities expressed as a
    magnitude and units.
    Units were inspired by the Unified Code for Units of Measure (UCUM), devel-
    oped by Gunther Schadow and Clement J. McDonald of The Regenstrief Institute.
        
    Can also be used for time durations, where it is more convenient to treat these as
    simply a number of seconds rather than days, months, years.
    """

    magnitude = Float(
        title=_(u"Magnitude"),
        description=_(u"""Numeric magnitude of the quantity."""),
        required=True
        )
    
    units = TextLine(
        title=_(u"Units"),
        description=_(u"""Stringified units, expressed in UCUM unit syntax, 
                    e.g. "kg/m2", "mm[Hg]", "ms-1", "km/h".Implemented accordingly in subtypes."""),
        required=True, # constraint = validUnits() -- see below
        )

    
    precision = Int(
        title=_(u"Precision"),
        description=_(u"""Precision to which the value of the quantity is expressed, in terms of 
                    number of decimal places. The value 0 implies an integral quantity.
                    The value -1 implies no limit, i.e. any number of decimal places."""),
        required=False
        )
    
    def validUnits():
        """Not implemented but needs to return a list of valid unit identifiers."""
        pass
    
    def isIntegral():
        """True if precision = 0; quantity represents an integral number."""

    
    def isStrictlyComparableTo(other):
        """Test if two instances are strictly comparable by ensuring that the measured 
        property is the same, achieved using the Measurement service function units_equivalent.
        
        Return selfunits == other.units
        """
        
    def validUnits(value):
        """
        This is a custom constraint to test that the units value adheres to the specified BNF.
        """

class IDvCount(IDvAmount):
    """        
    Purpose: Countable quantities
         
             Used for countable types such as pregnancies and steps (taken by a physiotherapy
    Use:     patient), number of cigarettes smoked in a day.

    Misuse:  Not used for amounts of physical entities (which all have units)
    """
    
    magnitude = Int(
        title=_(u"Magnitude"),
        description=_(u"""numeric magnitude of the quantity"""),
        required=True
        )
    
class IProportionKind(Interface):
    """
    Class of enumeration constants defining types of proportion for the
    DV_PROPORTION class.
    """


    def validProportionKind(n):
        """
        True if n is one of the defined types.
        """
        
    
class IDvProportion(IDvAmount, IProportionKind):
    """
              Models a ratio of values, i.e. where the numerator and denominator are both pure
    Purpose:  numbers.
    
              Used for recording titers (e.g. 1:128), concentration ratios, e.g. Na:K (unitary
      Use:    denominator), albumin:creatinine ratio, and percentages, e.g. red cell distirbution
              width (RDW).
        
              Should not be used to represent things like blood pressure which are often written
              using a / character, giving the misleading impression that the item is a ratio,
    MisUse:   when in fact it is a structured value. E.g. visual acuity 6/24 is not a ratio.
              Should not be used for formulations.
    """
    
    
    numerator = Float(
        title=_(u"numerator"),
        description=_(u"""numerator of ratio"""),
        required=True
    )
    
    denominator = Float(
        title=_(u"denominator"),
        description=_(u"""denominator of ratio"""),
        required=True
    )
    
    type = Int(
        title=_(u"type"),
        description=_(u"""Indicates semantic type of proportion, including percent, unitary etc."""),
        required=True
    )
    
    precision = Int(
        title=_(u"precision"),
        description=_(u"""Precision to which the numerator and denominator values of the proportion 
                    are expressed, in terms of number of decimal places. The value 0 implies an 
                    integral quantity. The value -1 implies no limit, i.e.any number of decimal places."""),
        required=False
    )
    
    
    def isIntegral():
        """
        True if the numerator and denominator values are integers, i.e. if the precision is 0.
        """

    def magnitude():
        """
        Effective magnitude represented by ratio.
        Result = numerator / denominator
        """  
    
        
class IDvAbsoluteQuantity(IDvQuantified):
    """
    Abstract class defining the concept of quantified entities whose values are abso-
    lute with respect to an origin. Dates and Times are the main example.
    """
    
        
    accuracy = Float(
        title=_(u"Accuracy"),
        description=_(u"""Accuracy of measurement, expressed as a half-range value of the diff type 
                    for this quantity (i.e. an accuracy of x means +/−x)."""),
        required=False,
        )
    
