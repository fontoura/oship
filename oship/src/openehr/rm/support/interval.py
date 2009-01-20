__author__ = u'Jacob Page <jacob.h.page@gmail.com>'
__contributors__ = u'Fabricio Ferracioli <fabricioferracioli@gmail.com>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'

import copy

from zope.schema import Field


class Smallest:
  """Represents the smallest value
  
  This type doesn't do much; it implements a pseudo-value that's smaller
  than everything but itself.
  
  >>> negInf = Smallest()
  >>> smallest = Smallest()
  >>> -264 < negInf
  False
  >>> -264 == negInf
  False
  >>> -264 > negInf
  True
  >>> negInf < negInf
  False
  >>> negInf == smallest
  True
  """
  
  def __neg__(self):
    """Returns the largest value
    
    The opposite of negative infinity is infinity, the largest value.

    >>> print -Smallest()
    ~
    """
    return Largest()
    
  def __cmp__(self, other):
    """Compares this with another object
    
    Always indicates that self is less than other, unless both are of 
    type Smallest, in which case they are equal.
    
    >>> 0 < Smallest()
    False
    >>> -9999999 < Smallest()
    False
    >>> Smallest() < -9999999
    True
    >>> Smallest() < Smallest()
    False
    >>> Smallest() == Smallest()
    True
    """
    if other.__class__ == self.__class__:
        retval = 0
    else:
        retval = -1
    return retval
    
  def __str__(self):
      """Returns a printable representation of this value
      
      The string for the smallest number is -~, which means negative infinity.
      
      >>> print Smallest()
      -~
      """
      return "-~"
    
  def __repr__(self):
    """Returns an evaluable representation of the object
    
    The representation of the smallest number is -Inf, which means 
    negative infinity.

    >>> Smallest()
    -Inf
    """
    return "-Inf"
    
  def __hash__(self):
    "Returns a value that can be used for generating hashes"
    return 0x55555555

class Largest:
  """Class representing the universal largest value
  
  This type doesn't do much; it implements a pseudo-value that's larger
  than everything but itself.
  
  >>> infinity = Largest()
  >>> greatest = Largest()
  >>> 6234 < infinity
  True
  >>> 6234 == infinity
  False
  >>> 6234 > infinity
  False
  >>> infinity > infinity
  False
  >>> infinity == greatest
  True
  """
  
  def __neg__(self):
    """Returns the smallest universal value
    
    The opposite of infinity is negative infinity, the smallest value.

    >>> print -Largest()
    -~
    """
    return Smallest()
    
  def __cmp__(self, other):
    """Compares object with another object
    
    Always indicates that self is greater than other, unless both are of
    type Largest, in which case they are equal.
    
    >>> 0 > Largest()
    False
    >>> Largest() < 9999999
    False
    >>> Largest() > 9999999
    True
    >>> Largest() < Largest()
    False
    >>> Largest() == Largest()
    True
    """
    if other.__class__ == self.__class__:
        retval = 0
    else:
        retval = 1
    return retval

  def __str__(self):
      """Returns a string representation of the object
      
      The largest number is displayed as ~ (it sort of looks like infinity...)
      
      >>> print Largest()
      ~
      """
      return "~"
    
  def __repr__(self):
    """Returns an evaluable expression representing this object
    
    >>> Largest()
    Inf
    """
    return "Inf"

  def __hash__(self):
    "Returns a value that can be used for generating hashes"
    return -0x55555555
  

