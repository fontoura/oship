# Hand developed representation of the ADL archetype in Python
# Author - Timothy W. Cook - October 2008
# For demonstration purposes only



# this section are required imports for (almost?) all archetypes
import grok
import datetime

from zope.interface import implements
from zope.schema import Set

from oship.openehr.am.archetype.archetype import Archetype
from oship.openehr.rm.support.identification.archetypeid import ArchetypeId
from oship.openehr.rm.support.identification.objectref import ObjectRef
from oship.openehr.rm.support.identification.objectid import ObjectId
from oship.openehr.am.archetype.interfaces.archetype import IArchetype
from oship.openehr.am.archetype.constraintmodel.ccomplexobject import CComplexObject
from oship.openehr.am.archetype.ontology.archetypeontology import ArchetypeOntology
from oship.openehr.rm.support.identification.terminologyid import TerminologyId
from oship.openehr.am.archetype.constraintmodel.cardinality import Cardinality
from oship.openehr.rm.support.interval import Interval


# this section is archetype specific though many apply to almost all archetypes
from oship.openehr.rm.datastructures.itemstructure.representation.cluster import Cluster
from oship.openehr.rm.datastructures.itemstructure.representation.element import Element
from oship.openehr.rm.datatypes.text.dvtext import DvText
from oship.openehr.rm.datatypes.text.codephrase import CodePhrase


class ChecklistItemGeneral(Archetype,grok.Container):
    """
    description
    original_author = <
        ["name"] = <"unknown">
    >
    details = <
        ["en"] = <
            language = <[ISO_639-1::en]>
            purpose = <"For constructing specialised checklist items.">
            use = <"">
            keywords = <"abstract", ...>
            misuse = <"">
        >
    >
    lifecycle_state = <"0">
    other_contributors = <>

    """
    
    implements(IArchetype)
    
    def __init__(self):
        self.adlVersion = u"1.4"
        self.archetypeId = ArchetypeId(u"openEHR-EHR-CLUSTER.checklist_item-general.v1")
        self.parentArchetypeId = ArchetypeId(u"openEHR-EHR-CLUSTER.checklist_item.v1")
        self.concept = u"at0000.1"
        self.description = None  # this really should be set to a Resource Description object.
        self.isControlled = True
        self.originalLanguage = CodePhrase(TerminologyId((u"ISO_639-1")),u"en")
        self.translations = None
        self.uid = None
        self.invariants = None
        self.revisionHistory = None
        
        self.__name__ = datetime.datetime.now().isoformat()   # just to generate a random name for the demo 
        
        # the modeling of the ontology, or at least our implementation of the ontology needs work because we do not actually carry 
        # the languages, or content of the description and text into the instance.  Since this is a specialization
        # we also do not have the parent archetype ontology info in this one.
        self.ontology = ArchetypeOntology()
        self.ontology.terminologiesAvailable=[u'N/A']
        self.ontology.specialisationDepth=1
        self.ontology.termCodes=[u'at0000',u'at0000.1',u'at0001',u'at0002']
        self.ontology.constraintCodes=[u'N/A']
        self.ontology.termAttributeNames=[u'description',u'text']
        self.ontology.parentArchetype=ObjectRef(ObjectId(u"test_id"),u"openEHR",u"ANY")
        
        # Now setup the definition section
        card=Cardinality(False,True,Interval(lower=0, upper=Largest(), lower_included=False, upper_included=False))
        
        attributes=Set()
        assumedValue=None
        rmTypeName=u"openEHR"
        occurrences=1
        nodeId=u"at0000.1"
        parent=u"openEHR-EHR-CLUSTER.checklist_item.v1"
        self.definition = CComplexObject(attributes,assumedValue,rmTypeName,occurrences,nodeId,parent)
        
        
        """
        
        definition
            CLUSTER[at0000.1] matches {	-- General check list item
                                        items cardinality matches {0..*; unordered} matches {
                                            ELEMENT[at0001] matches {	-- Answer
                                                                    value matches {
                                                                        DV_TEXT matches {
                                                                            value matches {"", "Yes", "No", "Not asked", "Not Applicable"}
                                                                        }
                                                                    }
                                                                    }
                                            ELEMENT[at0002] occurrences matches {0..1} matches {	-- Comment
                                                                                                        value matches {
                                                                                                            DV_TEXT matches {*}
                                                                                                        }
                                                                                                        }
                                        }
                                        }
        """



"""
ontology
    term_definitions = <
        ["en"] = <
            items = <
                ["at0000"] = <
                    description = <"Item on a checklist.">
                    text = <"Check list item">
                >
                ["at0000.1"] = <
                    description = <"General item on a checklist.">
                    text = <"General check list item">
                >
                ["at0001"] = <
                    description = <"The answer to the question.">
                    text = <"Answer">
                >
                ["at0002"] = <
                    description = <"A comment on the answer.">
                    text = <"Comment">
                >
            >
        >
    >

"""
