# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


from zope.app.folder import Folder


def ATDemo(adl_version,archetype_id,concept,parent_archetype_id,definition,ontology,invariants,rev):
    """As a demo just return a folder object with the contents being the AT info"""
    atFldr=Folder()
    atFldr.__name__=archetype_id
    atFldr.__contains__={
        'adl_version':adl_version,
        'archetype_id':archetype_id,
        'concept':concept,
        'parent_archetype_id':parent_archetype_id,
        'definition':definition,
        'ontology':ontology,
        'invariants':invariants,
        'rev':rev}
    return atFldr 
        