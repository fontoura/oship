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

"""
Yes, I realize that these imports are bad practice.  But in this alpha condition of the code it is expediate
"""
from archetype import ArchetypeOntology
from support import *
from datastructure import *
from datatypes import *
from demographic import *

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
if you choose not use use the standard import directory under oship/openehr/adl.
"""

adlDir='../adl'

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
    
    print parsed_adl.archetype

    
    
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
    
    
    f.write("#This file was created with adl2py module from the OSHIP project Release 1.0a2.\n")
    f.write("#Its quality is not guaranteed and will likely need hand editing before use.\n\n")
    f.write("#First write the parsed_adl out so it can be used as a Python structure.  A bit messy but it works.\n\n")
    f.write("def getAtId(parsed_adl):\n")
    f.write("    return "+repr(unicode(parsed_adl.archetype[1]))+"\n")
    f.write("def getVersion(parsed_adl):\n")
    f.write("    return " + unicode(parsed_adl.archetype[0][1])+"\n")
    f.write("\n\n")
    f.write("import grok\n")  
    f.write("import datetime\n")  
    f.write("from zope.interface import implements\n")  
    f.write("from oship.openehr.archetype import *\n")  
    f.write("from oship.openehr.support import *\n\n")  
   
    f.write("class "+ class_name+"(Archetype,grok.Container):\n\n")
    f.write("    implements(IArchetype)\n\n" )
    f.write("    def __init__(self):\n" )
    f.write("        self.archetypeId=getAtId()\n")
    f.write("        self.adlVersion = getVersion()\n")
    f.write("        self.archetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.archetype[1])))\n")
    f.write("        self.concept = unicode(parsed_adl.concept)\n")
    
    if parsed_adl.specialize:
        f.write("        self.parentArchetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.specialize)))\n")
    else:
        f.write("        self.parentArchetypeId=ArchetypeId(ObjectId(u''))\n")
        
    # next we build the ontology
    bldOntology(f,parsed_adl)    

           
     
    f.close()    


def bldOntology(f,parsed_adl):
    """Build an ontology."""
    
    # pre-assign all attributes
    termAvail=[]
    specDepth=0
    termCodes={}
    constCodes={}
    termAN=[]
    parent=u''
    ontology=ArchetypeOntology()
    
    #cleanup the list
    ontlist=flatten(parsed_adl.ontology)    
    key_list=[u'terminologies_available',u'term_definitions',u'constraint_definitions',u'term_binding',u'constraint_binding']
    lang_list=[u'en',u'de',u'nl',u'fr'] # needs to access Zope language list instead of this simple list
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
    """
    ontology.terminologiesAvailable=keywords
    
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
        
    sections=[]
    n=0
    for x in keywords:
        t=(x[1],x[0],endsection[n])
        sections.append(t)
        n+=1
     
    """
    Now sections contain tuples of the name of the present sections in the ontology, 
    the starting word and the ending word.
    i.e. [(u'terminologies_available', 0, 2), (u'term_definitions', 3, 345), (u'term_binding', 346, 405)]
    
    We need to prcess the sections in the order that they are expected to appear so that they break will work correctly (I think).
    """
    
    #print "Sections: ",sections
    
    # process terminologies available
    itemlist=[]
    for y in sections:    
        if y[0]==u'terminologies_available':      
            ontlist=ontmap.items() 
            #print ontlist
            try:
                for x in ontlist:
                    n=x[0]
                    if n > y[2]: 
                        break # if we have reached the end of the section then leave.
                    else:
                        itemlist.append(x[1])
            except IndexError:
                pass

    termAvail=itemlist
    
    # process termCodes - 
    """
    In OSHIP we added the word 'bind' as a key to every entry in order to maintain a 
    balanced structure for those that have term bindings and those that do not.  
    I find the word 'provenance as used in the specifications to be less than intuitive.  
    """
    itemlist=[]
    langCode=''
    for y in sections:    
        if y[0]==u'term_definitions':
            ontlist=ontmap.items() 
            try:
                for x in ontlist:
                    if x[1] in lang_list: # If it's a langugage change it.
                        langCode=x[1], 
                    if x[1].startswith(u'at0'): # check to see if this is an at code. 
                        n=x[0] # the index  number of this tuple
                        if n > y[2]: 
                            break # if we have reached the end of the section then leave.
                        else:
                            codeentry={ontlist[n+1][1]:ontlist[n+2][1],ontlist[n+3][1]:ontlist[n+4][1],u"bind":None}
                            #print "Code Entry = ",codeentry
                            #itemlist.append(codeentry)
                            f.write('\n        termCode=ArchetypeTerm([')
                            f.write(langCode[0])
                            f.write(',')
                            f.write(x[1])
                            f.write(',')
                            f.write(repr(codeentry))
                            f.write('])')
                            f.write("\n        ontology['termCodes'][x[1]]=")
                            f.write(repr(codeentry))
                            f.write("\n")

            except IndexError:
                pass
            
    f.write('\n\n')
            
    """
    The completed list looks like this:
     [u'en', u'at0000', {u'text': u'Body weight', u'description': u'Total body weight - a surrogate for naked body weight', u'bind': None}]
     We can get the language attribute, the at code is then used in ontology['termCodes'][atcode]=the dictionary to create the items attribute.
    """
    termCodes=itemlist  
    
    #process constraint codes
    itemlist=[]
    for y in sections:    
        if y[0]==u'constraint_definitions':      
            ontlist=ontmap.items() 
            try:
                for x in range(y[1],y[2]):
                    if ontlist[x][1] in lang_list: # If it's a langugage change just enter it.
                        itemlist.append(ontlist[x][1]) 
                    if ontlist[x][1].startswith(u'ac0'): # check to see if this is an ac code. 
                        n=ontlist[x][0] # the index  number of this tuple
                        itemlist.append({ontlist[x][1]:{ontlist[x+1][1]:ontlist[x+2][1],ontlist[x+3][1]:ontlist[x+4][1],u"bind":None}})
            except IndexError:
                pass
            
    constCodes=itemlist
   
    #process term bindings 
    itemlist=[]
    binddict={}
    for y in sections:    
        if y[0]==u'term_binding':      
            ontlist=ontmap.items() 
            tmplist=ontlist[y[1]:y[2]]
            try:
                z=3 # key of first at code
                for x in tmplist:
                    
                    binddict[tmplist[z][1]]=tmplist[z+1][1]
                    z+=2                             
            except IndexError:
                pass
            
        for y in termCodes:
            if isinstance(y,dict):
                z=y.keys() # always only one
                if binddict.has_key(z[0]):
                    codestr=binddict[z[0]].replace('_','')
                    codelist=codestr.split('::')
                    cp=CodePhrase(codelist[0],codelist[1])
                    y[z[0]][u'bind']=cp
                                
               
        
            
    #process constraint bindings
    itemlist=[]
    binddict={}
    for y in sections:    
        if y[0]==u'constraint_binding':      
            ontlist=ontmap.items() 
            try:
                for x in range(y[1],y[2]):
                    if ontlist[x][1].startswith(u'ac0'): # check to see if this is an ac code.
                        
                        for y in constCodes:
                            if isinstance(y,dict):
                                #print y
                                if y.has_key(ontlist[x][1]):
                                    #constCodes[y][u'bind']=ontlist[x+1]
                                    print "Constraint code: ",ontlist[x][1]
            except IndexError:
                pass
    
    #ontology=ArchetypeOntology(termAvail,specDepth,termCodes,constCodes,termAN,parent)    
    return ontology
 
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
            # replace any brackets with underscores so Python doesn't thnk it's a list and we still havea seperator.
            x=x.replace('[','_')
            x=x.replace(']','_')
            try:
                x=unicode(x, "utf-8")  # need more decode types here
            except UnicodeDecodeError:
                x=unicode(x, "latin1")
        
        rtnlist.append(x)

    return rtnlist    
    
    
if __name__ == "__main__":
        CreateAT()     
