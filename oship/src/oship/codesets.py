##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

This is a set of utility functions to return various code sets.  
In implementation they will be tied to data sources.

"""

__author__  = 'Timothy Cook <tw_cook@comcast.net>'
__docformat__ = 'plaintext'


def languages():
    """ 
    Define where to get the valid language codes from. 
    This is currently just a stub.    
    """
    
    return ['en','es','fr','de'] 


def characterSets():
    """ 
    Define where to get the valid character sets from. 
    This is currently just a stub.    
    """
    
    return ['8859-1','8859-10','KIO8-R'] 


def nullFlavors():
    nfList = ["Unknown", "Not Asked", "Indeterminate", "Refused Reply"]
    return nfList
