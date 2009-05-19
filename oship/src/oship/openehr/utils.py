# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2009, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'<name> <email address>'

"""
A set of utility functions needed mostly for processing archetypes at runtime.
"""

def Languages(): # enter the language codes into this list for your application(s).
    """
    As of OSHIP 1.0a3 I have removed all languages except international English.
    I have added registration for English for the i18nmessage Factory.  
    We need a tool to auto extract any additional languages and create .po files.
    """
    
    
    return [u"en",u"fr",u"de",u"ja",u"zh-cn"]