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

class DeviceV1(Archetype):

    implements(IArchetype)

    def __init__(self):
        self.adlVersion =u'1.4'
        self.archetypeId = ArchetypeId(ObjectId(u'openEHR-EHR-CLUSTER.device.v1'))
        self.concept = u'at0000'
        self.parentArchetypeId=ArchetypeId(ObjectId(u''))

        # Create the description components.
        self.originalLanguage=CodePhrase(u'ISO_639-1',u'en')
        self.translationDetails=None # needs to be completed in atbldr
        self.description=[u'original_author', u'name', u'Sam Heard', u'organisation', u'Ocean Informatics', u'email', u'sam.heard@oceaninformatics.com', u'date', u'19/03/2008', u'details', u'en', u'language', u'_ISO_639-1::en_', u'purpose', u'Record details of devices use in clinical care', u'use', u'Use to record the details pertaining to the device that is used to record clinical details.  This is likely to be as a nested archetype as part of a Protocol.', u'keywords', u'Device', u'Machine', u'Tool', u'misuse', u'', u'copyright', u'copyright (c) 2009 openEHR Foundation', u'lifecycle_state', u'AuthorDraft', u'other_contributors', u'other_details', u'references', u''] # needs to be completed in atbldr
        self.revisionHistory=None # needs to be completed in atbldr
        self.isControlled=False # needs to be completed in atbldr

        # Create the ontology.

        # Terminologies Available Section 
        termAvail=[]
        # Term Code Section (note that there is a bug in atbldr that always cutsoff the last description of termCodes)
        termCodes={u'en':{        u'at0000':[_(u'text'),_(u'Device details'),_(u'description'),_(u'The details of the device used')],\
        u'at0001':[_(u'text'),_(u'Name'),_(u'description'),_(u'The name of the device')],\
        u'at0002':[_(u'text'),_(u'Description'),_(u'description'),_(u'Description of the device')],\
        u'at0003':[_(u'text'),_(u'Manufacturer'),_(u'description'),_(u'The name of the manufacturer')],\
        u'at0004':[_(u'text'),_(u'Manufacturer details'),_(u'description'),_(u'Information about the manufacture of the device')],\
        u'at0005':[_(u'text'),_(u'Model'),_(u'description'),_(u'The model of the device')],\
        u'at0006':[_(u'text'),_(u'Serial number'),_(u'description'),_(u'The serial number of the device')],\
        u'at0007':[_(u'text'),_(u'Components'),_(u'description'),_(u'Information about the device components')],\
        u'at0008':[_(u'text'),_(u'Servicing'),_(u'description'),_(u'Details of servicing')],\
        u'at0009':[_(u'text'),_(u'Date last serviced'),_(u'description'),_(u'The date the device was last serviced')],\
        u'at0010':[_(u'text'),_(u'Date last calibration'),_(u'description'),_(u'Date the device was last calibrated')],\
        u'at0011':[_(u'text'),_(u'Serviced by'),_(u'description'),_(u'Agent performed the servicing')],\
        u'at0012':[_(u'text'),_(u'Components'),_(u'description'),_()]}}

        # Constraint Code Section 
        constCodes={}
        # Term Binding Section 
        term_binding={}
        # Constraint Binding Section 
        constraint_binding={}
        self.ontology=ArchetypeOntology(termAvail,specDepth,termCodes,constraintCodes,termAN,self.parentArchetypeId)

        # Definition Section Begins Here. We build it from the leaf nodes up.

        #Length of DefinList= 144
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
        nodeid=u'at0011'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'yyyy-??-??T??:??:??'
        #u'value'
        #1
        #u'..'
        #1
        DvDateTime(value)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0010'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'yyyy-??-??T??:??:??'
        #u'value'
        #1
        #u'..'
        #1
        DvDateTime(value)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0009'
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
        nodeid=u'at0008'
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
        #u'exclude'
        #u'/openEHR-EHR-CLUSTER\\.device\\.v1/'
        #u'archetype_id/value'
        #u'include'
        #u'*'
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0012'
        #u''
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
        #u'allow_archetype'
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
        nodeid=u'at0007'
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
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
        nodeid=u'at0006'
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
        nodeid=u'at0005'
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
        nodeid=u'at0003'
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
        nodeid=u'at0004'
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
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
        nodeid=u'at0002'
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
        nodeid=u'at0001'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
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
