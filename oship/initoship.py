# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""
Initialize the archetype repository
"""

import os
import sys

if sys.platform == 'win32':
    #print 'You are on a Windows platform'
    cwd=os.getcwd()
    osctl=open(cwd+'\\bin\\oship-ctl-script.py','r')
    syspaths=osctl.read()
    osctl.close()
    fh=open(cwd+'\\src\\oship\\load_ar.py','w')
    syspaths=syspaths.split('import oship.startup')[0]
    syspaths=syspaths.split('import sys')[1]

    # "\n\nfrom oship.at_bldr import CreateAT\nif __name__ == '__main__':\n   oship.at_bldr.CreateAT()\n"
    syspaths='import sys \n\n'+syspaths+"\nfrom at_bldr import CreateAT\nCreateAT()\n"
    fh.write(syspaths)
    fh.close()

    print "\n"
    print "1) Put your ADL files into the " + cwd + "\src\oship\import_adl directory."
    print "2) Execute '" + cwd + "\src\oship\load_ar.py'\n"
    print "You can re-run '" + cwd + "\src\oship\load_ar.py' anytime you want to add archetypes to the AR\n\n"


else:
    #print 'You are NOT on a Windows platform'
    cwd=os.getcwd()
    osctl=open(cwd+'/bin/oship-ctl','r')
    syspaths=osctl.read()
    osctl.close()
    fh=open(cwd+'/src/oship/load_ar.py','w')
    syspaths=syspaths.split('import oship.startup')[0]
    syspaths=syspaths.split('import sys')[1]

    # "\n\nfrom oship.at_bldr import CreateAT\nif __name__ == '__main__':\n   oship.at_bldr.CreateAT()\n"
    syspaths='import sys \n\n'+syspaths+"\nfrom at_bldr import CreateAT\nCreateAT()\n"
    fh.write(syspaths)
    fh.close()

    print "\n\nNow you should put your ADL files into the oship/src/import_adl directory."
    print "When ready.  Execute '$python load_ar.py' from the oship/src/oship directory."
    print "You can re-run '$python load_ar.py' anytime you want to add archetypes to the AR\n\n"




