#This file was created with create_pyfiles.py from the OSHIP project Release 1.0a2.
#Its quality is not guaranteed and will likely need hand editing before use.

#First write the parsed_adl out so it can be used as a Python structure.  A bit messy but it works.

def getAtId(parsed_adl):
    return u'openEHR-EHR-EVALUATION.alert.v1'
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
  

termCode=ArchetypeTerm([u'en', {u'at0000': {u'text': u'Alert', u'description': u'Information pertaining to a subject of care that may need special considertation by a healthcare provider before making a decision about his/her actions in order to avert an unfavourable healthcare event, or relate to the safety of subject or providers, or pertain to special circumstances relevant to the delivery of care', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0001': {u'text': u'List', u'description': u'@ internal @', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0002': {u'text': u'Category', u'description': u'The category of alert', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0003': {u'text': u'Description', u'description': u'Details of the alert', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0004': {u'text': u'Start of alert', u'description': u'The date/time that the issue or event commenced', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0005': {u'text': u'Certainty', u'description': u'An indication of confidence concerning the existence of the alert', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0006': {u'text': u'Confirmed', u'description': u'The event or alert has been confirmed', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0007': {u'text': u'Suspected', u'description': u'The issue of event is suspected to be present', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0008': {u'text': u'Discounted', u'description': u'The issue or event has been discounted', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0009': {u'text': u'Status', u'description': u'An indication of whether the alert is considered to be an active or inactive issue', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0010': {u'text': u'Review on', u'description': u'The date and time the alert requires review', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0011': {u'text': u'Active', u'description': u'The alert is active', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0012': {u'text': u'Inactive', u'description': u'The alert is not active at present', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0013': {u'text': u'Resolved', u'description': u'The alert has resolved', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0014': {u'text': u'End of alert', u'description': u'The end of the alert period if known', u'bind': None}}])class AlertV1(Archetype,grok.Container):

    implements(IArchetype)

    def __init__(self):
        self.archetypeId=getAtId()
        self.adlVersion = getVersion()
        self.archetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.archetype[1])))
        self.concept = unicode(parsed_adl.concept)
        self.parentArchetypeId=ArchetypeId(ObjectId(u''))
