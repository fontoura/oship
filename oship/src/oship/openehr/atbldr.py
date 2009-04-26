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



# this section are required imports for (almost?) all archetypes
import grok
import datetime
from classmap import getClassName

"""
Yes, I realize that these imports are bad practice.  But in this alpha condition of the code it is expediante
"""
from archetype import ArchetypeOntology
from support import *
from datastructure import *
from datatypes import *
from demographic import *
import adl_1_4

logfile=os.getcwd()+'/src/oship/openehr/py_files/pyfile_build.log'

#create the logfile if it doesn't exist
f=open(logfile,'w')
f.close()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=logfile,
                    filemode='w')



"""
edit the path below (no trailing '/') to point to your archetypes in ADL 1.4 format 
if you choose not use use the standard import directory under oship/openehr/adl.
"""

adlDir=os.getcwd()+'/src/oship/openehr/adl'
py_filesDir=os.getcwd()+'/src/oship/openehr/py_files/'


def CreatePy():
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
    print "ADL File count: ",count," in ",adlDir
    print "\n Placing Python source files in ", py_filesDir

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
    f=open(py_filesDir+class_file,'w') # create the file for writing
    
    
    f.write("#This file was created with adl2py module from the OSHIP project.\n")
    f.write("#Its quality is not guaranteed and will likely need hand editing before use.\n\n")
    f.write("import grok\n")  
    f.write("import datetime\n")  
    f.write("from zope.interface import implements\n")  
    f.write("from oship.openehr.archetype import *\n")  
    f.write("from oship.openehr.support import *\n\n")  
   
    f.write("class "+ class_name+"(Archetype,grok.Container):\n\n")
    f.write("    implements(IArchetype)\n\n" )
    f.write("    def __init__(self):\n" )
    f.write("        self.adlVersion =u'"+unicode(parsed_adl.archetype[0][1])+"'\n")
    f.write("        self.archetypeId = ArchetypeId(ObjectId(u'"+unicode(parsed_adl.archetype[1])+"'))\n")
    f.write("        self.concept = u'"+unicode(parsed_adl.concept.strip('[]')+"'\n"))
    
    if parsed_adl.specialize:
        f.write("        self.parentArchetypeId = ArchetypeId(ObjectId(u'"+unicode(parsed_adl.specialize)+"'))\n")
    else:
        f.write("        self.parentArchetypeId=ArchetypeId(ObjectId(u''))\n")
        
    # next we build the ontology

    f.write('\n        # Create the ontology.\n')
    # pre-assign all attributes
    termAvail=[]
    specDepth=0
    termCodes={}
    constCodes={}
    termAN=[]
    parent=u''
    
    #cleanup the list
    ontlist=flatten(parsed_adl.ontology)  
    
    # build some reference lists
    key_list=[u'terminologies_available',u'term_definitions',u'constraint_definitions',u'term_binding',u'constraint_binding']
    lang_list=[u'en',u'de',u'nl',u'fr'] # needs to access Zope language list/terminology look in zope.i18n.locaales.provider
    
    itemlist=[]
    # now go through ontlist and map all the words.  
    
    ontmap={}
    for index, item in enumerate(ontlist):
        ontmap[index]=item  
    
        
    a = ontmap.items()
    keywords=[]
    for x in a:
        for v in key_list:
            if v in x:
                keywords.append(x)
            
    """
    keywords now contains tuples of all the possible section names and their index:
    i.e. [(0, u'terminologies_available'), (3, u'term_definitions'), (346, u'term_binding')]
    This is so we know where each one starts. Below, we also want to know where each one ends.
    """
    
    
    numkeys=len(keywords)
    ends=[]
    endsection=[]
    for x in keywords:
        ends.append([x][0][0])
    
    ends=ends[1:]
    for x in ends:
        y=x-1
        endsection.append(y)
        
    endsection.append(len(a)) # final word in the ontology.
        
    sections={}
    n=0
    for x in keywords:
        t=(x[0],endsection[n])
        sections[x[1]]=t
        n+=1
     
    """
    Now the sections dictionary contains a tuples of the the starting word and the ending word.
    i.e.  {u'term_binding': (203, 213), u'term_definitions': (3, 107), u'constraint_definitions': (108, 202), u'terminologies_available': (0, 2), u'constraint_binding': (214, 233)}
    
    We need to process the sections in the order that they are expected to appear so that they will work correctly.
    """
    
    #print "Sections: ",sections
    f.write('\n        # Terminologies Available Section \n')
    
    # process terminologies available
    if sections.has_key(u'terminologies_available'):
        begin=sections[u'terminologies_available'][0]+1 # first location past the keyword
        end=sections[u'terminologies_available'][1]+1
        f.write("        self.ontology[u'terminologies_avalable']=[")
        for v in range(begin,end):
            f.write("u'"+ontlist[v]+"',")
            termAvail.append(ontlist[v])
        f.write("]\n")
    else:
        f.write("        # None Found\n")
    
    # process termCodes - 
    #"""
    #In OSHIP we added the word 'bind' as a key to every entry in order to maintain a 
    #balanced structure for those that have term bindings and those that do not.  
    #I find the word 'provenance as used in the specifications to be less than intuitive.  
    #"""
    f.write('\n        # Term Code Section \n')
    if sections.has_key(u'term_definitions'):
        begin=sections[u'term_definitions'][0]+1 # first location past the keyword
        end=sections[u'term_definitions'][1]
        # now locate the begininng of each language section
        lang_point=[]
        for v in range(begin,end):
            if ontlist[v] in lang_list:
                lang_point.append(v)
        
        f.write("        self.ontology[u'term_definitions']={")
        for v in range(begin,end):
            if v in lang_point:
                f.write(repr(ontlist[v])+':[')
            else:
                try:
                    if ontlist[v+1] in lang_list:
                        #print "lang code: ",ontlist[v+1]
                         
                        f.write(repr(ontlist[v])+']},{')
                    else:    
                        f.write(repr(ontlist[v])+',')
                except IndexError:
                    break # we're at the end
                    
        f.write("]}\n")
    else:
        f.write("        # None Found\n")

    #process constraint codes
    f.write('\n        # Constraint Code Section \n')
    if sections.has_key(u'constraint_definitions'):
        begin=sections[u'constraint_definitions'][0]+1 # first location past the keyword
        end=sections[u'constraint_definitions'][1]
        # now locate the begininng of each language section
        lang_point=[]
        for v in range(begin,end):
            if ontlist[v] in lang_list:
                lang_point.append(v)
        
        f.write("        self.ontology[u'constraint_definitions']={")
        for v in range(begin,end):
            if v in lang_point:
                f.write(repr(ontlist[v])+':[')
            else:
                try:
                    if ontlist[v+1] in lang_list:
                        #print "lang code: ",ontlist[v+1]
                         
                        f.write(repr(ontlist[v])+']},{')
                    else:    
                        f.write(repr(ontlist[v])+',')
                except IndexError:
                    break # we're at the end
                    
        f.write("]}\n")
    else:
        f.write("        # None Found\n")

    #process term bindings 

    f.write('\n        # Term Binding Section \n')
    if sections.has_key(u'term_binding'):
        begin=sections[u'term_binding'][0]+1 # first location past the keyword
        end=sections[u'term_binding'][1]+1
        f.write("        self.ontology[u'term_binding']={")
        try:
            for v in range(begin,end,2):
                if ontlist[v] in termAvail:
                    f.write("u'"+ontlist[v]+"':[")  
                else:    
                    if ontlist[v] != u'items':
                        f.write("{u'"+ontlist[v]+"':u'"+ontlist[v+1]+"'},")
        except IndexError:
            pass # we're at the end

        f.write("]}\n")
    else:
        f.write("        # None Found\n")
   
               
        
           
    #process constraint bindings

    f.write('\n        # Constraint Binding Section \n')
    if sections.has_key(u'constraint_binding'):
        begin=sections[u'constraint_binding'][0]+1 # first location past the keyword
        end=sections[u'constraint_binding'][1]+1
        f.write("        self.ontology[u'constraint_binding']={")
        try:
            for v in range(begin,end,2):
                if ontlist[v] in termAvail:
                    f.write("u'"+ontlist[v]+"':[")  
                else:    
                    if ontlist[v] != u'items':
                        f.write("{u'"+ontlist[v]+"':u'"+ontlist[v+1]+"'},")
        except IndexError:
            pass # we're at the end

        f.write("]}\n")
    else:
        f.write("        # None Found\n\n")
    
        
        
    # Now build the definition section
    f.write("\n\n        # Definition Section Begins Here. We build it from the leaf nodes up.\n\n")

    
    definList=flatten(parsed_adl.definition)
    definList.reverse()
    
    n=len(definList)
    for x in definList:
        nodeid=""
        #strip off the nodeid if there is one
        if isinstance(x,basestring) and x.find('_at')!=-1:
            nodeid=x[x.find('_at'):]
            f.write("        nodeid=u'"+nodeid.strip('_')+"'\n")
            x = x[:x.find('_at')]
            
        className=getClassName(x)
        if className == None:
            f.write("        #"+repr(x)+'\n')
        else:
            
            f.write("        "+className+'\n')
         
    
    f.write("        self.definition=\n")
    
    
    
    #Finished building the Archetype class        
    f.close()
    return

 
def flatten(x):
    """flatten(sequence) -> list

    Returns a single, flat list which contains all elements retrieved
    from the sequence and all recursively contained sub-sequences
    (iterables). All strings are converted to unicode.
    
    """
    result = []
    for el in x:
        #if isinstance(el, (list, tuple)):
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
            
            
    # all strings must be unicode
    rtnlist=[]
    for x in result:
        if isinstance(x,str):
            # replace any brackets so Python doesn't think it's a list and we still havea seperator.
            x=x.replace('[','_')
            x=x.replace(']','_')
            try:
                x=unicode(x, "utf8")  # need more decode types here
            except UnicodeDecodeError:
                x=unicode(x, "latin1")
            except UnicodeDecodeError:
                x=unicode(x,"iso-8859-1")
        
        rtnlist.append(x)

    return rtnlist    
    
    
if __name__ == "__main__":
        CreateAT()     
