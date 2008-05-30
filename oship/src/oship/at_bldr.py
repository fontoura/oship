# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
   Creates in memory archetype objects from ADL files and stores them in the ZODB.        
        Parsing is performed in adl_1_4.py using Pyparsing. 
        
"""

__author__  = 'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = 'plaintext'

import ZODB
from ZODB import FileStorage,DB

import transaction
from zope.schema import Text
from zope.interface import Interface,implements
from persistent import Persistent 
from zope.exceptions import DuplicationError
from zope.app.folder import folder 
from zope.app.component.site import *

import codecs
import pprint
import time
import sys
import traceback
import mglob     
from sets import Set
from pyparsing import *

from openehr.rm.datatypes.text import CodePhrase,DvText

import adl_1_4

from atdemo import ATDemo

dbDir='/home/tim/projects/oship/var/Data.fs'
# edit the path below (no trailing '/') to point to your archetypes in ADL 1.4 format
adlDir='/home/tim/projects/oship/src/oship/import_adl'
#adlDir='/home/tim/Documents/openEHR/knowledge/archetypes'
#adlDir='/home/tim/Documents/openEHR/knowledge/archetypes/dev/adl/openehr/ehr/composition'

definClassMap={'SECTION':'Section','COMPOSITION':'Composition','OBSERVATION':'Observation',\
               'ITEM_TREE':'ItemTree','ADMIN_ENTRY':'AdminEntry','ACTION':'Action',\
                'EVALUATION':'Evaluation','INSTRUCTION':'Instruction','ELEMENT':'Element',\
                'CLUSTER':'Cluster','EVENT':'Event'}

fs=FileStorage.FileStorage(dbDir)
db=DB(fs)
conn=db.open()
root=conn.root()
if 'AR' not in root['Application']:
    root['Application']['AR']=folder.Folder()
    sm = LocalSiteManager(root['Application']['AR'])
    root['Application']['AR'].setSiteManager(sm)
    transaction.commit()
    
if 'CLINICAL' not in root['Application']:
    root['Application']['CLINICAL']=folder.Folder()
    sm = LocalSiteManager(root['Application']['CLINICAL'])
    root['Application']['CLINICAL'].setSiteManager(sm)
    transaction.commit()

if 'DEMOGRAPHICS' not in root['Application']:
    root['Application']['DEMOGRAPHICS']=folder.Folder()
    sm = LocalSiteManager(root['Application']['DEMOGRAPHICS'])
    root['Application']['DEMOGRAPHICS'].setSiteManager(sm)
    transaction.commit()
    

errlog=open('ADL14parse_errors.log', 'w')

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
    print "File count: ",count

    for fname in fnames:
        n+=1               
        print "\n\nProcessing # ",n,' of ',count,' --->',fname
        adlSource = file(fname).read()
        
        try:
            # adlParsed is the returned ParseResults object
            adlParsed = adl_1_4.archetypeDefinition.parseString(adlSource)
        except ParseException: 
            e+=1
            errlog.write("Error # "+str(e)+" Occured Parsing "+fname+':\n')
            traceback.print_exc(2,file=errlog)
            errlog.write("\n\n")
            print "Parsing Failed -- Error Logged!\n"
            errCount+=1
        else:   
            bldArchetype(adlParsed)  
                
                
    print "Parsed ",count," files in",time.clock()-startTime," seconds."
    print "There were ",errCount," parse errors. See the ADL14parse_errors.log file for details."
    errlog.write("***END of Error Log***\n\n")       
    errlog.close()
    conn.close()
    db.close()

    return
        
        
def bldArchetype(adlParsed):
    """
    Build the archetype object ready for persistence in the Archetype Repository site (AR).
    """
        
    adl_version=adlParsed.archetype.adl_version
    archetype_id=adlParsed.archetype[1]
    concept=adlParsed.concept
    parent_archetype_id=adlParsed.specialize
    
    invariants=u"invariants"    
    #invariants=bldInvariants(adlParsed)
    definition=bldDefinition(adlParsed)
    ontology="ontology"
    rev="Revision History" 
    #ontology=bldOntology(adlParsed)
    #rev=bldRevisionHistory(adlParsed) 
       
    atObj=ATDemo(adl_version,archetype_id,concept,parent_archetype_id,definition,ontology,invariants,rev)            
    #atObj=Archetype(adl_version,archetype_id,concept,parent_archetype_id,definition,ontology,invariants,rev)            
    
    # now we need to persist the archetype in the ZODB
    try:
        root['Application']['AR'][atObj.archetype_id]=atObj
        transaction.commit()
    except NameError:
        errlog.write("WARNING: Error Occured Storing Archetype:\n")
        traceback.print_exc(2,file=errlog)
        errlog.write("\n\n")
    except DuplicationError:
        errlog.write("WARNING: Error Occured Storing Archetype:\n")
        traceback.print_exc(2,file=errlog)
        errlog.write("\n\n")
    
        
        

def bldDefinition(adlParsed):
    """
    Create a CComplexObject containing the definition.
    """
    definClassDict = adlParsed.definition[0].asDict()
    oeClass = definClassDict['id']
    
    if oeClass.find('[at')!=-1:
        oeClass = oeClass[:oeClass.find('[at')]
        
    if definClassMap.has_key(oeClass):
        className = definClassMap[oeClass]
    else:
        className = ''
        print "Unknown class name: ",oeClass
        
    if className == 'Section':
            defObj = bldSection(adlParsed)
            return defObj
        
    if className == 'Composition':
            defObj = bldComposition(adlParsed)
            return defObj
        
    if className == 'Observation':
            defObj = bldObservation(adlParsed)
            return defObj
        
    if className == 'ItemTree':
            defObj = bldItemTree(adlParsed)
            return defObj

    if className == 'AdminEntry':
            defObj = bldAdminEntry(adlParsed)
            return defObj

    if className == 'Action':
            defObj = bldAction(adlParsed)
            return defObj

    if className == 'Evaluation':
            defObj = bldEvaluation(adlParsed)
            return defObj
        
    if className == 'Instruction':
            defObj = bldInstruction(adlParsed)
            return defObj

    if className == 'Element':
            defObj = bldElement(adlParsed)
            return defObj

    if className == 'Cluster':
            defObj = bldCluster(adlParsed)
            return defObj

    if className == 'Event':
            defObj = bldEvent(adlParsed)
            return defObj

def bldSection(adlParsed):
        return "Section"
    
def bldObservation(adlParsed):
        return "Observation"
    
def bldItemTree(adlParsed):
        return "ItemTree"

def bldAdminEntry(adlParsed):
        return "AdminEntry"

def bldAction(adlParsed):
        return "Action"

def bldEvaluation(adlParsed):
        return "Evaluation"
    
def bldInstruction(adlParsed):
        return "Instruction"

def bldElement(adlParsed):
        return "Element"

def bldCluster(adlParsed):
        return "Cluster"

def bldEvent(adlParsed):
        return "Event"

        
def bldComposition(adlParsed):
    definClassDict=adlParsed.definition[0].asDict()
    langTermId=adlParsed.language['original_language'].split('::')[0].strip('[')
    langStr=adlParsed.language['original_language'].split('::')[1].strip(']')   
    node_id = definClassDict['id'][definClassDict['id'].find('[at'):]
    category=definClassDict['body']['attributes']['category']
    
    if 'content' in definClassDict['body']['attributes'].keys():
        content=definClassDict['body']['attributes']['content']
    else:
        content=None
        
    if 'context' in definClassDict['body']['attributes'].keys():
        context=definClassDict['body']['attributes']['context']            
    else:
        context=None     
    
    composer = "PartyProxy"
    language = CodePhrase(langTermId,langStr)
    territory = CodePhrase('ISO_3166-1','AU') #see implementation notes.
    uid = "UidBasedId()"       
    name = DvText(adlParsed.archetype[1],{},'','','','') # should be concatenated with path to instance at runtime
    archetypeDetails = adlParsed.archetype[1],'','1.0.1'
    feederAudit = "FeederAudit()"
    links = Set([])
    
    definition=[context,content,category,composer,language,territory,uid,\
                          name,archetypeDetails,feederAudit,links]
    """    
    definition=CComplexObject(context,content,category,composer,language,territory,uid,\
                          name,archetypeDetails,feederAudit,links)
    """    
    return definition
    

        
# End of Definition Section


def bldInvariants(adlParsed):
        file.write("\n\n   attr: invariants: "+repr(Set(adlParsed.invariant))+"\n")

def bldOntology(adlParsed):
        file.write("\n   ArchetypeOntology: ")
        sections = adlParsed.ontology.keys()    
        tANList = []
        termCodes = []
        constraintCodes = []
        
        if len(adlParsed.specialize) == 0 or adlParsed.specialize == '':
                specialsationDepth = 0
        else:
                specialsationDepth = 1 # this is a hack!!!!!!! need to turn this into a list
                
                
        if 'terminologies_available' in sections:
                file.write("\n      attr: terminologiesAvailable = "+repr(adlParsed.ontology['terminologies_available']))
        else:
                file.write("\n      attr: terminologiesAvailable = 0")
                
        
        if 'term_definitions' in sections:
                avail_lang = []
                for language in adlParsed.ontology['term_definitions']:
                        avail_lang.append(language[0])
                
                for l in avail_lang:
                        at_codes = adlParsed.ontology['term_definitions'][l]['items']
                        for code in at_codes:
                                for x in range(1,len(code)):
                                        tANList.append(code[x][0])
                                termCodes.append([l,code[0]])
                        file.write("\n      attr: termCodes = "+repr(termCodes))
                
        if 'constraint_definitions' in sections:
                avail_lang = []
                for language in adlParsed.ontology['constraint_definitions']:
                        avail_lang.append(language[0])       
                for l in avail_lang:
                        ac_codes = adlParsed.ontology['constraint_definitions'][l]['items']
                        
                        for code in ac_codes:
                                for x in range(1,len(code)):
                                        tANList.append(code[x][0])
                                constraintCodes.append([l,code[0]])
                        file.write("\n      attr: constraintCodes = "+repr(constraintCodes))
        
        else:
                file.write("\n      attr: constraintCodes = None Defined")

                
        termAttributeNames = Set(tANList) 
        
        file.write("\n      attr: specializationDepth = "+repr(specialsationDepth))
        file.write("\n      attr: termAttributeNames = "+repr(termAttributeNames    ))
        file.write("\n      attr: parentArchetype = (runtime object reference to parent)")    
                        

def bldRevisionHistory(adlParsed):
        file.write("\n\n Revision History: ")
        file.write("    "+repr(adlParsed.revision_history))
        

def flatten(sequence):
        """flattens a nested list structure into one list"""
        
        def hms(fpd):
                        if fpd < 60:
                                return fpd
                        elif fpd < 60**2:
                                return "%s:%s" % (int(fpd/60), fpd-int(fpd/60)*60)
                        else:
                                h = int(fpd/60**2)
                                fpd -= h*60**2
                                m = int(fpd/60)
                                fpd -= m*60
                                s = fpd
                                return "%s:%s:%s" % (h, m, s)
                        
        def rflat(seq2):
                        seq = []
                        for entry in seq2:
                                        if seqin([entry]):
                                                        seq.extend([i for i in entry])
                                        else:
                                                        seq.append(entry)
                        return seq

        def seqin(sequence):
                        for i in sequence:
                                        if ('__contains__' in dir(i) and    ## all sequences have '__contains__' in their dir()
                                                type(i) != str and type(i) != dict): ## parentheses present to aid commenting mid-condition
                                                        return True
                        return False

        import time
        btime = time.time()
        d1time = btime
        seq = [sequence][:]    ## in case parameter isn't already a sequence
        #print "Thinking",
        while seqin(seq):
                        d2time = time.time()
                        if d2time-d1time >= 5:
                                print ".",
                                d1time = d2time
                        seq = rflat(seq)
        atime = time.time()
        #print
        #print "Sequence flattened in " + str(hms(atime-btime))
        return seq

        
    
    
    
if __name__ == "__main__":
        CreateAT()     
