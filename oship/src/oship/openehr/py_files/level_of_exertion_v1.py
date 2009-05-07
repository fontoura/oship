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

class LevelOfExertionV1(Archetype):

    implements(IArchetype)

    def __init__(self):
        self.adlVersion =u'1.4'
        self.archetypeId = ArchetypeId(ObjectId(u'openEHR-EHR-CLUSTER.level_of_exertion.v1'))
        self.concept = u'at0000'
        self.parentArchetypeId=ArchetypeId(ObjectId(u''))

        # Create the description components.
        self.originalLanguage=CodePhrase(u'ISO_639-1',u'en')
        self.translationDetails=None # needs to be completed in atbldr
        self.description=[u'original_author', u'name', u'Heather Leslie', u'organisation', u'Ocean Informatics', u'email', u'heather.leslie@oceaninformatics.com', u'date', u'27/10/2008', u'details', u'en', u'language', u'_ISO_639-1::en_', u'purpose', u'Record information about the amount of energy expenditure that has been, or is being, experienced by the patient', u'use', u'Record information about phase and levels of exertion - to provide state/context information within OBSERVATIONS such as Blood Pressure.', u'keywords', u'exercise', u'work', u'exertion', u'activity', u'energy', u'misuse', u'Not to be used to record actual exercise activities and measurements which should be recorded as OBSERVATIONS in their own right.', u'copyright', u'copyright (c) 2009 openEHR Foundation', u'lifecycle_state', u'AuthorDraft', u'other_contributors', u'other_details', u'references', u''] # needs to be completed in atbldr
        self.revisionHistory=None # needs to be completed in atbldr
        self.isControlled=False # needs to be completed in atbldr

        # Create the ontology.

        # Terminologies Available Section 
        termAvail=[]
        # Term Code Section (note that there is a bug in atbldr that always cutsoff the last description of termCodes)
        termCodes={u'en':{        u'at0000':[u'text',u'Level of Exertion',u'description',u'Record information about level of exertion'],\
        u'at0005':[u'text',u'Measured',u'description',u'The measured level of exertion'],\
        u'at0006':[u'text',u'At rest',u'description',u'The person is at rest, prior to undertaking exercise'],\
        u'at0007':[u'text',u'During exertion',u'description',u'The person is exerting themselves at the time'],\
        u'at0008':[u'text',u'Post-exertion',u'description',u'Measurement is taken after exertion has ceased'],\
        u'at0009':[u'text',u'Phase',u'description',u'The phase or context of exercise'],\
        u'at0010':[u'text',u'Exercise intensity',u'description',u'Amount of work being done during exercise'],\
        u'at0011':[u'text',u'Intensity',u'description',u'Semiquantitative description of the intensity of exercise undertaken'],\
        u'at0012':[u'text',u'Low Intensity',u'description',u'Up to 80% Maximal Heart Rate'],\
        u'at0013':[u'text',u'Medium Intensity ',u'description',u'80-85% of Maximal Heart Rate'],\
        u'at0014':[u'text',u'High Intensity ',u'description',u'85-90% Maximal Heart Rate'],\
        u'at0015':[u'text',u'Flat Out ',u'description',u'90-100% Maximal Heart Rate'],\
        u'at0016':[u'text',u'Description',u'description',]}}

        # Constraint Code Section 
        constCodes={}
        # Term Binding Section 
        term_binding={}
        # Constraint Binding Section 
        constraint_binding={}
        self.ontology=ArchetypeOntology(termAvail,specDepth,termCodes,constraintCodes,termAN,self.parentArchetypeId)

        # Definition Section Begins Here. We build it from the leaf nodes up.

        #Length of DefinList= 82
        #u'at0008'
        #u'at0007'
        #u'at0006'
        #u'local::'
        #u'defining_code'
        #1
        #u'..'
        #1
        DvCodedText(definingCode,value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0009'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'|'
        #1000.0
        #u'..'
        #0.0
        #u'|'
        #u'magnitude'
        #u'J/min'
        #u'units'
        #u'"1"'
        #u'list'
        #u'_openehr::130_'
        #u'property'
        CDvQuantity(list,property)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0005'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'at0015'
        #u'at0014'
        #u'at0013'
        #u'at0012'
        #u'local::'
        #u'defining_code'
        #1
        #u'..'
        #1
        DvCodedText(definingCode,value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0011'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'*'
        #1
        #u'..'
        #1
        DvText(value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0016'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'unordered'
        #u'*'
        #u'..'
        #0
        #u'cardinality'
        #u'items'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0010'
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
        #u'unordered'
        #u'*'
        #u'..'
        #0
        #u'cardinality'
        #u'items'
        #1
        #u'..'
        #1
        nodeid=u'at0000'
        self.definition=Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
