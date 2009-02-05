# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

From the uri data types from Data Types Information Model
URI Package Rev. 2.1.0.

"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'

from zope.i18nmessageid import MessageFactory

from dvuri import IDvUri

_ = MessageFactory('oship')


        
class IDvEhrUri(IDvUri):
    """
    A DvEhrUri is a DvUri which has the scheme name "ehr", and which can only reference 
    elements in EHRs. The syntax is described below.
    
    Used to reference elements in an EHR, which may be the current one, or another.
    
    The syntax of a DV_EHR_URI is an openEHR path, inside the "ehr" URI scheme-space, and is 
    of the form: "ehr://" ehr_path
    The syntax of ehr_path is described in the section on Paths in The openEHR Architecture Overview 
    document. DV_EHR_URIs are used as a mechanism for referencing in the EHR, ensuring readability by 
    humans, as well as validity when extracts are transmitted elsewhere: even if the target of a path 
    is not present, the path can be used to locate the missing item on demand.
    """
    
    def schemeIsEhr():
        """ Ensure scheme == 'ehr' """
        