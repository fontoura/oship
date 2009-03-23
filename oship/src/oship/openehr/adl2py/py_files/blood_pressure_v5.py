#This file was created with create_pyfiles.py from the OSHIP project Release 1.0a2.
#Its quality is not guaranteed and will likely need hand editing before use.

#First write the parsed_adl out so it can be used as a Python structure.  A bit messy but it works.

def getAtId(parsed_adl):
    return u'openEHR-EHR-OBSERVATION.blood_pressure.v5'
def getVersion(parsed_adl):
    return 1.4


import sys
import oship.newsyspath
sys.path[0:0] = mypath()
import grok
import datetime
from zope.interface import implements
from zope.schema import Set
from oship.openehr.archetype import Archetype
from oship.openehr.support import ArchetypeId
from oship.openehr.support import ObjectRef
from oship.openehr.support import ObjectId
from oship.openehr.archetype import IArchetype
from oship.openehr.archetype import CComplexObject
from oship.openehr.archetype import ArchetypeOntology
from oship.openehr.support import TerminologyId
from oship.openehr.archetype import Cardinality
from oship.openehr.support import Interval   
  

termCode=ArchetypeTerm([u'de', {u'at0000': {u'text': u'Blutdruckmessung', u'description': u'Die Messung des systemischen arteriellen Blutdrucks, die als geeignet angesehen wird, den tats\xe4chlichen systemischen Blutdruck zu repr\xe4sentieren.', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0001': {u'text': u'Historie', u'description': u'Historie', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0002': {u'text': u'Basismessung', u'description': u'Basismessung', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0003': {u'text': u'*blood pressure(en)', u'description': u'*@ internal @(en)', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0004': {u'text': u'systolisch', u'description': u'Der h\xf6chste arterielle Blutdruck eines Zyklus - gemessen in der systolischen oder Kontraktionsphase des Herzens.', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0005': {u'text': u'diastolisch', u'description': u'Der minimale systemische arterielle Blutdruck eines Zyklus - gemessen in der diastolischen oder Entspannungsphase des Herzens.', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0006': {u'text': u'unbestimmtes Ereignis', u'description': u'anderes unbestimmtes Ereignis', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0007': {u'text': u'*state structure(en)', u'description': u'*@ internal @(en)', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0008': {u'text': u'Position', u'description': u'Die Position des Patienten zum Zeitpunkt der Blutdruckmessung', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0009': {u'text': u'Anstrengungsniveau', u'description': u'Das Anstrengungsniveau zum Zeitpunkt der Messung', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0010': {u'text': u'k\xf6rperliche Belastung', u'description': u'Die Beschreibung, ob und wann eine Leibes\xfcbung durchgef\xfchrt wurde bzw. eine k\xf6rperliche Belastung bestand.', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0011': {u'text': u'Listenstruktur', u'description': u'Listenstruktur', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0012': {u'text': u'Instrument', u'description': u'Das Instrument, das zur Blutdruckmessung benutzt wird', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0013': {u'text': u'Manschettengr\xf6\xdfe', u'description': u'Die Gr\xf6\xdfe der Manschette des benutzten Sphygmomanometers', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0014': {u'text': u'Ort der Messung', u'description': u'Ort der Blutdruckmessung', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0015': {u'text': u'Erwachsener', u'description': u'Eine normale Manschette f\xfcr Erwachsene', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0016': {u'text': u'Erwachsener (weit)', u'description': u'Eine Manschette f\xfcr Erwachsene mit dickeren Armen', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0017': {u'text': u'P\xe4diatrisch', u'description': u'Eine Manschette geeignet f\xfcr ein Kind mit d\xfcnnen Armen', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0022': {u'text': u'In Ruhe', u'description': u'Die Person ist in Ruhe und nicht in der Erholungsphase von einer Anstrengung', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0023': {u'text': u'Nach Leibes\xfcbung/k\xf6rperlicher Belastung', u'description': u'Die Messung wird unmittelbar nach einer Leibes\xfcbung/k\xf6rperlicher Belastung durchgef\xfchrt', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0024': {u'text': u'W\xe4hrend Leibes\xfcbung/k\xf6rperlicher Belastung', u'description': u'Die Messung wird w\xe4hrend einer Leibes\xfcbung/k\xf6rperlicher Belastung durchgef\xfchrt', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0025': {u'text': u'Rechter Arm', u'description': u'Der rechte Arm der Person', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0026': {u'text': u'Linker Arm', u'description': u'Der linke Arm der Person', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0027': {u'text': u'Rechtes Bein', u'description': u'Rechtes Bein des Patienten', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0028': {u'text': u'Linkes Bein', u'description': u'Linkes Bein des Patienten', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0029': {u'text': u'5-Minuten-Messung', u'description': u'Blutdruckmessung nach 5 Minuten Ruhepause', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0030': {u'text': u'10-Minuten-Messung', u'description': u'Blutdruckmessung nach 10 Minuten Ruhepause', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0031': {u'text': u'posturale \xc4nderung', u'description': u'Die Differenz zwischen stehendem und sitzendem/liegendem Blutdruck', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0032': {u'text': u'Intra-arteriell', u'description': u'Blutdruckmessung durch intra-arterielle (invasive) Messung', u'bind': None}}])
termCode=ArchetypeTerm([u'de', {u'at0033': {u'text': u'Kommentar', u'description': u'Kommentar zur Blutdruckmessung', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0000': {u'text': u'Blood Pressure', u'description': u'The measurement by any means (invasive or non-invasive) of systemic arterial blood pressure which is deemed to represent the actual systemic blood pressure', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0001': {u'text': u'history', u'description': u'history Structural node', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0002': {u'text': u'Baseline reading', u'description': u'Baseline event in event history', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0003': {u'text': u'blood pressure', u'description': u'@ internal @', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0004': {u'text': u'Systolic', u'description': u'Peak systemic arterial blood pressure over one cycle - measured in systolic or contraction phase of the heart cycle', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0005': {u'text': u'Diastolic', u'description': u'Minimum systemic arterial blood pressure over one cycle - measured in the diastolic or relaxation phase', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0006': {u'text': u'any event', u'description': u'other event in event history', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0007': {u'text': u'state structure', u'description': u'@ internal @', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0008': {u'text': u'Position', u'description': u'The position of the patient at the time of measuring blood pressure', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0009': {u'text': u'Exertion level', u'description': u'The level of exertion at the time of taking the measurement', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0010': {u'text': u'Exercise', u'description': u'The classification of the exercise level', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0011': {u'text': u'list structure', u'description': u'list structure', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0012': {u'text': u'Instrument', u'description': u'The instrument used to measure the blood pressure', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0013': {u'comment': u'http://www.americanheart.org/presenter.jhtml?identifier=3000861', u'text': u'Cuff size', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0014': {u'comment': u'http://hyper.ahajournals.org/cgi/content/full/45/1/142', u'text': u'Location of measurement', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0015': {u'text': u'Adult', u'description': u'A cuff that is standard for an adult - bladder approx 13cm x 30cm', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0016': {u'text': u'Large Adult', u'description': u'A cuff for adults with larger arms - bladder approx 16cm x 38cm', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0017': {u'text': u'Paediatric/Child', u'description': u'A cuff that is appropriate for a child or thin arm - bladder approx 8cm x 21 cm', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0022': {u'text': u'At rest', u'description': u'The person is at rest and not in the recovery phase from exersion', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0023': {u'text': u'Post-exercise', u'description': u'Measurement is taken immediately after exercise', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0024': {u'text': u'During exercise', u'description': u'The measurement is taken during exercise', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0025': {u'text': u'Right arm', u'description': u'The right arm of the person', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0026': {u'text': u'Left arm', u'description': u'The left arm of the person', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0027': {u'text': u'Right leg', u'description': u'The right leg of the patient', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0028': {u'text': u'Left leg', u'description': u'The left leg of the person', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0029': {u'text': u'5 minute reading', u'description': u'Blood pressure reading after 5 minutes rest', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0030': {u'text': u'10 minute reading', u'description': u'Blood pressure reading after 10 minutes rest', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0031': {u'text': u'Postural change', u'description': u'The difference between standing and sitting/lying blood pressure', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0032': {u'text': u'Intra-arterial', u'description': u'Blood pressure monitored via an intra-arterial line', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0033': {u'text': u'Comment', u'description': u'Comment on blood pressure reading', u'bind': None}}])class BloodPressureV5(Archetype,grok.Container):

    implements(IArchetype)

    def __init__(self):
        self.archetypeId=getAtId()
        self.adlVersion = getVersion()
        self.archetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.archetype[1])))
        self.concept = unicode(parsed_adl.concept)
        self.parentArchetypeId=ArchetypeId(ObjectId(u''))
