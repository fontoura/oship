#This file was created with create_pyfiles.py from the OSHIP project Release 1.0a.
#Its quality is not guaranteed and will likely need hand editing before use.
#The files should then be moved to the appropriate directory under oship/km/openehr.
#You should also move the matching ADL file to the same location.

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
  
class AlertV1(Archetype,grok.Container):

    implements(IArchetype)

    def __init__(self,parsed_adl):
        self.adlVersion = unicode(parsed_adl.archetype.adl_version)
        self.archetypeId = ArchetypeId(ObjectId(unicode(parsed_adl.archetype[1])))
        self.concept = unicode(parsed_adl.concept)
        self.parentArchetypeId=ArchetypeId(ObjectId(u''))
