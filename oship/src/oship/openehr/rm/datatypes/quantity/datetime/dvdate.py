# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
From Data Types Information Model
Quantity Package Rev. 2.1.0.

In the specs the package is shown as data_types.quantity.date_time We have changed it 
in this implementation to datatypes.datetime

"""

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Andre Goncalves <golcalves.aluiz@gmail.com>', u'Fabricio Ferracioli <fabricioferracioli@gmail.com>', u'Roberto Cunha <roliveiracunha@yahoo.com.br>', u'Sergio Miranda Freire <sergio@lampada.uerj.br>'


from datetime import time, date


from zope.interface import implements 
from zope.i18nmessageid.message import MessageFactory

from oship.openehr.rm.datatypes.quantity.datetime.dvtemporal import DvTemporal
from oship.openehr.rm.datatypes.quantity.datetime.dvduration import DvDuration
from oship.openehr.rm.datatypes.quantity.datetime.interfaces.dvdate import IDvDate

_ = MessageFactory('oship')
        
class DvDate(DvTemporal):
    """
    Represents an absolute point in time, as measured on the Gregorian calendar, and
    specified only to the day. Semantics defined by ISO 8601.
    Used for recording dates in real world time. The partial form is used for 
    approximate birth dates, dates of death, etc.   
    """

    implements(IDvDate)

    def __init__(self,value):
        #try:
            #value = string.replace(value, ' ', '-')
            #value = string.replace(value, '/', '-')
            #self.value = time.strptime(value, '%Y-%m-%d')
        #except Exception:
            #raise ValueError('Incorrect date format. Date must be YYYY-MM-DD')            
        try:
            d=value.split('-')
            self.value = date(int(d[0]),int(d[1]),int(d[2]))
        except Exception:
            raise ValueError('Incorrect date format. Date must be YYYY-MM-DD')
    

    def diff(other):
        """Difference of two dates. Returns a Dv_Duration"""
        return DvDuration(other,self.value)
        
    def magnitude():
        """ Returns the numeric value of the date as days since the calendar origin point 1/1/0000"""
        return date(value.tm_year, value.tm_mon, value.tm_mday).toordinal()