class Interval(object):
  def __init__(self, lower=Smallest(), upper=Largest(), lower_included=False, upper_included=False):
      self.__name__=''
      
      """Initializes an interval
      
      Parameters
      ==========
      - lower: The lower bound of an interval (default Smallest())
      - upper: The upper bound of an interval (default Largest())
      - lower_included: Boolean telling if the lower value of interval are included (default True).
      - upper_included: Boolean telling if the greater value of interval are included (default True)
      
      An Interval can represent an infinite set.

      >>> r = Interval() # All values
      >>> r.has(0)
      True

      An Interval can represent sets unbounded on an end.

      >>> r = Interval(0,5)
      >>> r.has(-1)
      True
      >>> r.has(3)
      True
      >>> r.has(5.1)
      False

      An Interval can represent a set of values up to, but not including a
      value.

      >>> r = Interval(25, 28, False)
      >>> r.has(25)
      False
      >>> r.has(28)
      True

      An Interval can represent a set of values that have an inclusive
      boundary.

      >>> r = Interval(29, 216)

      An Interval can represent a single value

      >>> r = Interval(82, 82)
      >>> r.has(82)
      True

      Intervals that are not normalized, gives an exception.

      >>> r = Interval(4, 1)

      Intervals can represent an empty set.

      >>> r = Interval(5, 5, False, False)
      """
      if (lower == None or upper == None):
        raise ValueError('lower and upper must not be None')
      
      if (not isinstance(lower, Smallest) and not isinstance(upper, Largest)):
        if (type(lower) != type(upper)):
          raise TypeError('lower and upper must be of the same type')
      if (not callable(getattr(lower, '__cmp__')) or not callable(getattr(upper, '__cmp__'))):
        raise NotImplementedError('Classes are not comparable. Implement __cmp__ methods')
      
      if (lower > upper):
        raise ValueError('lower must be less than or equal to upper')
      
      if (lower_included and isinstance(lower, Smallest)):
        raise ValueError('lower_included implies lower greater than -Inf')
      
      if(upper_included and isinstance(upper, Largest)):
        raise ValueError('upper_included implies upper greater than Inf')
      
      self.lower = lower 
      if (isinstance(lower, Smallest)):
        self.lower_unbounded = True
      else:
        self.lower_unbounded = False
      self.lower_included = lower_included
      
      self.upper = upper
      if (isinstance(upper, Largest)):
        self.upper_unbounded = True
      else:
        self.upper_unbounded = False
      self.upper_included = upper_included

  def __hash__(self):
    """Returns a hashed value of the object
    
    Intervals are to be considered immutable.  Thus, a 32-bit hash can
    be generated for them.
    """
    return hash((self.lower_unbounded, self.upper_unbounded, self.lower, self.upper))
      
  def __repr__(self):
    """Returns an evaluable expression that can reproduce the object
        
    >>> Interval(3, 6)
    Interval(lower=3, upper=6, lower_unbounded=False, upper_unbounded=False, lower_included=True, upper_included=True)
        """
    return "Interval(lower=%s, upper=%s, lower_unbounded=%s, upper_unbounded=%s, lower_included=%s, upper_included=%s)" % (
      repr(self.lower), repr(self.upper), repr(self.lower_unbounded), repr(self.upper_unbounded), repr(self.lower_included), repr(self.upper_included))

  def has(self, value):
    """
    Returns if a value is inside the interval
    >>> interval = Interval(0,2)
    >>> interval.has(4)
    False
    >>> interval.has(1.5)
    True
    
    """

    if (value == None):
      raise ValueError('value must not be None')
    
    if (type(value) == type(self)):
      raise TypeError('value must be of the same type as self')
    
    #the value is between Smallest and Largest
    if (isinstance(self.lower, Smallest) and isinstance(self.upper, Largest)):
      return True
    #Smallest is the value of self.lower and upper is finite, need to test the value of upper
    elif (isinstance(self.lower, Smallest)):
      if (value < self.upper):
        return True
      else:
        #test for the upper closed interval
        return self.upper_included and value == self.upper
    #Largest is the value of self.upper and lower is finite, need to test the value of lower
    elif (isinstance(self.upper, Largest)):
      if (value > self.lower):
        return True
      else:
        #test for the lower closed interval
        return self.lower_included and value == self.lower
    else:
      #test for intervals that upper and lower values are finite
      if (value > self.lower and value < self.upper):
        return True
      else:
      #test for closed values
        if (self.lower_included and value == self.lower):
          return True
        elif (self.upper_included and value == self.upper):
          return True
        else:       
          return False 