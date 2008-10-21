# Hand developed representation of the ADL archetype in Python
# Author - Timothy W. Cook - October 2008
# For demonstration and testing purposes only

import grok
from zope.interface import implements

from oship.openehr.am.archetype.archetype import Archetype
from oship.openehr.am.archetype.interfaces.archetype import IArchetype

from oship.openehr.rm.datastructures.itemstructure.representation.cluster import Cluster
from oship.openehr.rm.datastructures.itemstructure.representation.element import Element
from oship.openehr.rm.datatypes.text.dvtext import DvText


class openEHREHRCLUSTERchecklist_itemgeneralv1(Archetype,grok.Model):
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
        self.__name__ = u"openEHR-EHR-CLUSTER.checklist_item-general.v1"
                
        
        
        
"""
archetype (adl_version=1.4)
    openEHR-EHR-CLUSTER.checklist_item-general.v1
specialize
    openEHR-EHR-CLUSTER.checklist_item.v1

concept
    [at0000.1]	-- General check list item
language
    original_language = <[ISO_639-1::en]>

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
