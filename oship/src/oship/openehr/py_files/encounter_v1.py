#This file was created with atbldr module from the OSHIP project.
#Its quality is not guaranteed and will need hand editing, especially the definition section before use.

import grok
import datetime
from zope.interface import implements
from zope.i18nmessageid import MessageFactory
from oship.openehr.archetype import *
from oship.openehr.common import *
from oship.openehr.datastructure import *
from oship.openehr.datatypes import *
from oship.openehr.demographic import *
from oship.openehr.ehr import *
from oship.openehr.extract import *
from oship.openehr.integration import *
from oship.openehr.openehrprofile import *
from oship.openehr.sm import *
from oship.openehr.support import *

_ = MessageFactory('oship')

class EncounterV1(Archetype):

    implements(IArchetype)

    def __init__(self):
        self.adlVersion =u'1.4'
        self.archetypeId = ArchetypeId(ObjectId(u'openEHR-EHR-COMPOSITION.encounter.v1'))
        self.concept = u'at0000'
        self.parentArchetypeId=ArchetypeId(ObjectId(u''))

        # Create the description components.
        self.originalLanguage=CodePhrase(u'ISO_639-1',u'en')
        self.translationDetails=None # needs to be completed in atbldr
        self.description=[u'original_author', u'name', u'Thomas Beale', u'organisation', u'Ocean Informatics', u'date', u'2005-10-10', u'details', u'en', u'language', u'_ISO_639-1::en_', u'purpose', u'Record of encounter as a progress note.', u'use', u'', u'keywords', u'progress', u'note', u'encounter', u'misuse', u'', u'copyright', u'copyright (c) 2009 openEHR Foundation', u'lifecycle_state', u'AuthorDraft', u'other_contributors'] # needs to be completed in atbldr
        self.revisionHistory=None # needs to be completed in atbldr
        self.isControlled=False # needs to be completed in atbldr

        # Create the ontology.

        # Terminologies Available Section 
        termAvail=[]
        # Term Code Section (note that there is a bug in atbldr that always cutsoff the last description of termCodes)
        termCodes={u'en':{        u'at0000':[u'text',u'Encounter',u'description',]}}

        # Constraint Code Section 
        constCodes={}
        # Term Binding Section 
        term_binding={}
        # Constraint Binding Section 
        constraint_binding={}
        self.ontology=ArchetypeOntology(termAvail,specDepth,termCodes,constraintCodes,termAN,self.parentArchetypeId)

        # Definition Section Begins Here. We build it from the leaf nodes up.

        #Length of DefinList= 12
        #u'433'
        #u'openehr::'
        #u'defining_code'
        #1
        #u'..'
        #1
        DvCodedText(definingCode,value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)
        #u'category'
        #1
        #u'..'
        #1
        nodeid=u'at0000'
        self.definition=Composition(content,context,composer,category,lang,terr,uid,nodeid,name,atdetails,fdraudit,links)
