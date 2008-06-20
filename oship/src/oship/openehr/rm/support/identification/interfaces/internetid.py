# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

u"""

From the identification package in support_im.pdf Rev. 1.6.0

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'

from zope.interface import implements
from zope.schema import TextLine,URI
from zope.i18nmessageid.message import MessageFactory 

import uid

_ = MessageFactory('oship')


class IInternetId(IUID):
    u"""
    Model of a reverse internet domain, as used to uniquely identify an internet
    domain. In the form of a dot-separated string in the reverse order of a domain
    name specified by IETF RFC1034 (http://www.ietf.org/rfc/rfc1034.txt).
    """

    value = URI(
        title=_(u"Value"),
        description=_(u"A single unicode string containing a valid URL"),
        required=True,
        )


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """

class InternetId(URI):
    u"""
    Model of a reverse internet domain, as used to uniquely identify an internet
    domain. In the form of a dot-separated string in the reverse order of a domain
    name specified by IETF RFC1034 (http://www.ietf.org/rfc/rfc1034.txt).
    """
    
    implements(IInternetId)

    def __init__(self, value,**kwargs):
        self.value = value
        for n,v in kw.items():
            setattr(self,n,v)


    def valueExists(): 
        u"""        
        value != None and then not value != ''
        """
        return self.value!=None and self.value!=''

