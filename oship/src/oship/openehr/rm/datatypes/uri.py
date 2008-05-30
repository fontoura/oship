# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""

These are the interfaces for the uri data types from Data Types Information Model
Quantity Package Rev. 2.1.0.

"""


__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.schema import Text, TextLine, Field

from openehr.rm.datatypes.basic import DataValue
from openehr.rm.datatypes.interfaces.uri import *  


class DvUri(DataValue):
    """A reference to an object which conforms to the Universal Resource Identifier
    (URI) standard, as defined by W3C RFC 2936. See "Universal Resource Identifiers in WWW"
    by Tim Berners-Lee at http://www.ietf.org/rfc/rfc2396.txt. This is a World-Wide Web RFC 
    for global identification of resources. See http://www.w3.org/Addressing for a starting 
    point on URIs. See http://www.ietf.org/rfc/rfc2806.txt for new URI types like telephone, 
    fax and modem numbers.
    
    Enables external resources to be referenced from within the content of the EHR. A number 
    of functions return the logical subparts of the URI string."""
    
    implements(IDvUri)

    def __init__(self, value,scheme,path,fragmentId,query,**kwargs):
        self.value = value
        self.scheme=scheme
        self.path=path
        self.fragmentId=fragmentId
        self.query=query
        Field.__init__(self,**kwargs)

    
    def scheme():
        """A distributed information "space" in which information objects exist. The scheme 
        simultaneously specifies an information space and a mechanism for accessing objects 
        in that space. For example if scheme = "ftp", it identifies the information space in 
        which all ftpable objects exist, and also the application - ftp - which can be used 
        to access them. Values may include: "ftp", "telnet", "mailto", "gopher" and many others. 
        Refer to WWW URI RFC for a full list. New information spaces can be accommodated within 
        the URI specification."""
        
    def path():
        u"""A string whose format is a function of the scheme. Identifies the location in 
        <scheme>-space of an information entity. Typical values include hierarchical directory 
        paths for any machine. For example, with scheme = "ftp", path might be /pub/images/image_01. 
        The strings "." and ".." are reserved for use in the path. Paths may include internet/intranet 
        location identifiers of the form: sub_domain...domain, e.g. "info.cern.ch" """

    def fragmentId():
        u"""A part of, a fragment or a sub-function within an object. Allows references to sub-parts 
        of objects, such as a certain line and character position in a text object. The syntax and 
        semantics are defined by the application responsible for the object. """


    def query():
        u"""Query string to send to application implied by scheme and path Enables queries to 
        applications, including databases to be included in the URI Any query meaningful to the 
        server, including SQL."""
        

    def valueExists():
        u"""value != None and value != '' """
        
        
class DvEhrUri(DvUri):
    u"""
    A DvEhrUri is a DvUri which has the scheme name ehr, and which can only reference 
    elements in EHRs. The syntax is described below.
    
    Used to reference elements in an EHR, which may be the current one, or another.
    
    The syntax of a DV_EHR_URI is an openEHR path, inside the ehr URI scheme-space, and is 
    of the form: ehr:// ehr_path
    The syntax of ehr_path is described in the section on Paths in The openEHR Architecture Overview 
    document. DV_EHR_URIs are used as a mechanism for referencing in the EHR, ensuring readability by 
    humans, as well as validity when extracts are transmitted elsewhere: even if the target of a path 
    is not present, the path can be used to locate the missing item on demand.
    """
    def __init__(self, value,scheme,path,fragmentId,query,**kwargs):
        self.value = value
        self.scheme="ehr"
        self.path=path
        self.fragmentId=fragmentId
        self.query=query
        Field.__init__(self,**kwargs)
    
    def schemeIsEhr():
        u""" Ensure scheme == 'ehr' """
        return self.scheme == 'ehr'

