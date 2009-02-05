# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates Python source files from ADL files.        
        Parsing is performed in adl_1_4.py using Pyparsing. 
        You will need to easy_install pyparsing and mglob in your 'oshipenv'
        
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'


import codecs
import time
import os
import traceback   
import sys
import mglob
import logging

from pyparsing import *

import adl_1_4


# this section are required imports for (almost?) all archetypes
import grok
import datetime

#from zope.interface import implements
#from zope.schema import Set

#from oship.openehr.archetype import Archetype
#from oship.openehr.support import ArchetypeId
#from oship.openehr.support import ObjectRef
#from oship.openehr.support import ObjectId
#from oship.openehr.archetype import IArchetype
#from oship.openehr.archetype import CComplexObject
#from oship.openehr.archetype import ArchetypeOntology
#from oship.openehr.support import TerminologyId
#from oship.openehr.archetype import Cardinality
#from oship.openehr.support import Interval


os.getcwd()+'/at_build_errors.log'

logfile=os.getcwd()+'/pyfile_build.log'

#create the logfile if it doesn't exist
f=open(logfile,'w')
f.close()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=logfile,
                    filemode='w')



"""
edit the path below (no trailing '/') to point to your archetypes in ADL 1.4 format 
if you choose not use use the standard import directory.
"""

adlDir='./adl'

def CreateAT():
    """
    Create parse results to send to the builder.
    """
    
    fnames = mglob.expand("rec:"+adlDir+"=*.adl")
    n=0
    e=0
    errCount=0
    count=len(fnames)
    startTime=time.clock()
        
    fnames.sort()
    print "ADL File count: ",count

    for fname in fnames:
        n+=1               
        print "\n\nProcessing # ",n,' of ',count,' --->',fname
        adlSource = file(fname).read()
        
        try:
            # parsed_adl is the returned ParseResults object
            parsed_adl = adl_1_4.archetypeDefinition.parseString(adlSource)
        except ParseException: 
            e+=1
            logging.error("Error # "+str(e)+" Occured Parsing "+fname+':\n')
            print "Parsing Failed -- Error Logged!\n"
            errCount+=1
        else: 
            logging.info("Processing: "+fname) 
            bldArchetype(fname,parsed_adl)  
            
                
    print "\n\nParsed ",count," files in",time.clock()-startTime," seconds."
    print "There were ",errCount," parse errors. " 
    logging.info("There were "+repr(errCount)+" parse errors. ") 
    if errCount > 0:
        print "Please see: "+logfile+" file for errors & warnings."
        
        
    logging.info("*******END OF LOG FILE FOR THIS RUN*******")         
    logging.shutdown()
    return
        
        
def bldArchetype(fname,parsed_adl):
    """
    Build the archetype source file.
    """
    #get the class name from the archetypeID
    class_name=(parsed_adl.archetype[1]).partition('.')[2]
    class_name=class_name.replace('.','_')
    class_name=class_name.replace('-','_')
    
    #get the filename from the class_name
    class_file=class_name+'.py'
    
    #now lets turn the class_name into a normal Python CamelCase name
    class_list=class_name.split('_')
    class_name=''
    for n in class_list:
        class_name=class_name+n.capitalize()
            
    print '\n Creating Class : ',class_name+'\n\n'
    logging.info("The Python class name is: "+class_name+' in file: '+class_file+'\n') 
    f=open('./py_files/'+class_file,'w') # create the file for writing
    archetypeId=unicode(parsed_adl.archetype[1])
    
    f.write("#This file was created with create_pyfiles.py from the OSHIP project Release 1.0.1a2.\n")
    f.write("#Its quality is not guaranteed and will likely need hand editing before use.\n\n")
    
    
    f.write("import grok\n")  
    f.write("import datetime\n")  
    f.write("from zope.interface import implements\n")  
    f.write("from zope.schema import Set\n")  
    f.write("from oship.openehr.archetype import Archetype\n")  
    f.write("from oship.openehr.support import ArchetypeId\n")  
    f.write("from oship.openehr.support import ObjectRef\n")  
    f.write("from oship.openehr.support import ObjectId\n")  
    f.write("from oship.openehr.archetype import IArchetype\n")  
    f.write("from oship.openehr.archetype import CComplexObject\n")  
    f.write("from oship.openehr.archetype import ArchetypeOntology\n")  
    f.write("from oship.openehr.support import TerminologyId\n")  
    f.write("from oship.openehr.archetype import Cardinality\n")  
    f.write("from oship.openehr.support import Interval   \n  \n")
    
    f.write("class "+ class_name+"(Archetype,grok.Container):\n\n")
    f.write("    implements(IArchetype)\n\n" )
    f.write("    def __init__(self,parsed_adl):\n" )
    f.write("        self.adlVersion = unicode(parsed_adl.archetype.adl_version)\n")
    f.write("        self.archetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.archetype[1])))\n")
    f.write("        self.concept = unicode(parsed_adl.concept)\n")
    
    if parsed_adl.specialize:
        f.write("        self.parentArchetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.specialize)))\n")
    else:
        f.write("        self.parentArchetypeId=ArchetypeId(ObjectId(u''))\n")
        
    ## the ontology must be built first so it can be used in the definition section.
    #ontology=bldOntology(parsed_adl)
    #definition=bldDefinition(parsed_adl)
    #invariants=bldInvariants(parsed_adl)
    #rev=None #bldRevisionHistory(parsed_adl) 
    #uid=None # The OID can be assigned in the application instances
    ##terminology ID for original language
    #termID=TerminologyId(u"ISO_639-1::en",None)
    #olang=CodePhrase(termID,u'en')
    #trans=None #translations
    #descr=None #ResourceDescription(olang,'testing',[],'the use','mis-use','copyright',{},{})
    #ctrld=False #is controlled
    
    
    #atObj=Archetype(adlVersion,archetypeId,uid,concept,parentArchetypeId,definition,ontology,invariants,olang,trans,descr,rev,ctrld)            
    ## now fillin the data attribute with the object attributes so the Zope machinery works
    #atObj.__name__ = unicode(parsed_adl.archetype[1])
    
    
    ## now we need to persist the archetype in the ZODB
    #try:
        #root['Application']['AR'].__setitem__(atObj.__name__,atObj)
        #transaction.commit()
    #except NameError:
        #logging.warning("WARNING: Error Occured Storing Archetype: "+atObj.__name__)
    #except DuplicationError:
        #print "WARNING:**** Duplicate Archetype ID. This Archetype was not committed to the repository. ***"
        #logging.warning("Duplicate Archetype ID: "+atObj.__name__+" was not commited to the repository.")
        
    f.close()    


    
    
if __name__ == "__main__":
        CreateAT()     
