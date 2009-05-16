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

class BloodPressureV1(Archetype):

    implements(IArchetype)

    def __init__(self):
        self.adlVersion =u'1.4'
        self.archetypeId = ArchetypeId(ObjectId(u'openEHR-EHR-OBSERVATION.blood_pressure.v1'))
        self.concept = u'at0000'
        self.parentArchetypeId=ArchetypeId(ObjectId(u''))

        # Create the description components.
        self.originalLanguage=CodePhrase(u'ISO_639-1',u'en')
        self.translationDetails=None # needs to be completed in atbldr
        self.description=[u'original_author', u'name', u'Sam Heard', u'organisation', u'Ocean Informatics', u'email', u'sam.heard@oceaninformatics.com', u'date', u'22/03/2006', u'details', u'en', u'language', u'_ISO_639-1::en_', u'purpose', u'To record the systemic arterial blood pressure of a person. ', u'use', u'All systemic arterial blood pressure measurements are recorded using this archetype. There is a rich state model, which can be used to support exercise/stress testing and research using tilt tables.', u'keywords', u'observations', u'measurement', u'bp', u'vital signs', u'mean arterial pressure', u'pulse pressure', u'systolic', u'diastolic', u'RR', u'NIBP', u'misuse', u'Not to be used for intravenous pressure.\r\nNot to be used for the recording of the measurement of arterial pressure specific locations such as the radial artery or brachial artery.\r\nUse OBSERVATION.intravascular_pressure and related specialisations in these situations.', u'copyright', u'copyright (c) 2009 openEHR Foundation', u'ja', u'language', u'_ISO_639-1::ja_', u'purpose', u'*To record the systemic blood pressure of a person. The measurement records the systolic and the diastolic pressure by some means suitable for the result to be seen as a surrogate for the general and systemic blood pressure.(en)', u'use', u'*All blood pressure measurements are recorded using this archetype. There is a rich state model for use with exercise ECGs and Tilt Table measurements.(en)', u'keywords', u'*observations(en)', u'*blood pressure(en)', u'*measurement(en)', u'misuse', u'*Not to be used for intravascular pressure.(en)', u'copyright', u'copyright (c) 2009 openEHR Foundation', u'de', u'language', u'_ISO_639-1::de_', u'purpose', u'Dient der Dokumentation des systemischen Blutdrucks einer Person. Die Messung zeichnet den systolischen und diastolischen Blutdruck auf geeignete Art und Weise auf, sodass das Resultat der Messung als charakteristisch f\xfcr den tats\xe4chlichen systemischen Blutdruck angesehen werden kann.', u'use', u'Alle Blutdruckmessungen werden unter Zuhilfenahme dieses Archetypen dokumentiert. Der Archetyp beinhaltet ein umfassendes Status-Modell z.B. bei Durchf\xfchrung von Belastungs-EKGs und Kipptischuntersuchungen.', u'misuse', u'Nicht zu Benutzen zur Dokumentation des intravaskul\xe4ren Drucks.', u'copyright', u'copyright (c) 2009 openEHR Foundation', u'zh-cn', u'language', u'_ISO_639-1::zh-cn_', u'purpose', u'*To record the systemic blood pressure of a person. The measurement records the systolic and the diastolic pressure by some means suitable for the result to be seen as a surrogate for the general and systemic blood pressure.(en)', u'use', u'*All blood pressure measurements are recorded using this archetype. There is a rich state model for use with exercise ECGs and Tilt Table measurements.(en)', u'keywords', u'*observations(en)', u'*blood pressure(en)', u'*measurement(en)', u'misuse', u'*Not to be used for intravascular pressure.(en)', u'copyright', u'copyright (c) 2009 openEHR Foundation', u'lifecycle_state', u'AuthorDraft', u'other_contributors', u'Heather Leslie, Ocean Informatics', u'Sundaresan Jagannathan, NHS Scotland', u'Sebastian Garde, Ocean Informatics', u'Jeroen Meintjens, Medisch Centrum Alkmaar, Netherlands', u'Pieter Hummel, Medisch Centrum Alkmaar, Netherlands', u'Melvin Reynolds, UK', u'Evelyn Hovenga, Australia', u'Ian McNicoll, Ocean Informatics, Scotland', u'Derek Hoy, Scotland', u'Anneke Goossen, Netherlands', u'Tony Shannon, NHS, UK', u'Rong Chen, Sweden', u'Beatriz De Faria Leao, Brazil', u'Knut Bernstein, Denmark', u'Eugene Igras, IRIS Systems, Canada', u'other_details', u'references', u'Cuff sizes:  Circulation (1993;88:2460-2467), by Dorothee Perloff,MD; Carlene Grim, MSN, SpDN; John Flack, MD; Edward D. Frohlich, MD; Martha Hill, PhD, RN; Mary McDonald, MSPH, RN; and Bruce Z. Morgenstern, MD, Writing Group'] # needs to be completed in atbldr
        self.revisionHistory=None # needs to be completed in atbldr
        self.isControlled=False # needs to be completed in atbldr

        # Create the ontology.

        # Terminologies Available Section 
        termAvail=[u'SNOMED-CT',u'...',]

        # Term Code Section (note that there is a bug in atbldr that always cutsoff the last description of termCodes)
        termCodes={u'en':{        u'at0000':[_(u'text'),_(u'Blood pressure'),_(u'description'),_(u'The measurement of arterial blood pressure which is a surrogate for arterial pressure in the systemic circulation.')],\
        u'at0001':[_(u'text'),_(u'history'),_(u'description'),_(u'history Structural node')],\
        u'at0003':[_(u'text'),_(u'blood pressure'),_(u'description'),_(u'@ internal @')],\
        u'at0004':[_(u'text'),_(u'Systolic'),_(u'description'),_(u'Peak systemic arterial blood pressure over one cycle - measured in systolic or contraction phase of the heart cycle')],\
        u'at0005':[_(u'text'),_(u'Diastolic'),_(u'description'),_(u'Minimum systemic arterial blood pressure over one cycle - measured in the diastolic or relaxation phase')],\
        u'at0006':[_(u'text'),_(u'any event'),_(u'description'),_(u'Other event in event history')],\
        u'at0007':[_(u'text'),_(u'state structure'),_(u'description'),_(u'@ internal @')],\
        u'at0008':[_(u'text'),_(u'Position'),_(u'description'),_(u'The position of the person at the time of measurement')],\
        u'at0011':[_(u'text'),_(u'list structure'),_(u'description'),_(u'list structure')],\
        u'at0013':[_(u'text'),_(u'Cuff size'),_(u'description'),_(u'The size of the cuff used for blood pressure measurement')],\
        u'at0014':[_(u'text'),_(u'Location of measurement'),_(u'description'),_(u'The site of the measurement of the blood pressure')],\
        u'at0015':[_(u'text'),_(u'Adult'),_(u'description'),_(u'A cuff that is standard for an adult - bladder approx 13cm x 30cm')],\
        u'at0016':[_(u'text'),_(u'Large Adult'),_(u'description'),_(u'A cuff for adults with larger arms - bladder approx 16cm x 38cm')],\
        u'at0017':[_(u'text'),_(u'Paediatric/Child'),_(u'description'),_(u'A cuff that is appropriate for a child or thin arm - bladder approx 8cm x 21cm')],\
        u'at0025':[_(u'text'),_(u'Right arm'),_(u'description'),_(u'The right arm of the person')],\
        u'at0026':[_(u'text'),_(u'Left arm'),_(u'description'),_(u'The left arm of the person')],\
        u'at0027':[_(u'text'),_(u'Right thigh'),_(u'description'),_(u'The right thigh of the person')],\
        u'at0028':[_(u'text'),_(u'Left thigh'),_(u'description'),_(u'The left thigh of the person')],\
        u'at0031':[_(u'text'),_(u'Postural change'),_(u'description'),_(u'The difference between standing and sitting/lying blood pressure')],\
        u'at0033':[_(u'text'),_(u'Comment'),_(u'description'),_(u'Comment on blood pressure measurement')],\
        u'at1000':[_(u'text'),_(u'Standing'),_(u'description'),_(u'Standing at the time of blood pressure measurement')],\
        u'at1001':[_(u'text'),_(u'Sitting'),_(u'description'),_(u'Sitting (for example on bed or chair) at the time of blood pressure measurement')],\
        u'at1002':[_(u'text'),_(u'Reclining'),_(u'description'),_(u'Reclining at the time of blood pressure measurement')],\
        u'at1003':[_(u'text'),_(u'Lying'),_(u'description'),_(u'Lying flat at the time of blood pressure measurement')],\
        u'at1004':[_(u'text'),_(u'Paradox'),_(u'description'),_(u'Variation in blood pressure with respiration')],\
        u'at1005':[_(u'text'),_(u'Tilt'),_(u'description'),_(u'The craniocaudal tilt of the surface on which the person is lying at the time of measurement')],\
        u'at1006':[_(u'text'),_(u'Mean Arterial Pressure'),_(u'description'),_(u'The average arterial pressure that occurs over the entire course of the heart contraction and relaxation cycle.   ')],\
        u'at1007':[_(u'text'),_(u'Pulse Pressure'),_(u'description'),_(u'The difference between the systolic and diastolic pressure over one contraction cycle.')],\
        u'at1008':[_(u'text'),_(u'Adult Thigh'),_(u'description'),_(u'A cuff used for an adult thigh - bladder approx 20cm x 42cm')],\
        u'at1009':[_(u'text'),_(u'Neonatal'),_(u'description'),_(u'A cuff used for a new born - bladder approx 3cm x 6cm')],\
        u'at1010':[_(u'text'),_(u'Korotkoff sounds'),_(u'description'),_(u'Record which Korotkoff sound is used for determining diastolic pressure')],\
        u'at1011':[_(u'text'),_(u'Fourth sound'),_(u'description'),_(u'The fourth Korotkoff sound is identified as an abrupt muffling of sounds')],\
        u'at1012':[_(u'text'),_(u'Fifth sound'),_(u'description'),_(u'The fifth Korotkoff sound is identified by absence of sounds as the cuff pressure drops below the diastolic blood pressure')],\
        u'at1013':[_(u'text'),_(u'Trendelenburg'),_(u'description'),_(u'Lying flat on the back (supine position) with the feet higher than the head at the time of blood pressure measurement')],\
        u'at1014':[_(u'text'),_(u'Left Lateral'),_(u'description'),_(u'Lying on the left side at the time of blood pressure measurement')],\
        u'at1018':[_(u'text'),_(u'Infant'),_(u'description'),_(u'A cuff used for infants - bladder approx 5cm x 15cm')],\
        u'at1019':[_(u'text'),_(u'Small Adult'),_(u'description'),_(u'A cuff used for a small adult - bladder approx 10cm x 24cm')],\
        u'at1020':[_(u'text'),_(u'Right wrist'),_(u'description'),_(u'The right wrist of the person')],\
        u'at1021':[_(u'text'),_(u'Left wrist'),_(u'description'),_(u'The left wrist of the person')],\
        u'at1025':[_(u'text'),_(u'Device'),_(u'description'),_(u'Details about sphygmomanometer or other device used to measure the blood pressure')],\
        u'at1026':[_(u'text'),_(u'Finger'),_(u'description'),_(u'A finger of the person')],\
        u'at1030':[_(u'text'),_(u'Exertion  '),_(u'description'),_(u'Details about physical activity undertaken at the time of blood pressure measurement')],\
        u'at1031':[_(u'text'),_(u'Right ankle'),_(u'description'),_(u'The right ankle of the person')],\
        u'at1032':[_(u'text'),_(u'Left ankle'),_(u'description'),_(u'The left ankle of the person')],\
        u'at1033':[_(u'text'),_(u'Location'),_(u'description'),_(u'Body site of blood pressure location')],\
        u'at1034':[_(u'text'),_(u'Description of location'),_(u'description'),_(u'Detailed description about the site of the measurement of the blood pressure')],\
        u'at1035':[_(u'text'),_(u'Method'),_(u'description'),_(u'Method of measurement of blood pressure')],\
        u'at1036':[_(u'text'),_(u'Auscultation'),_(u'description'),_(u'Method of measuring blood pressure externally, using a stethoscope and Korotkoff sounds')],\
        u'at1037':[_(u'text'),_(u'Palpation'),_(u'description'),_(u'Method of measuring blood pressure externally, using palpation (usually of the radial artery at the wrist)')],\
        u'at1038':[_(u'text'),_(u'Mean Arterial Pressure Formula'),_(u'description'),_(u'Formula used to calculate the MAP (if recorded in data)')],\
        u'at1039':[_(u'text'),_(u'Machine'),_(u'description'),_(u'Method of measuring blood pressure externally, using a blood pressure machine')],\
        u'at1040':[_(u'text'),_(u'Invasive'),_(u'description'),_(u'Method of measuring blood pressure internally ie involving penetration of the skin and measuring inside blood vessels')],\
        u'at1041':[_(u'text'),_(u'Anxiety '),_(u'description'),_(u"Details about the subject's level of anxiety at the time of blood pressure measurement")]}}

        # Constraint Code Section 
        constCodes={}
        # Term Binding Section 
        term_binding={u'SNOMED-CT':[{u'at0000':u'_SNOMED-CT(2003)::163020007_'},{u'at0004':u'_SNOMED-CT(2003)::163030003_'},{u'at0005':u'_SNOMED-CT(2003)::163031004_'},{u'at0013':u'_SNOMED-CT(2003)::246153002_'},]}

        # Constraint Binding Section 
        constraint_binding={}
        self.ontology=ArchetypeOntology(termAvail,specDepth,termCodes,constraintCodes,termAN,self.parentArchetypeId)

        # Definition Section Begins Here. We build it from the leaf nodes up.

        #Length of DefinList= 399
        #u'at1012'
        #u'at1011'
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
        nodeid=u'at1010'
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
        nodeid=u'at1038'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'exclude'
        #u'/openEHR-EHR-CLUSTER\\.device\\.v1/'
        #u'archetype_id/value'
        #u'include'
        #u'*'
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at1025'
        #u''
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
        #u'allow_archetype'
        #u'at1040'
        #u'at1039'
        #u'at1037'
        #u'at1036'
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
        nodeid=u'at1035'
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
        nodeid=u'at1034'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'at1032'
        #u'at1031'
        #u'at1026'
        #u'at1021'
        #u'at1020'
        #u'at0028'
        #u'at0027'
        #u'at0026'
        #u'at0025'
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
        nodeid=u'at0014'
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
        nodeid=u'at1033'
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
        #u'at1019'
        #u'at1018'
        #u'at1009'
        #u'at1008'
        #u'at0017'
        #u'at0016'
        #u'at0015'
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
        nodeid=u'at0013'
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
        nodeid=u'at0011'
        ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)
        #u'protocol'
        nodeid=u'at0001_/events_at0006_/state_at0007'
        #u'/data'
        #1
        #u'..'
        #1
        ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)
        #u'use_node'
        #u'state'
        nodeid=u'at0001_/events_at0006_/data_at0003'
        #u'/data'
        #1
        #u'..'
        #1
        ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)
        #u'use_node'
        #u'data'
        #u'149'
        #u'openehr::'
        #u'defining_code'
        #1
        #u'..'
        #1
        DvCodedText(definingCode,value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)
        #u'math_function'
        #u'*'
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at1004'
        IntervalEvent(width,mfunc,scount)
        nodeid=u'at0001_/events_at0006_/state_at0007'
        #u'/data'
        #1
        #u'..'
        #1
        ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)
        #u'use_node'
        #u'state'
        nodeid=u'at0001_/events_at0006_/data_at0003'
        #u'/data'
        #1
        #u'..'
        #1
        ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)
        #u'use_node'
        #u'data'
        #u'147'
        #u'openehr::'
        #u'defining_code'
        #1
        #u'..'
        #1
        DvCodedText(definingCode,value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)
        #u'math_function'
        #u'*'
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0031'
        IntervalEvent(width,mfunc,scount)
        #0
        #u'precision'
        #u'\xb0'
        #u'units'
        #0.0
        #u'magnitude'
        #u'assumed_value'
        #u'|'
        #0
        #u'|'
        #u'precision'
        #u'|'
        #90.0
        #u'..'
        #-90.0
        #u'|'
        #u'magnitude'
        #u'\xb0'
        #u'units'
        #u'"1"'
        #u'list'
        #u'_openehr::497_'
        #u'property'
        CDvQuantity(list,property)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at1005'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'exclude'
        #u'/.*/'
        #u'archetype_id/value'
        #u'include'
        #u'*'
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at1041'
        #u''
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
        #u'allow_archetype'
        #u'exclude'
        #u'/openEHR-EHR-CLUSTER\\.level_of_exertion\\.v1/'
        #u'archetype_id/value'
        #u'include'
        #u'*'
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at1030'
        #u''
        Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)
        #u'allow_archetype'
        #u'at1001'
        #u'at1014'
        #u'at1013'
        #u'at1003'
        #u'at1002'
        #u'at1001'
        #u'at1000'
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
        nodeid=u'at0008'
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
        nodeid=u'at0007'
        ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)
        #u'state'
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
        nodeid=u'at0033'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'|'
        #0
        #u'|'
        #u'precision'
        #u'|'
        #1000.0
        #u'<'
        #u'..'
        #0.0
        #u'|'
        #u'magnitude'
        #u'mm_Hg_'
        #u'units'
        #u'"1"'
        #u'list'
        #u'_openehr::125_'
        #u'property'
        CDvQuantity(list,property)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at1007'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'|'
        #0
        #u'|'
        #u'precision'
        #u'|'
        #1000.0
        #u'<'
        #u'..'
        #0.0
        #u'|'
        #u'magnitude'
        #u'mm_Hg_'
        #u'units'
        #u'"1"'
        #u'list'
        #u'_openehr::125_'
        #u'property'
        CDvQuantity(list,property)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at1006'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'|'
        #0
        #u'|'
        #u'precision'
        #u'|'
        #1000.0
        #u'<'
        #u'..'
        #0.0
        #u'|'
        #u'magnitude'
        #u'mm_Hg_'
        #u'units'
        #u'"1"'
        #u'list'
        #u'_openehr::125_'
        #u'property'
        CDvQuantity(list,property)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0005'
        Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)
        #u'|'
        #0
        #u'|'
        #u'precision'
        #u'|'
        #1000.0
        #u'<'
        #u'..'
        #0.0
        #u'|'
        #u'magnitude'
        #u'mm_Hg_'
        #u'units'
        #u'"1"'
        #u'list'
        #u'_openehr::125_'
        #u'property'
        CDvQuantity(list,property)
        #u'value'
        #1
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0004'
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
        nodeid=u'at0003'
        ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)
        #u'data'
        #u'*'
        #u'..'
        #0
        #u'occurrences'
        nodeid=u'at0006'
        Event(time,data,state,parent,offset)
        #u'unordered'
        #u'*'
        #u'..'
        #1
        #u'cardinality'
        #u'events'
        #1
        #u'..'
        #1
        nodeid=u'at0001'
        History(origin,events,period,duration,summary,uid,nodeid,name,atdetails,fdraudit,links)
        #u'data'
        #1
        #u'..'
        #1
        nodeid=u'at0000'
        self.definition=Observation(data,state,nodeid,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)
