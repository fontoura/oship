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

from zope.schema import URI,TextLine
from zope.schema.interfaces import IURI
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('oship')


class IDvUri(IURI):
    """A reference to an object which conforms to the Universal Resource Identifier
    (URI) standard, as defined by W3C RFC 2936. See "Universal Resource Identifiers in WWW"
    by Tim Berners-Lee at http://www.ietf.org/rfc/rfc2396.txt. This is a World-Wide Web RFC 
    for global identification of resources. See http://www.w3.org/Addressing for a starting 
    point on URIs. See http://www.ietf.org/rfc/rfc2806.txt for new URI types like telephone, 
    fax and modem numbers.
    
    Enables external resources to be referenced from within the content of the EHR. A number 
    of functions return the logical subparts of the URI string."""
    
    value = URI(
        title = _(u"Value"),
        description = _(u"""The URI as a string."""),
        required = True,
        )
    
    scheme=TextLine(
        title = _("Scheme"),
        description = _("""Distributed information space."""),
        required = True,
        )
    
    path=TextLine(
        title = _("Path"),
        description = _("""_"""),
        required = True,
        )
    
    fragmentId=TextLine(
        title = _("FragmentId"),
        description = _("""_"""),
        required = True,
        )
    
    query=TextLine(
        title = _("Query"),
        description = _("""_"""),
        required = True,
        )
    
    
    def scheme():
        """A distributed information "space" in which information objects exist. The scheme 
        simultaneously specifies an information space and a mechanism for accessing objects 
        in that space. For example if scheme = "ftp", it identifies the information space in 
        which all ftpable objects exist, and also the application - ftp - which can be used 
        to access them. Values may include: "ftp", "telnet", "mailto", "gopher" and many others. 
        Refer to WWW URI RFC for a full list. New information spaces can be accommodated within 
        the URI specification."""
        
    def path():
        """A string whose format is a function of the scheme. Identifies the location in 
        <scheme>-space of an information entity. Typical values include hierarchical directory 
        paths for any machine. For example, with scheme = "ftp", path might be /pub/images/image_01. 
        The strings "." and ".." are reserved for use in the path. Paths may include internet/intranet 
        location identifiers of the form: sub_domain...domain, e.g. "info.cern.ch" """

    def fragmentId():
        """A part of, a fragment or a sub-function within an object. Allows references to sub-parts 
        of objects, such as a certain line and character position in a text object. The syntax and 
        semantics are defined by the application responsible for the object. """


    def query():
        """Query string to send to application implied by scheme and path Enables queries to 
        applications, including databases to be included in the URI Any query meaningful to the 
        server, including SQL."""
        

    def valueExists():
        """value != None and value != '' """
        
 