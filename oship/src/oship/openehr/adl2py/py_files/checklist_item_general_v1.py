#This file was created with create_pyfiles.py from the OSHIP project Release 1.0a2.
#Its quality is not guaranteed and will likely need hand editing before use.

#First write the parsed_adl out so it can be used as a Python structure.  A bit messy but it works.

def getAtId(parsed_adl):
    return u'openEHR-EHR-CLUSTER.checklist_item-general.v1'
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
  

termCode=ArchetypeTerm([u'en', {u'at0000': {u'text': u'Check list item', u'description': u'Item on a checklist.', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0000.1': {u'text': u'General check list item', u'description': u'General item on a checklist.', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0001': {u'text': u'Answer', u'description': u'The answer to the question.', u'bind': None}}])
termCode=ArchetypeTerm([u'en', {u'at0002': {u'text': u'Comment', u'description': u'A comment on the answer.', u'bind': None}}])class ChecklistItemGeneralV1(Archetype,grok.Container):

    implements(IArchetype)

    def __init__(self):
        self.archetypeId=getAtId()
        self.adlVersion = getVersion()
        self.archetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.archetype[1])))
        self.concept = unicode(parsed_adl.concept)
        self.parentArchetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.specialize)))
