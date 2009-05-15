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

from archetype import ArchetypeOntology
from support import *
from datastructure import *
from datatypes import *
from demographic import *
import adl_1_4
from utils import Languages


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
    
    
    f.write("#This file was created with atbldr module from the OSHIP project.\n")
    f.write("#Its quality is not guaranteed and will need hand editing, especially the definition section before use.\n\n")
    f.write("import grok\n")  
    f.write("import datetime\n")  
    f.write("from zope.interface import implements\n")  
    f.write("from zope.i18nmessageid import MessageFactory\n")
    f.write("from oship.openehr.archetype import *\n")  
    f.write("from oship.openehr.common import *\n")  
    f.write("from oship.openehr.datastructure import *\n")  
    f.write("from oship.openehr.datatypes import *\n")  
    f.write("from oship.openehr.demographic import *\n")  
    f.write("from oship.openehr.ehr import *\n")  
    f.write("from oship.openehr.extract import *\n")  
    f.write("from oship.openehr.integration import *\n")  
    f.write("from oship.openehr.openehrprofile import *\n")  
    f.write("from oship.openehr.sm import *\n")  
    f.write("from oship.openehr.support import *\n\n")  
    f.write("_ = MessageFactory('oship')\n\n")
    
    f.write("class "+ class_name+"(Archetype):\n\n")
    f.write("    implements(IArchetype)\n\n" )
    f.write("    def __init__(self):\n" )
    f.write("        self.adlVersion =u'"+unicode(parsed_adl.archetype[0][1])+"'\n")
    f.write("        self.archetypeId = ArchetypeId(ObjectId(u'"+unicode(parsed_adl.archetype[1])+"'))\n")
    f.write("        self.concept = u'"+unicode(parsed_adl.concept.strip('[]')+"'\n"))
    
    if parsed_adl.specialize:
        f.write("        self.parentArchetypeId = ArchetypeId(ObjectId(u'"+unicode(parsed_adl.specialize)+"'))\n")
    else:
        f.write("        self.parentArchetypeId=ArchetypeId(ObjectId(u''))\n")
        
        
        
    # we need to build a description section         
    
    original_author=flatten(parsed_adl.description[0])
    details=flatten(parsed_adl.description[1])
    lifecycle_state=flatten(parsed_adl.description[2])
    other_contributors=flatten(parsed_adl.description[3])
    if len(parsed_adl.description)>=5:
        other_details=flatten(parsed_adl.description[4])
    else:
        other_details=None
        
    #print "\nOriginal Author  = ",original_author
    #print "\nDetails = ",details
    #print "\nLifecycle State = ",lifecycle_state
    #print "\nOther Contributors = ",other_contributors
    #print "\nOther Details = ", other_details

    f.write('\n        # Create the description components.\n')
    ol=details[3].split("::")
    f.write("        self.originalLanguage=CodePhrase(u'"+ol[0][1:]+"',u'"+ol[1].strip('_')+"')\n")
    f.write("        self.translationDetails=None # needs to be completed in atbldr\n")
    f.write("        self.description="+repr(flatten(parsed_adl.description))+" # needs to be completed in atbldr\n")
    f.write("        self.revisionHistory=None # needs to be completed in atbldr\n")
    f.write("        self.isControlled=False # needs to be completed in atbldr\n")
    
    # next we build the ontology

    f.write('\n        # Create the ontology.\n')
    # pre-assign all attributes
    termAvail=[]
    specDepth=0
    termCodes={}
    constCodes={}
    termAN=[]
    
    
    #cleanup the list
    ontlist=flatten(parsed_adl.ontology)  
    
    # build some reference lists
    key_list=[u'terminologies_available',u'term_definitions',u'constraint_definitions',u'term_binding',u'constraint_binding']
    lang_list=Languages() # see utils.py
    
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
    Now the sections dictionary contains a tuple of the postions of the starting word and the ending word.
    i.e.  {u'term_binding': (203, 213), u'term_definitions': (3, 107), u'constraint_definitions': (108, 202), u'terminologies_available': (0, 2), u'constraint_binding': (214, 233)}
    
    We need to process the sections in the order that they are expected to appear so that they will work correctly.
    """
    
    #print "Sections: ",sections
    f.write('\n        # Terminologies Available Section \n')
    
    # process terminologies available
    if sections.has_key(u'terminologies_available'):
        begin=sections[u'terminologies_available'][0]+1 # first location past the keyword
        end=sections[u'terminologies_available'][1]+1
        f.write("        termAvail=[")
        for v in range(begin,end):
            f.write("u'"+ontlist[v]+"',")
            termAvail.append(ontlist[v])
        f.write("]\n")
    else:
        f.write("        termAvail=[]")
    
    # process termCodes - 
    #"""
    #In OSHIP we added the word 'bind' as a key to every entry in order to maintain a 
    #balanced structure for those that have term bindings and those that do not.  
    #I find the word 'provenance as used in the specifications to be less than intuitive.  
    #"""
    f.write('\n        # Term Code Section (note that there is a bug in atbldr that always cutsoff the last description of termCodes)\n')
    if sections.has_key(u'term_definitions'):
        begin=sections[u'term_definitions'][0]+1 # first location past the keyword
        end=sections[u'term_definitions'][1]
        # now locate the begininng of each language section
        lang_point=[]
        for v in range(begin,end):
            if ontlist[v] in lang_list:
                lang_point.append(v)
        
        f.write("        termCodes={") 
        for v in range(begin,end): # the range of the termcode section in ontlist
            if v in lang_point:
                f.write(repr(ontlist[v])+':{')
            else:
                try:
                    if ontlist[v+1] in lang_list: #is the next entry a new language?
                        #print "lang code: ",ontlist[v+1]
                         
                        f.write(repr(ontlist[v])+']}},\\\n        {')
                    else:    
                        if ontlist[v] != u'items':
                            if ontlist[v][0:2]=='at':
                                f.write('        '+repr(ontlist[v])+':[_(')
                            elif ontlist[v+1][0:2]=='at':
                                f.write(repr(ontlist[v])+')],\\\n')
                             
                            else:
                                f.write(repr(ontlist[v])+'),_(')
                except IndexError:
                    break # we're at the end
                    
        f.write(")]}}\n")
    else:
        f.write("        termCodes={}")

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
        
        f.write("        constCodes={")
        for v in range(begin,end): # the range of the constraint code section in ontlist
            if v in lang_point:
                f.write(repr(ontlist[v])+':{')
            else:
                try:
                    if ontlist[v+1] in lang_list: #is the next entry a new language?
                        #print "lang code: ",ontlist[v+1]
                         
                        f.write(repr(ontlist[v])+']}},\\\n        {')
                    else:    
                        if ontlist[v] != u'items':
                            if ontlist[v][0:2]=='at':
                                f.write('        '+repr(ontlist[v])+':[')
                            elif ontlist[v+1][0:2]=='ac':
                                f.write(repr(ontlist[v])+'],\\\n')
                             
                            else:
                                f.write(repr(ontlist[v])+',')
                except IndexError:
                    break # we're at the end
                    
        f.write("]}}\n")
    else:
        f.write("        constCodes={}")

    #process term bindings 

    f.write('\n        # Term Binding Section \n')
    if sections.has_key(u'term_binding'):
        begin=sections[u'term_binding'][0]+1 # first location past the keyword
        end=sections[u'term_binding'][1]+1
        f.write("        term_binding={")
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
        f.write("        term_binding={}")
   
               
        
           
    #process constraint bindings

    f.write('\n        # Constraint Binding Section \n')
    if sections.has_key(u'constraint_binding'):
        begin=sections[u'constraint_binding'][0]+1 # first location past the keyword
        end=sections[u'constraint_binding'][1]+1
        f.write("        constraint_binding={")
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
        f.write("        constraint_binding={}")
    
     
    f.write("\n        self.ontology=ArchetypeOntology(termAvail,specDepth,termCodes,constraintCodes,termAN,self.parentArchetypeId)")
        
    # Now build the definition section
    f.write("\n\n        # Definition Section Begins Here. We build it from the leaf nodes up.\n\n")

    
    definList=flatten(parsed_adl.definition)
    definList.reverse()
    
    n=len(definList)
    f.write("        #Length of DefinList= "+repr(n)+'\n')
    m=0
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
            if m == n-1: # If at the last class name then assign it to the archetype definition.
                f.write("        self.definition="+className+'\n')
            else:    
                f.write("        "+className+'\n')
         
        m+=1 # counting which item of the list we are at.
    
    
    
    
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
            except UnicodeDecodeError:
                x=unicode(x,"eucJP")
        
        rtnlist.append(x)

    return rtnlist    
    
    
if __name__ == "__main__":
        CreateAT()     
