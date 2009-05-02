#This file was created with atbldr module from the OSHIP project.
#Its quality is not guaranteed and will need hand editing, especially the definition section before use.

import grok
import datetime
from zope.interface import implements
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
        termCodes={u'en':{        u'at0000':[u'text',u'Blood pressure',u'description',u'The measurement of arterial blood pressure which is a surrogate for arterial pressure in the systemic circulation.'],\
        u'at0001':[u'text',u'history',u'description',u'history Structural node'],\
        u'at0003':[u'text',u'blood pressure',u'description',u'@ internal @'],\
        u'at0004':[u'text',u'Systolic',u'description',u'Peak systemic arterial blood pressure over one cycle - measured in systolic or contraction phase of the heart cycle'],\
        u'at0005':[u'text',u'Diastolic',u'description',u'Minimum systemic arterial blood pressure over one cycle - measured in the diastolic or relaxation phase'],\
        u'at0006':[u'text',u'any event',u'description',u'Other event in event history'],\
        u'at0007':[u'text',u'state structure',u'description',u'@ internal @'],\
        u'at0008':[u'text',u'Position',u'description',u'The position of the person at the time of measurement'],\
        u'at0011':[u'text',u'list structure',u'description',u'list structure'],\
        u'at0013':[u'text',u'Cuff size',u'description',u'The size of the cuff used for blood pressure measurement'],\
        u'at0014':[u'text',u'Location of measurement',u'description',u'The site of the measurement of the blood pressure'],\
        u'at0015':[u'text',u'Adult',u'description',u'A cuff that is standard for an adult - bladder approx 13cm x 30cm'],\
        u'at0016':[u'text',u'Large Adult',u'description',u'A cuff for adults with larger arms - bladder approx 16cm x 38cm'],\
        u'at0017':[u'text',u'Paediatric/Child',u'description',u'A cuff that is appropriate for a child or thin arm - bladder approx 8cm x 21cm'],\
        u'at0025':[u'text',u'Right arm',u'description',u'The right arm of the person'],\
        u'at0026':[u'text',u'Left arm',u'description',u'The left arm of the person'],\
        u'at0027':[u'text',u'Right thigh',u'description',u'The right thigh of the person'],\
        u'at0028':[u'text',u'Left thigh',u'description',u'The left thigh of the person'],\
        u'at0031':[u'text',u'Postural change',u'description',u'The difference between standing and sitting/lying blood pressure'],\
        u'at0033':[u'text',u'Comment',u'description',u'Comment on blood pressure measurement'],\
        u'at1000':[u'text',u'Standing',u'description',u'Standing at the time of blood pressure measurement'],\
        u'at1001':[u'text',u'Sitting',u'description',u'Sitting (for example on bed or chair) at the time of blood pressure measurement'],\
        u'at1002':[u'text',u'Reclining',u'description',u'Reclining at the time of blood pressure measurement'],\
        u'at1003':[u'text',u'Lying',u'description',u'Lying flat at the time of blood pressure measurement'],\
        u'at1004':[u'text',u'Paradox',u'description',u'Variation in blood pressure with respiration'],\
        u'at1005':[u'text',u'Tilt',u'description',u'The craniocaudal tilt of the surface on which the person is lying at the time of measurement'],\
        u'at1006':[u'text',u'Mean Arterial Pressure',u'description',u'The average arterial pressure that occurs over the entire course of the heart contraction and relaxation cycle.   '],\
        u'at1007':[u'text',u'Pulse Pressure',u'description',u'The difference between the systolic and diastolic pressure over one contraction cycle.'],\
        u'at1008':[u'text',u'Adult Thigh',u'description',u'A cuff used for an adult thigh - bladder approx 20cm x 42cm'],\
        u'at1009':[u'text',u'Neonatal',u'description',u'A cuff used for a new born - bladder approx 3cm x 6cm'],\
        u'at1010':[u'text',u'Korotkoff sounds',u'description',u'Record which Korotkoff sound is used for determining diastolic pressure'],\
        u'at1011':[u'text',u'Fourth sound',u'description',u'The fourth Korotkoff sound is identified as an abrupt muffling of sounds'],\
        u'at1012':[u'text',u'Fifth sound',u'description',u'The fifth Korotkoff sound is identified by absence of sounds as the cuff pressure drops below the diastolic blood pressure'],\
        u'at1013':[u'text',u'Trendelenburg',u'description',u'Lying flat on the back (supine position) with the feet higher than the head at the time of blood pressure measurement'],\
        u'at1014':[u'text',u'Left Lateral',u'description',u'Lying on the left side at the time of blood pressure measurement'],\
        u'at1018':[u'text',u'Infant',u'description',u'A cuff used for infants - bladder approx 5cm x 15cm'],\
        u'at1019':[u'text',u'Small Adult',u'description',u'A cuff used for a small adult - bladder approx 10cm x 24cm'],\
        u'at1020':[u'text',u'Right wrist',u'description',u'The right wrist of the person'],\
        u'at1021':[u'text',u'Left wrist',u'description',u'The left wrist of the person'],\
        u'at1025':[u'text',u'Device',u'description',u'Details about sphygmomanometer or other device used to measure the blood pressure'],\
        u'at1026':[u'text',u'Finger',u'description',u'A finger of the person'],\
        u'at1030':[u'text',u'Exertion  ',u'description',u'Details about physical activity undertaken at the time of blood pressure measurement'],\
        u'at1031':[u'text',u'Right ankle',u'description',u'The right ankle of the person'],\
        u'at1032':[u'text',u'Left ankle',u'description',u'The left ankle of the person'],\
        u'at1033':[u'text',u'Location',u'description',u'Body site of blood pressure location'],\
        u'at1034':[u'text',u'Description of location',u'description',u'Detailed description about the site of the measurement of the blood pressure'],\
        u'at1035':[u'text',u'Method',u'description',u'Method of measurement of blood pressure'],\
        u'at1036':[u'text',u'Auscultation',u'description',u'Method of measuring blood pressure externally, using a stethoscope and Korotkoff sounds'],\
        u'at1037':[u'text',u'Palpation',u'description',u'Method of measuring blood pressure externally, using palpation (usually of the radial artery at the wrist)'],\
        u'at1038':[u'text',u'Mean Arterial Pressure Formula',u'description',u'Formula used to calculate the MAP (if recorded in data)'],\
        u'at1039':[u'text',u'Machine',u'description',u'Method of measuring blood pressure externally, using a blood pressure machine'],\
        u'at1040':[u'text',u'Invasive',u'description',u'Method of measuring blood pressure internally ie involving penetration of the skin and measuring inside blood vessels'],\
        u'at1041':[u'text',u'Anxiety ',u'description',u"Details about the subject's level of anxiety at the time of blood pressure measurement"]}},\
        {u'ja':{        u'at0000':[u'text',u'\u8840\u5727',u'description',u'\u6e2c\u5b9a\u3055\u308c\u3001\u3042\u3089\u3086\u308b\u624b\u6bb5\uff08\u4fb5\u8972\u7684\u307e\u305f\u306f\u975e\u4fb5\u8972\u7684\u306a\uff09\u306e\u5168\u8eab\u52d5\u8108\u8840\u5727\u306e\u5909\u5316\u3092\u8868\u3059\u3082\u306e\u3067\u306f\u3001\u5b9f\u969b\u306e\u5168\u8eab\u306e\u8840\u6db2\u306e\u5727\u529b'],\
        u'at0001':[u'text',u'*history(en)',u'description',u'*history Structural node(en)'],\
        u'at0003':[u'text',u'\u8840\u5727',u'description',u'*@ internal @(en)'],\
        u'at0004':[u'text',u'\u53ce\u7e2e\u671f',u'description',u'1\u3064\u4ee5\u4e0a\u306e\u8108\u306e\u9593\u3067\u6700\u9ad8\u5024\u3092\u793a\u3059\u5168\u8eab\u306e\u52d5\u8108\u5727 - \u5fc3\u6a5f\u56f3\u306e\u53ce\u7e2e\u671f\u3067\u6e2c\u5b9a\u3055\u308c\u308b'],\
        u'at0005':[u'text',u'\u62e1\u5f35\u671f',u'description',u'1\u3064\u4ee5\u4e0a\u306e\u8108\u306e\u9593\u3067\u6700\u4f4e\u5024\u3092\u793a\u3059\u5168\u8eab\u306e\u52d5\u8108\u5727 - \u5fc3\u6a5f\u56f3\u306e\u62e1\u5f35\u671f\u3067\u6e2c\u5b9a\u3055\u308c\u308b'],\
        u'at0006':[u'text',u'\u4efb\u610f\u30a4\u30d9\u30f3\u30c8',u'description',u' \u30a4\u30d9\u30f3\u30c8\u306e\u5c65\u6b74\u306b\u304a\u3051\u308b\u4ed6\u306e\u30a4\u30d9\u30f3\u30c8'],\
        u'at0007':[u'text',u'*state structure(en)',u'description',u'*@ internal @(en)'],\
        u'at0008':[u'text',u'*Position(en)',u'description',u'*The position of the person at the time of measurement(en)'],\
        u'at0011':[u'text',u'*list structure(en)',u'description',u'*list structure(en)'],\
        u'at0013':[u'text',u'\u30ab\u30d5\u30b5\u30a4\u30ba',u'description',u'\u8840\u5727\u8a08\u304c\u4f7f\u7528\u3059\u308b\u30ab\u30d5\u306e\u30b5\u30a4\u30ba'],\
        u'at0014':[u'text',u'\u6e2c\u5b9a\u90e8\u4f4d',u'description',u'\u8840\u5727\u3092\u6e2c\u5b9a\u3059\u308b\u90e8\u4f4d'],\
        u'at0015':[u'text',u'*Adult(en)',u'description',u'*A cuff that is standard for an adult - bladder approx 13cm x 30cm(en)'],\
        u'at0016':[u'text',u'*Large Adult(en)',u'description',u'*A cuff for adults with larger arms - bladder approx 16cm x 38cm(en)'],\
        u'at0017':[u'text',u'*Paediatric/Child(en)',u'description',u'*A cuff that is appropriate for a child or thin arm - bladder approx 8cm x 21cm(en)'],\
        u'at0025':[u'text',u'\u53f3\u8155',u'description',u'*The right arm of the person(en)'],\
        u'at0026':[u'text',u'\u5de6\u8155',u'description',u'*The left arm of the person(en)'],\
        u'at0027':[u'text',u'*Right leg(en)',u'description',u'*The right leg of the person(en)'],\
        u'at0028':[u'text',u'\u5de6\u811a',u'description',u'*The left leg of the person(en)'],\
        u'at0031':[u'text',u'\u59ff\u52e2\u5909\u5316',u'description',u'\u5ea7\u4f4d\u3068\u7acb\u4f4d\u3067\u306e\u8840\u5727\u5909\u5316'],\
        u'at0033':[u'text',u'\u30b3\u30e1\u30f3\u30c8',u'description',u'\u8840\u5727\u6e2c\u5b9a\u306e\u30b3\u30e1\u30f3\u30c8'],\
        u'at1000':[u'text',u'\u7acb\u4f4d',u'description',u'*Standing at the time of blood pressure measurement(en)'],\
        u'at1001':[u'text',u'\u5ea7\u4f4d',u'description',u'*Sitting on bed or chair at the time of blood pressure measurement(en)'],\
        u'at1002':[u'text',u'\u659c\u4f4d',u'description',u'*Person reclining at 45 degrees at the time of blood pressure measurement(en)'],\
        u'at1003':[u'text',u'\u81e5\u4f4d',u'description',u'*Patient lying flat at the time of blood pressure measurement(en)'],\
        u'at1004':[u'text',u'\u5947\u8108',u'description',u'\u547c\u5438\u306b\u3088\u308b\u8840\u5727\u5909\u52d5'],\
        u'at1005':[u'text',u'*Tilt(en)',u'description',u'*The craniocaudal tilt of the surface on which the person is lying at the time of measurement(en)'],\
        u'at1006':[u'text',u'*Mean Arterial Pressure(en)',u'description',u'*The average arterial pressure that occurs over the entire course of the heart contraction and relaxation cycle.   (en)'],\
        u'at1007':[u'text',u'\u8108\u5727',u'description',u'1\u56de\u306e\u53ce\u7e2e\u30b5\u30a4\u30af\u30eb\u3067\u306e\u8840\u5727\u306e\u5909\u52d5'],\
        u'at1008':[u'text',u'*Adult Thigh(en)',u'description',u'*A cuff used for an adult thigh - bladder approx 20cm x 42cm(en)'],\
        u'at1009':[u'text',u'*Neonatal(en)',u'description',u'*A cuff used for a new born - bladder approx 3cm x 6cm(en)'],\
        u'at1010':[u'text',u'\u30b3\u30ed\u30c8\u30b3\u30d5\u97f3',u'description',u'\u62e1\u5f35\u671f\u3092\u6c7a\u5b9a\u3059\u308b\u3068\u304d\u306b\u4f7f\u7528\u3055\u308c\u305f\u30b3\u30ed\u30c8\u30b3\u30d5\u97f3\u306e\u8a18\u9332'],\
        u'at1011':[u'text',u'*Fourth sound(en)',u'description',u'*The fifth Korotkoff sound is silence as the cuff pressure drops below the diastolic blood pressure(en)'],\
        u'at1012':[u'text',u'*Fifth sound(en)',u'description',u'*The fifth Korotkoff sound is silence as the cuff pressure drops below the diastolic blood pressure(en)'],\
        u'at1013':[u'text',u'*Trendelenburg(en)',u'description',u'*Person is lying flat on the back (supine position) with the feet higher than the head at the time of blood pressure measurement(en)'],\
        u'at1014':[u'text',u'*Left Lateral(en)',u'description',u'*Person is lying on their left side at the time of blood pressure measurement(en)'],\
        u'at1018':[u'text',u'*Infant(en)',u'description',u'*A cuff used for infants - bladder approx 5cm x 15cm(en)'],\
        u'at1019':[u'text',u'*Small Adult(en)',u'description',u'*A cuff used for a small adult - bladder approx 10cm x 24cm(en)'],\
        u'at1020':[u'text',u'*Right wrist(en)',u'description',u'*The right wrist of the person(en)'],\
        u'at1021':[u'text',u'*Left wrist(en)',u'description',u'*The left wrist of the person(en)'],\
        u'at1025':[u'text',u'*Device(en)',u'description',u'*Details about sphygmomanometer or other device used to measure the blood pressure(en)'],\
        u'at1026':[u'text',u'Finger',u'description',u'*A finger of the person(en)'],\
        u'at1030':[u'text',u'*Exertion  (en)',u'description',u'*Details about physical activity undertaken at the time of blood pressure measurement(en)'],\
        u'at1031':[u'text',u'*Left ankle(en)',u'description',u'**(en)'],\
        u'at1032':[u'text',u'*Right ankle(en)',u'description',u'*The right ankle of the person(en)'],\
        u'at1033':[u'text',u'*New cluster(en)',u'description',u'**(en)'],\
        u'at1034':[u'text',u'*New element(en)',u'description',u'**(en)'],\
        u'at1035':[u'text',u'*New element(en)',u'description',u'**(en)'],\
        u'at1036':[u'text',u'*Auscultation(en)',u'description',u'*Method of measuring blood pressure externally, using a stethoscope and Korotkoff sounds(en)'],\
        u'at1037':[u'text',u'*Palpation(en)',u'description',u'*Method of measuring blood pressure externally, using palpation (usually of the radial artery at the wrist)(en)'],\
        u'at1038':[u'text',u'*Mean Arterial Pressure Formula(en)',u'description',u'*Formula used to calculate the MAP (if recorded in data)(en)'],\
        u'at1039':[u'text',u'*Machine(en)',u'description',u'*Method of measuring blood pressure externally, using a blood pressure machine(en)'],\
        u'at1040':[u'text',u'*Invasive(en)',u'description',u'*Method of measuring blood pressure internally ie involving penetration of the skin and measuring inside blood vessels(en)'],\
        u'at1041':[u'text',u'*Anxiety (en)',u'description',u"*Details about the subject's level of anxiety at the time of blood pressure measurement(en)"]}},\
        {u'de':{        u'at0000':[u'text',u'Blutdruckmessung',u'description',u'Die Messung des systemischen arteriellen Blutdrucks, die als geeignet angesehen wird, den tats\xe4chlichen systemischen Blutdruck zu repr\xe4sentieren.'],\
        u'at0001':[u'text',u'Historie',u'description',u'Historie'],\
        u'at0003':[u'text',u'Blutdruck',u'description',u'*@ internal @(en)'],\
        u'at0004':[u'text',u'Systolisch',u'description',u'Der h\xf6chste arterielle Blutdruck eines Zyklus - gemessen in der systolischen oder Kontraktionsphase des Herzens.'],\
        u'at0005':[u'text',u'Diastolisch',u'description',u'Der minimale systemische arterielle Blutdruck eines Zyklus - gemessen in der diastolischen oder Entspannungsphase des Herzens.'],\
        u'at0006':[u'text',u'Unbestimmtes Ereignis',u'description',u'anderes unbestimmtes Ereignis'],\
        u'at0007':[u'text',u'*state structure(en)',u'description',u'*@ internal @(en)'],\
        u'at0008':[u'text',u'*Position(en)',u'description',u'*The position of the person at the time of measurement(en)'],\
        u'at0011':[u'text',u'Listenstruktur',u'description',u'Listenstruktur'],\
        u'at0013':[u'text',u'Manschettengr\xf6\xdfe',u'description',u'Die Gr\xf6\xdfe der Manschette des benutzten Sphygmomanometers'],\
        u'at0014':[u'text',u'Ort der Messung',u'description',u'Ort der Blutdruckmessung'],\
        u'at0015':[u'text',u'*Adult(en)',u'description',u'*A cuff that is standard for an adult - bladder approx 13cm x 30cm(en)'],\
        u'at0016':[u'text',u'*Large Adult(en)',u'description',u'*A cuff for adults with larger arms - bladder approx 16cm x 38cm(en)'],\
        u'at0017':[u'text',u'*Paediatric/Child(en)',u'description',u'*A cuff that is appropriate for a child or thin arm - bladder approx 8cm x 21cm(en)'],\
        u'at0025':[u'text',u'Rechter Arm',u'description',u'Der rechte Arm der Person'],\
        u'at0026':[u'text',u'Linker Arm',u'description',u'Der linke Arm der Person'],\
        u'at0027':[u'text',u'*Right leg(en)',u'description',u'*The right leg of the person(en)'],\
        u'at0028':[u'text',u'Linkes Bein',u'description',u'Linkes Bein des Patienten'],\
        u'at0031':[u'text',u'Posturale \xc4nderung',u'description',u'Die Differenz zwischen stehendem und sitzendem/liegendem Blutdruck'],\
        u'at0033':[u'text',u'Kommentar',u'description',u'Kommentar zur Blutdruckmessung'],\
        u'at1000':[u'text',u'Stehend',u'description',u'Stehend zum Zeitpunkt der Blutdruckmessung'],\
        u'at1001':[u'text',u'Sitzend',u'description',u'Sitzend zum Zeitpunkt der Blutdruckmessung'],\
        u'at1002':[u'text',u'Zur\xfcckgelehnt',u'description',u'Patient 45 Grad zur\xfcckgelehnt zum Zeitpunkt der Blutdruckmessung'],\
        u'at1003':[u'text',u'Liegend',u'description',u'Patient flach liegend zum Zeitpunkt der Blutdruckmessung'],\
        u'at1004':[u'text',u'Paradox',u'description',u'Variation des Blutdrucks bei Atmung'],\
        u'at1005':[u'text',u'*Tilt(en)',u'description',u'*The craniocaudal tilt of the surface on which the person is lying at the time of measurement(en)'],\
        u'at1006':[u'text',u'*Mean Arterial Pressure(en)',u'description',u'*The average arterial pressure that occurs over the entire course of the heart contraction and relaxation cycle.   (en)'],\
        u'at1007':[u'text',u'Pulsdruck',u'description',u'Der Abstand zwischen dem systolischen und dem diastolischen Blutdruckwert. Beschreibt die Druckwelle, die mit jedem Herzschlag durch das Blutgef\xe4\xdfsystem l\xe4uft.'],\
        u'at1008':[u'text',u'*Adult Thigh(en)',u'description',u'*A cuff used for an adult thigh - bladder approx 20cm x 42cm(en)'],\
        u'at1009':[u'text',u'*Neonatal(en)',u'description',u'*A cuff used for a new born - bladder approx 3cm x 6cm(en)'],\
        u'at1010':[u'text',u'Korotkoff Ger\xe4usche',u'description',u'Korotkoff Ger\xe4usch, das zur Betimmung des diastolischen Blutdrucks benuzt wurde'],\
        u'at1011':[u'text',u'*Fourth sound(en)',u'description',u'*The fifth Korotkoff sound is silence as the cuff pressure drops below the diastolic blood pressure(en)'],\
        u'at1012':[u'text',u'*Fifth sound(en)',u'description',u'*The fifth Korotkoff sound is silence as the cuff pressure drops below the diastolic blood pressure(en)'],\
        u'at1013':[u'text',u'*Trendelenburg(en)',u'description',u'*Person is lying flat on the back (supine position) with the feet higher than the head at the time of blood pressure measurement(en)'],\
        u'at1014':[u'text',u'*Left Lateral(en)',u'description',u'*Person is lying on their left side at the time of blood pressure measurement(en)'],\
        u'at1018':[u'text',u'*Infant(en)',u'description',u'*A cuff used for infants - bladder approx 5cm x 15cm(en)'],\
        u'at1019':[u'text',u'*Small Adult(en)',u'description',u'*A cuff used for a small adult - bladder approx 10cm x 24cm(en)'],\
        u'at1020':[u'text',u'*Right wrist(en)',u'description',u'*The right wrist of the person(en)'],\
        u'at1021':[u'text',u'*Left wrist(en)',u'description',u'*The left wrist of the person(en)'],\
        u'at1025':[u'text',u'*Device(en)',u'description',u'*Details about sphygmomanometer or other device used to measure the blood pressure(en)'],\
        u'at1026':[u'text',u'*Finger(en)',u'description',u'**(en)'],\
        u'at1030':[u'text',u'*Exertion  (en)',u'description',u'*Details about physical activity undertaken at the time of blood pressure measurement(en)'],\
        u'at1031':[u'text',u'*Left ankle(en)',u'description',u'**(en)'],\
        u'at1032':[u'text',u'*Right ankle(en)',u'description',u'*The right ankle of the person(en)'],\
        u'at1033':[u'text',u'*New cluster(en)',u'description',u'**(en)'],\
        u'at1034':[u'text',u'*New element(en)',u'description',u'**(en)'],\
        u'at1035':[u'text',u'*New element(en)',u'description',u'**(en)'],\
        u'at1036':[u'text',u'*Auscultation(en)',u'description',u'*Method of measuring blood pressure externally, using a stethoscope and Korotkoff sounds(en)'],\
        u'at1037':[u'text',u'*Palpation(en)',u'description',u'*Method of measuring blood pressure externally, using palpation (usually of the radial artery at the wrist)(en)'],\
        u'at1038':[u'text',u'*Mean Arterial Pressure Formula(en)',u'description',u'*Formula used to calculate the MAP (if recorded in data)(en)'],\
        u'at1039':[u'text',u'*Machine(en)',u'description',u'*Method of measuring blood pressure externally, using a blood pressure machine(en)'],\
        u'at1040':[u'text',u'*Invasive(en)',u'description',u'*Method of measuring blood pressure internally ie involving penetration of the skin and measuring inside blood vessels(en)'],\
        u'at1041':[u'text',u'*Anxiety (en)',u'description',u"*Details about the subject's level of anxiety at the time of blood pressure measurement(en)"]}},\
        {u'zh-cn':{        u'at0000':[u'text',u'\u8840\u538b',u'description',u'\u4ee5\u4efb\u4f55\u65b9\u5f0f\u6d4b\u91cf\u7684\u7cfb\u7edf\u6027\u52a8\u8109\u8840\u538b\u7684\u538b\u529b\uff0c \u88ab\u8ba4\u4e3a\u662f\u4ee3\u8868\u5b9e\u9645\u7684\u7cfb\u7edf\u6027\u8840\u538b'],\
        u'at0001':[u'text',u'*history(en)',u'description',u'*history Structural node(en)'],\
        u'at0003':[u'text',u'\u8840\u538b',u'description',u'*@ internal @(en)'],\
        u'at0004':[u'text',u'\u6536\u7f29\u538b',u'description',u'\u4e00\u4e2a\u8840\u6db2\u5faa\u73af\u5468\u671f\u4e2d\uff0c\u7cfb\u7edf\u6027\u52a8\u8109\u8840\u538b\u9ad8\u5cf0\u503c\u3002 \u6536\u7f29\u671f\u8840\u538b'],\
        u'at0005':[u'text',u'\u8212\u5f20\u538b',u'description',u'\u4e00\u4e2a\u8840\u6db2\u5faa\u73af\u5468\u671f\u4e2d\uff0c\u7cfb\u7edf\u6027\u52a8\u8109\u8840\u538b\u6700\u4f4e\u503c\u3002 \u8212\u5f20\u671f\u8840\u538b'],\
        u'at0006':[u'text',u'*any event(en)',u'description',u'*other event in event history(en)'],\
        u'at0007':[u'text',u'*state structure(en)',u'description',u'*@ internal @(en)'],\
        u'at0008':[u'text',u'*Position(en)',u'description',u'*The position of the person at the time of measurement(en)'],\
        u'at0011':[u'text',u'*list structure(en)',u'description',u'*list structure(en)'],\
        u'at0013':[u'text',u'\u8896\u5e26\u5c3a\u5ea6',u'description',u'\u8840\u538b\u8ba1\u8896\u5e26\u5c3a\u5ea6'],\
        u'at0014':[u'text',u'\u6d4b\u91cf\u90e8\u4f4d',u'description',u'\u6d4b\u91cf\u8840\u538b\u7684\u90e8\u4f4d'],\
        u'at0015':[u'text',u'*Adult(en)',u'description',u'*A cuff that is standard for an adult - bladder approx 13cm x 30cm(en)'],\
        u'at0016':[u'text',u'*Large Adult(en)',u'description',u'*A cuff for adults with larger arms - bladder approx 16cm x 38cm(en)'],\
        u'at0017':[u'text',u'*Paediatric/Child(en)',u'description',u'*A cuff that is appropriate for a child or thin arm - bladder approx 8cm x 21cm(en)'],\
        u'at0025':[u'text',u'\u53f3\u81c2',u'description',u'\u88ab\u6d4b\u8bd5\u8005\u53f3\u81c2'],\
        u'at0026':[u'text',u'\u5de6\u81c2',u'description',u'\u88ab\u6d4b\u8bd5\u8005\u5de6\u81c2'],\
        u'at0027':[u'text',u'*Right leg(en)',u'description',u'*The right leg of the person(en)'],\
        u'at0028':[u'text',u'\u5de6\u817f',u'description',u'\u88ab\u6d4b\u8bd5\u8005\u5de6\u4e0b\u80a2'],\
        u'at0031':[u'text',u'\u59ff\u52bf\u53d8\u5316',u'description',u'\u7531\u4f53\u4f4d\u53d8\u52a8\u5f15\u8d77\u7684\u8840\u538b\u503c\u53d8\u5316'],\
        u'at0033':[u'text',u'\u6ce8\u91ca',u'description',u'\u6709\u5173\u8840\u538b\u503c\u7684\u6ce8\u91ca'],\
        u'at1000':[u'text',u'\u7acb\u4f4d',u'description',u'\u6d4b\u91cf\u8840\u538b\u65f6\u8eab\u4f53\u5904\u4e8e\u7ad9\u7acb\u4f53\u4f4d'],\
        u'at1001':[u'text',u'\u5750\u4f4d',u'description',u'\u6d4b\u91cf\u8840\u538b\u65f6\u8eab\u4f53\u5904\u4e8e\u5750\u4f4d'],\
        u'at1002':[u'text',u'\u4fa7\u5367\u4f4d',u'description',u'\u6d4b\u91cf\u8840\u538b\u65f6\u8eab\u4f53\u5904\u4e8e45\u5ea6\u89d2\u4fa7\u5367\u4f4d'],\
        u'at1003':[u'text',u'\u5367\u4f4d',u'description',u'\u6d4b\u91cf\u8840\u538b\u65f6\u8eab\u4f53\u5904\u4e8e\u5e73\u5367\u4f4d'],\
        u'at1004':[u'text',u'\u5947\u8109',u'description',u'\u5947\u8109\u65f6\u5f15\u8d77\u8840\u538b\u53d8\u5316'],\
        u'at1005':[u'text',u'*Tilt(en)',u'description',u'*The craniocaudal tilt of the surface on which the person is lying at the time of measurement(en)'],\
        u'at1006':[u'text',u'*Mean Arterial Pressure(en)',u'description',u'*The average arterial pressure that occurs over the entire course of the heart contraction and relaxation cycle.   (en)'],\
        u'at1007':[u'text',u'\u8109\u538b',u'description',u'*The variation in pressure over one contraction cycle(en)'],\
        u'at1008':[u'text',u'*Adult Thigh(en)',u'description',u'*A cuff used for an adult thigh - bladder approx 20cm x 42cm(en)'],\
        u'at1009':[u'text',u'*Neonatal(en)',u'description',u'*A cuff used for a new born - bladder approx 3cm x 6cm(en)'],\
        u'at1010':[u'text',u'\u514b\u592b\u97f3\u6548',u'description',u'*Record which Korotkoff sound is used for determining Diastolic pressure(en)'],\
        u'at1011':[u'text',u'*Fourth sound(en)',u'description',u'*The fifth Korotkoff sound is silence as the cuff pressure drops below the diastolic blood pressure(en)'],\
        u'at1012':[u'text',u'*Fifth sound(en)',u'description',u'*The fifth Korotkoff sound is silence as the cuff pressure drops below the diastolic blood pressure(en)'],\
        u'at1013':[u'text',u'*Trendelenburg(en)',u'description',u'*Person is lying flat on the back (supine position) with the feet higher than the head at the time of blood pressure measurement(en)'],\
        u'at1014':[u'text',u'*Left Lateral(en)',u'description',u'*Person is lying on their left side at the time of blood pressure measurement(en)'],\
        u'at1018':[u'text',u'*Infant(en)',u'description',u'*A cuff used for infants - bladder approx 5cm x 15cm(en)'],\
        u'at1019':[u'text',u'*Small Adult(en)',u'description',u'*A cuff used for a small adult - bladder approx 10cm x 24cm(en)'],\
        u'at1020':[u'text',u'*Right wrist(en)',u'description',u'*The right wrist of the person(en)'],\
        u'at1021':[u'text',u'*Left wrist(en)',u'description',u'*The left wrist of the person(en)'],\
        u'at1025':[u'text',u'*Device(en)',u'description',u'*Details about sphygmomanometer or other device used to measure the blood pressure(en)'],\
        u'at1026':[u'text',u'*Finger(en)',u'description',u'*A finger of the person(en)'],\
        u'at1030':[u'text',u'*Exertion  (en)',u'description',u'*Details about physical activity undertaken at the time of blood pressure measurement(en)'],\
        u'at1031':[u'text',u'*Left ankle(en)',u'description',u'**(en)'],\
        u'at1032':[u'text',u'*Right ankle(en)',u'description',u'*The right ankle of the person(en)'],\
        u'at1033':[u'text',u'*New cluster(en)',u'description',u'**(en)'],\
        u'at1034':[u'text',u'*New element(en)',u'description',u'**(en)'],\
        u'at1035':[u'text',u'*New element(en)',u'description',u'**(en)'],\
        u'at1036':[u'text',u'*Auscultation(en)',u'description',u'*Method of measuring blood pressure externally, using a stethoscope and Korotkoff sounds(en)'],\
        u'at1037':[u'text',u'*Palpation(en)',u'description',u'*Method of measuring blood pressure externally, using palpation (usually of the radial artery at the wrist)(en)'],\
        u'at1038':[u'text',u'*Mean Arterial Pressure Formula(en)',u'description',u'*Formula used to calculate the MAP (if recorded in data)(en)'],\
        u'at1039':[u'text',u'*Machine(en)',u'description',u'*Method of measuring blood pressure externally, using a blood pressure machine(en)'],\
        u'at1040':[u'text',u'*Invasive(en)',u'description',u'*Method of measuring blood pressure internally ie involving penetration of the skin and measuring inside blood vessels(en)'],\
        u'at1041':[u'text',u'*Anxiety (en)',u'description',]}}

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
