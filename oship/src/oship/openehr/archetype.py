# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the MPL license.
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################

"""

From the Archetype specifications

"""
__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'Roger Erens <roger.erens@e-s-c.biz>'


from zope.interface import Interface,implements
from zope.i18nmessageid import MessageFactory
from zope.schema import TextLine,Object,Set,Field,Int,List,Bool,Date,Datetime,Float,Time,Field,Dict
from zope.schema.fieldproperty import FieldProperty

import grok

from support import IArchetypeId,Interval,IHierObjectId,IObjectRef
from common import AuthoredResource


_ = MessageFactory('oship')


class ICAttribute(Interface):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    rmAttributeName=TextLine(
        title=_(u"RM Attribute Name"),
        description=_(u"Reference model attribute within the enclosed type representedby a CObject."),
        
    )
    
    existence=Int(
        title=_(u"Existence"),
        description=_(u"Indicates whether the target object exists or not."),
        
    )
    
    children=List(
        title=_(u"Children"),
        description=_(u"Child constraint nodes."),
        required=False,
        value_type=Object(schema=IObjectRef),
    )
    

class ICComplexObject(Interface):
    """
    Constraint on complex objects.
    """
    
    attributes=Set(
        title=_(u"Attributes"),
        description=_(u"List of constraints on attributes of the reference model."),
        required=False,
        value_type=Object(schema=ICAttribute),
    )

    anyAllowed=Bool(
        title=_(u"Any Allowed"),
        description=_(u"True if any value of the reference model is allowed."),
        
    )
    
    def anyAllowed():
        """True if any value of the reference model is allowed.
        """
class IArchetypeOntology(Interface):
    """
    Local ontology of an archetype.
    """
    
    terminologiesAvailable=List(
        title=_(u"Terminologies"),
        description=_(u"List of terminologies in this ontology."),
        
        value_type=TextLine(),
    )

    specialisationDepth=Int(
        title=_(u"Specialisation Depth"),
        description=_(u"Specialisation depth of this archetype."),
        
    )
    
    termCodes=List(
        title=_(u"Term Codes"),
        description=_(u"List of all term codes in this archetype."),
        
        value_type=TextLine(),
    )

    constraintCodes=List(
        title=_(u"Constraint Codes"),
        description=_(u"List of all constraint codes in this archetype."),
        
        value_type=TextLine(),
    )
    
    termAttributeNames=List(
        title=_(u"Term Attribute Names"),
        description=_(u"List of attribute names in this archetype ontology."),
        
        value_type=TextLine(),
    )

    parentArchetype=Object(
        schema=IObjectRef,  
        title=_(u"Parent"),
        description=_(u"Archetype which owns this ontology."),
        required=False,
    )

    def hasLanguage(aLang):
        """
        True if aLang is present in ontology.
        """
        
    def hasTerminology(aTermId):
        """
        True if ontology has aTermId, terminology Id.
        """
        
    def hasTermCode(tcode):
        """
        True if tcode is in termCodes.
        """
        
    def hasConstraintCode(ccode):
        """
        True if ccode is in constraintCodes.
        """
        
    def constraintDefinition(aLang,aCode):
        """
        Constraint definition for aCode expressed in aLang.
        """
        
    def termBinding(aTermId,aCode):
        """
        Return a CodePhrase for aCode in aTermId.
        """
        
    def constraintBinding(aTermId,aCode):
        """
        Return a string that describes the constraint aCode in aTermId usually in the form of a query expression.
        """
        
        
class IExprItem(Interface):
    """
    Abstract parent of allexpression tree items.
    """
    
    type=TextLine(
        title=_(u"Type"),
        description=_(u"Mathematical type name of this expression."),
        
    )
    
class IAssertionVariable(Interface):
    """
    Definition of named variable.
    """
    
    name=TextLine(
        title=_(u"Name"),
        description=_(u"Name of variable."),
        
    )

    definition=TextLine(
        title=_(u"Definition"),
        description=_(u"Formal definition of variable."),
        
    )

        
        
class IAssertion(Interface):
    """
    Structural model of a typed first order predicate logic assertion
    in the forma of an expression tree including optional variable definitions.
    """
    
    tag=TextLine(
        title=_(u"Tag"),
        description=_(u"Used for differentiating multiple assertions."),
        required=False,
    )

    expression=Object(
        schema=IExprItem,
        title=_(u"Expression"),
        description=_(u"Root of expression tree."),
        
    )

    stringExpression=TextLine(
        title=_(u"String Expression"),
        description=_(u"String form of expression."),
        required=False,
    )

    variables=List(
        title=_(u"Variables"),
        description=_(u"Variable definitions used in the assertion."),
        required=False,
        value_type=Object(schema=IAssertionVariable),
    )

class IArchetype(Interface):
    """
    Archetype equivalent to ARCHETYPED class in Common reference model.
    Defines semantics of identfication, lifecycle, versioning, composition 
    and specialisation.
    """
    
    adlVersion = TextLine(
        title = _(u"adlVersion"),
        description = _(u"""ADL version if archteype was read in from an ADL sharable archetype."""),
        required = False,
        readonly = True,
    )
    
    archetypeId=Object(
        schema=IArchetypeId,
        title=_(u"Archetype Id"),
        description=_(u"Multi-axial identifier of this archetype."),
        
    )
    
    uid=Object(
        schema=IHierObjectId,
        title=_(u"UID"),
        description=_(u"OID of this archetype."),
        required=False,
    )
    
    concept=TextLine(
        title=_(u"Concept"),
        description=_(u"The normative meaning of archetype as a whole."),
        
        readonly = True,
    )
    
    parentArchetypeId=Object(
        schema=IArchetypeId,
        title=_(u"Parent Archetype Id"),
        description=_(u"Identifier of the specialsation parent of this archetype."),
        required=False,
    )
    
    definition=Object(
        schema=ICComplexObject,
        title=_(u"Definition"),
        description=_(u"Root node of this archetype."),
        
    )

    ontology=Object(
        schema=IArchetypeOntology,
        title=_(u"Ontology"),
        description=_(u"The ontology of the archetype"),
        
    )

    invariants=Set(
        title=_(u"Invariants"),
        description=_(u"FOPL invariant statements"),
        required=False,
        value_type=Object(schema=IAssertion),
    )

    def version():
        """
        Version string extracted from id.
        """
        
    def previousVersion():
        """
        Version of predecessor if any.
        """
        
    def shortConceptName():
        """
        String extracted from id.
        """
        
    def conceptName():
        """
        Concept string extracted from the ontology.
        """
    
    def physicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        """
        
    def logicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        except the nodeIds are replaced by their meanings from the ontology.
        """
        
    def isSpecialised():
        """
        True if this archetype is a specialisation of another.
        Otherwise it returns False.
        """
        
    def specialisationDepth():
        """
        Return ontology.specialisationDepth
        """
    
    def nodeIdsValid():        
        """
        Return True if every CObject.nodeId is found
        in the ontolgy.termCodes
        """
        
    def internalReferencesValid():
        """
        True if every ArchetypeInternalRef.targetPath
        refers to a legitimate node in the archetype definition.
        """
        
    def constraintReferencesValid():
        """
        True if every ConstraintRef.reference found in CObject nodes
        definition is found in ontology.constraintCodes
        """
        
    def isValid():
        """
        Return True if the archetype is overall valid.
        """


class Archetype(AuthoredResource):
    _(u"""
    Archetype equivalent to ARCHETYPED class in Common reference model.
    Defines semantics of identfication, lifecycle, versioning, composition 
    and specialisation.
    """)
    
    implements(IArchetype)
    
    def __init__(self,adlver,atid,uid,concept,paid,defin,ont,inv,olang,trans,descr,revhist,ctrld):
        AuthoredResource.__init__(self,olang,trans,descr,revhist,ctrld)

        self.adlVersion=adlver
        self.archetypeId=atid
        self.uid=uid
        self.concept=concept
        self.parentArchetypeId=paid
        self.definition=defin
        self.ontology=ont
        self.invariants=inv
            
    def version(self):
        """
        Version string extracted from id.
        """
        return self.archetypeId.versionId(self)
    
    def previousVersion(self):
        """
        Version of predecessor if any.
        """
        return None
    
    def shortConceptName(self):
        """
        String extracted from id.
        """
        
    
    def conceptName(self, language=None):
        """
        Concept string extracted from the ontology.
        """
        return self.archetypeId.conceptName()
    
    def physicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        """
        
    def logicalPaths():
        """
        Set of Xpath like statements extracted from
        CObject.nodeId and CAttribute.rmAttributeName
        except the nodeIds are replaced by their meanings from the ontology.
        """
        
    def isSpecialised(self):
        """
        True if this archetype is a specialisation of another.
        Otherwise it returns False.
        """
        if self.archetypeId.specialisation() == 0:
            return False
        else:
            return True
        
        
    def specialisationDepth():
        """
        Return ontology.specialisationDepth
        """
        return self.ontology.specialisationDepth
    
    def nodeIdsValid():        
        """
        Return True if every CObject.nodeId is found
        in the ontolgy.termCodes
        """
        
    def internalReferencesValid():
        """
        True if every ArchetypeInternalRef.targetPath
        refers to a legitimate node in the archetype definition.
        """
        
    def constraintReferencesValid():
        """
        True if every ConstraintRef.reference found in CObject nodes
        definition is found in ontology.constraintCodes
        """
        
    def isValid():
        """
        Return True if the archetype is overall valid.
        """
        
        
class IValidityKind(Interface):
    """
    An enumeration of three values which may commonly occur in constrint models.
    Use to indicate the validity of date/Time fields etc.
    
    
    #constants
    mandatory=1001
    optional=1002
    disallowed=1003
    """
    value=Int(
        title=_(u"Value"),
        description=_(u"Actual value."),
        
    )

    def validValidity():
        """
        Test if value is == to one of the constants.
        """
        

class ValidityKind(grok.Model):
    _(u"""
    An enumeration of three values which may commonly occur in constrint models.
    Use to indicate the validity of date/Time fields etc.
    """)
    
    implements(IValidityKind)
    
     
    constants={'mandatory':1001,'optional':1002,'disallowed':1003}

    def validValidity():
        """
        Test if value is == to one of the constants.
        """
        



    
class Assertion(grok.Container):
    """
    Structural model of a typed first order predicate logic assertion
    in the forma of an expression tree including optional variable definitions.
    """
    
    implements(IAssertion)
    

    def __init__(self,tag,expr,sexpr,var):
        self.tag=tag
        self.expression=expr
        self.stringExpression=sexpr
        self.variables=var


class AssertionVariable(grok.Model):
    """
    Definition of named variable.
    """
    
    implements(IAssertionVariable)
    
    
    def __init__(self,name,defin):
        self.name=name
        self.definition=defin
        
        
class IOperatorKind(Interface):
    _(u"""
    Enumeration of assertion package operator types.
    
    
    #constants
    opEq=2001  #= or ==
    opNe=2002
    opLe=2003
    opLt=2004
    opGe=2005
    opGt=2006
    opMatches=2007
    
    opNot=2010
    opAnd=2011
    opOr=2012
    opXor=2013
    opImplies=2014
    opForAll=2015
    opExists=2016

    opPlus=2020
    opMinus=2021
    opMultiply=2022
    opDivide=2023
    opExp=2024
    """)
    
    value=Int(
        title=_(u"Value"),
        description=_(u"Actual value of this instance."),
    )

    def validOperator(anOp):
        """
        Return True if anOp is a valid operator.
        """

class IExprOperator(Interface):
    """
    Abstract parent of operator types.
    """
    
    operator=Object(
        schema=IOperatorKind,
        title=_(u"Operator"),
        description=_(u"Code of the operator."),
        
    )

    precedenceOverridden=Bool(
        title=_(u"Precedence Overridden"),
        description=_(u"True if natural precedence of operators is overridden in the expression."),
        
    )

class ExprOperator(grok.Model):
    """
    Abstract parent of operator types.
    """
    implements(IExprOperator)
    
    def __init__(self,operator,precedenceOverridden):
        self.operator=operator
        self.precedenceOverridden=precedenceOverridden
        
    
    
   
class ExprItem(grok.Model):
    """
    Abstract parent of allexpression tree items.
    """
    
    implements(IExprItem)
    def __init__(self,type):
        self.type=type
        
        
class IExprBinaryOperator(Interface):
    """
    Binary expression node.
    """
    
    leftOperand=Object(
        schema=IExprItem,
        title=_(u"Left"),
        description=_(u"Left operand node."),
        
    )

    rightOperand=Object(
        schema=IExprItem,
        title=_(u"Right"),
        description=_(u"Right operand node."),
        
    )


class ExprBinaryOperator(ExprOperator):
    """
    Binary expression node.
    """
    
    implements(IExprBinaryOperator)
    
    def __init__(self,leftOperand,rightOperand,operator,precedenceOverridden):
        self.leftOperand=leftOperand
        self.rightOperand=rightOperand
        ExprOperator.__init__(self,operator,precedenceOverridden)


class IExprLeaf(Interface):
    """
    Expression tree, leaf form.
    """
    
    item=Field(
        title=_(u"Item"),
        description=_(u"The value refered to."),
        
    )

    referenceType=TextLine(
        title=_(u"Reference Type"),
        description=_(u"Type of reference: constant, attribute, etc."),
        
    )

    
class ExprLeaf(ExprItem):
    """
    Expression tree, leaf form.
    """
    
    implements(IExprLeaf)
    
    def __init__(self,item,referenceType,type):
        self.item=item
        self.referenceType=referenceType
        ExprItem.__init__(self,type)
    
class IExprUnaryOperator(Interface):
    """
    Unary expression node operator.
    """
    
    operand=Object(
        schema=IExprItem,
        title=_(u"Operand"),
        description=_(u"Operand node."),
        
    )
    
class ExprUnaryOperator(ExprOperator):
    """
    Unary expression node operator.
    """
    
    implements(IExprUnaryOperator)
    
    def __init__(self,operand,operator,precedenceOverridden):
        ExprOperator.__init__(self,operator,precedenceOverridden)
    
        
class OperatorKind(grok.Model):
    """
    Enumeration of assertion package operator types.
    """
    
    implements(IOperatorKind)
    
    constants={'opEq':2001,'opNe':2002,'opLe':2003,'opLt':2004,'opGe':2005,'opGt':2006,'opMatches':2007,\
               'opNot':2010,'opAnd':2011,'opOr':2012,'opXor':2013,'opImplies':2014,'opForAll':2015,\
               'opExists':2016,'opPlus':2020,'opMinus':2021,'opMultiply':2022,'opDivide':2023,'opExp':2024}

    def validOperator(anOp):
        """
        Return True if anOp is a valid operator.
        """
        return anOp in constants.values()
        
#Begin Constraint package
class IArchetypeConstraint(Interface):
    """
    Archetype equivalent to Locatable class in the Common package of the reference model.
    """
    
    def isSubsetOf(other):
        u"""True if constraints are narrower than this node."""

    def isValid():
        u"""True if this node and sub-nodes are valid for its type."""

    def path():
        """
        Return a string containt the path of this node relative to the archetype root.
        """
        
    def hasPath(aPath):
        """
        Return True if the relative path (aPath) exists at this node.
        """

class ArchetypeConstraint(grok.Container):
    """
    Archetype equivalent to Locatable class in the Common package of the reference model.
    """
    
    implements(IArchetypeConstraint)
    
    def isSubsetOf(other):
        u"""True if constraints are narrower than this node."""

    def isValid():
        u"""True if this node and sub-nodes are valid for its type."""

    def path():
        """
        Return a string containt the path of this node relative to the archetype root.
        """
        
    def hasPath(aPath):
        """
        Return True if the relative path (aPath) exists at this node.
        """
        
class ICObject(Interface):
    """
    Abstract model of constraint on any kind of object node.
    """
    
    rmTypeName=TextLine(
        title=_(u"RM Type Name"),
        description=_(u"Reference model type that this node corresponds to."),
        
    )

    occurrences=Int(
        title=_(u"Occurrences"),
        description=_(u"Occurrences of this object node in the data."),
        
    )

    nodeId=TextLine(
        title=_(u"Node Id"),
        description=_(u"Semantic id of this node."),
        
    )

    
    parent=Object(
        schema=ICAttribute,
        title=_(u"Parent"),
        description=_(u"CAttribute that owns the CObject."),
        required=False,
    )
    
    
class CObject(grok.Model):
    """
    Abstract model of constraint on any kind of object node.
    """
    
    implements(ICObject)
    
    def __init__(self, rmTypeName, occurrences, nodeId, parent):
        self.rmTypeName = rmTypeName
        self.occurrences = occurrences
        self.nodeId = nodeId
        self.parent = parent

    def rmTypeNameValid():
        if (self.rmTypeName != None):
            return self.rmTypeName != ''
        return self.rmTypeName == None
    
    def nodeIdValid():
        if (self.nodeId != None):
            return self.nodeId != ''
        return self.rmTypeName == None
    
    def occurrencesValidity():
        if (self.occurrences != None and self.parent != None):
            return not isinstance(parent, CMultipleAttribute) and occurrences.upper <= 1
        return True
    

        
class ICReferenceObject(Interface):
    """
    Abstract parent of CObject subtypes that are defined by reference.
    """
    
class CReferenceObject(CObject):
    """
    Abstract parent of CObject subtypes that are defined by reference.
    """
    
    implements(ICReferenceObject)
    pass

        
class IArchetypeInternalRef(Interface):
    """
    See the AOM reference document.
    """
    
    targetPath=TextLine(
        title=_(u"Target Path"),
        description=_(u"Reference to an object node using archetype path notation."),
        
    )


class ArchetypeInternalRef(CReferenceObject):
    """
    See the AOM reference document.
    """
    
    implements(IArchetypeInternalRef)
    
    
    def __init__(self,tgtpath):
        self.tgtpath=tgtpath


class IArchetypeSlot(Interface):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    includes=Set(
        title=_(u"Includes"),
        description=_(u"List of constraints defining other archetypes that can be included here."),
        required=False,
        value_type=Object(schema=IAssertion),
    )

    excludes=Set(
        title=_(u"Excludes"),
        description=_(u"List of constraints defining archetypes that cannot be include here."),
        required=False,
        value_type=Object(schema=IAssertion),
    )


class ArchetypeSlot(CReferenceObject):
    """
    Constraint describing a slot where other archetypes can occur.
    """
    
    implements(IArchetypeSlot)
    

    def __init__(self,incl,excl):
        self.includes=incl
        self.excludes=excl
 


class ICardinality(Interface):
    """
    Expresses constraints on the cardinality of container classes.
    """
    
    isOrdered=Bool(
        title=_(u"Ordered"),
        description=_(u"True if members are ordered."),
        
    )

    isUnique=Bool(
        title=_(u"Unique"),
        description=_(u"True if members are unique."),
        
    )
    
    interval=Interval(
        title=_(u"Interval"),
        description=_(u"Interval of this cardinality."),
    )
    
    def isBag():
        """
        Return True if this cardinality represents an unordered set.
        """
        
    def isList():
        """
        Return True if this cardinality represents an ordered, non-unique membership.
        """
        
    def isSet():
        """
        Return True if this cardinality represents an unordered, non-unique membership.
        """
                
class Cardinality(grok.Model):
    """
    Expresses constraints on the cardinality of container classes.
    """
    
    implements(ICardinality)
    
    def __init__(self, isOrdered, isUnique, interval,**kw)    :
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.interval = interval
        
    def isBag():
        """
        Return True if this cardinality represents an unordered set.
        """
        return not self.isOrdered and not self.isUnique
        
    def isList():
        """
        Return True if this cardinality represents an ordered, non-unique membership.
        """
        return (self.isOrdered) and (not self.isUnique)
    
    def isSet():
        """
        Return True if this cardinality represents an unordered, non-unique membership.
        """
        return (not self.isOrdered) and (self.isUnique)
    



   
class CAttribute(ArchetypeConstraint):
    """
    Abstract model of constraint on any kind of attribute code.
    """
    
    implements(ICAttribute)
    
    def __init__(self, rmAttributeName, existence, children,):
        self.rmAttributeName = rmAttributeName
        self.existence = existence
        self.children = children
        
    def rmAttributeNameValid():
        if (self.rmAttributeName != None):
            return self.rmAttributeName != ''
        return self.rmAttributeName == None
    
    def existenceSet():
        if (self.existence != None):
            return self.existence.lower >= 0 and self.existence.upper <= 1
        return self.existence == None
    
    def childrenValidity():
        return xor(issubclass(type(self.children), CObject), self.children != None)
class ICDefinedObject(Interface):
    """
    Abstract parent of CObject subtypes that are defined by this value.
    """
    
    assumedValue=Field(
        title=_(u"Assumed Value"),
        description=_(u"Value to be assumed if none sent in data."),
        required=False,
    )

    def hasAssumedValue():
        """
        Return True if assumedValue is not equal to None.
        """

class CDefinedObject(CObject):
    """
    Abstract parent of CObject subtypes that are defined by this value.
    """
    
    implements(ICDefinedObject)
    
    def __init__(self, rmTypeName, occurence, nodeId, parent, assumedValue):
        CObject.__init__(self, rmTypeName, occurence, nodeId, parent)
        self.assumedValue = assumedValue
        
    def hasAssumedValue():
        """
        Return True if assumedValue is not equal to None.
        """
        return self.returnedValue != None
    
    def validValue(a_value):
        return a_value != None
         

        
class CComplexObject(CDefinedObject):
    """
    Constraint on complex objects.
    """
    
    implements(ICComplexObject)
   
    
    def __init__(self,attributes,assumedValue,rmTypeName,occurrences,nodeId,parent):
        self.attributes=attributes
        self.assumedValue=assumedValue
        self.rmTypeName=rmTypeName
        self.occurrences=occurrences
        self.nodeId=nodeId
        self.parent=parent
        
        
    def anyAllowed():
        if not self.attributes is None:
            return (len(self.attributes) == 0)
        else:
            return (False)
    

        
   
class ICDomainType(Interface):
    """
    Abstract parent of domain specific constrainer types.
    """
    
    standardEquivalent=Object(
        schema=ICComplexObject,
        title=_(u"Standard Equivalent"),
        description=_(u"Standard form of constraint."),
        
    )
class CDomainType(CDefinedObject):
    """
    Abstract parent of domain specific constrainer types.
    """
    
    implements(ICDomainType)
    
    def __init__(self,assumedValue,rmTypeName,occurrences,nodeId,parent):
        CDefinedObject.__init__(assumedValue,rmTypeName,occurrences,nodeId,parent)
    

class ICMultipleAttribute(Interface):
    """
    Abstract model of constraint on any kind of attribute node.
    """
    
    cardinality=Object(
        schema=ICardinality,
        title=_(u"Cardinality"),
        description=_(u"Cardinality of this attribute constraint."),
        
    )

    def members(cobj):
        """
        List of constraints representing members of the container value of this attribute.
        """
         
class CMultipleAttribute(grok.Model):
    """
    Abstract model of constraint on any kind of attribute node.
    """
    
    implements(ICMultipleAttribute)
    
    def __init__(self, cardinality):
        self.cardinality = cardinality
    
    def members(cobj):
        """
        List of constraints representing members of the container value of this attribute.
        """
        return self.children
    
    def cardinalityValidity():
        return self.cardinality != None
    
    def membersValid():
        if (self.children != None):
            for co in self.children:
                if (issubclass(type(co), CObject) and co.occurrences.upper >= 1):
                    return False
            return True
            
        


class IConstraintRef(Interface):
    """
    Reference to a constraint described in the same archetype.
    """
    
    reference=TextLine(
        title=_(u"Reference"),
        description=_(u"Reference to a constraint in the archetype ontology."),
        
    )
  
    
class ConstraintRef(CReferenceObject):
    """
    Reference to a constraint described in the same archetype.
    """
    
    implements(IConstraintRef)
     
class ICPrimitive(Interface):
    """
    Abstract super type of all primitive types.
    """

    defaultValue=Field(
        title=_(u"Default Value"),
        description=_(u"A default value for this constraint object."),

    )

    hasAssumedValue=Bool(
        title=_(u"Has Assumed Value"),
        description=_(u"True if there is an assumed value."),

    )
    
    assumedValue=Field(
        title=_("Assumed Value"),
    )
    

    def validValue(aVal):
        """
        True if aValue is valid with respect to the expressed constraint.
        """
    
class ICPrimitiveObject(Interface):
    """
    Constraint on a primitive object.
    """
    
    anyAllowed=Bool(
        title=_(u"Any Allowed"),
        description=_(u"True if any value of the type being constrained is allowed."),
        
    )
    
    item=Object(
        schema=ICPrimitive,
        title=_(u"Item"),
        description=_(u"Object actually defining the constraint."),
        required=False,
    )
   

class CPrimitiveObject(CDefinedObject):
    """
    Constraint on a primitive object.
    """
    
    implements(ICPrimitiveObject)
    



class ICSingleAttribute(Interface):
    """
    Concrete model of constraint on a single valued attribute.
    """
    
    alternatives=List(
        title=_(u"Alternatives"),
        description=_(u"A list of alternative constraints for the single child of this attribute."),
        required=False,
        value_type=Object(schema=ICObject),
    )

class CSingleAttribute(grok.Model):
    """
    Concrete model of constraint on a single valued attribute.
    """
    
    implements(ICSingleAttribute)
    
    def __init__(self, alternatives):
        self.alternatives = alternatives
    
    def alternativesExists():
        return self.alternatives != None  
    
    


        
class CPrimitive(grok.Model):
    """
    Abstract super type of all primitive types.
    """
    
    implements(ICPrimitive)
    
    def __init__(self,defaultValue,hasAssumedValue,assumedValue):
        self.defaultValue=defaultValue
        self.hasAssumedValue=hasAssumedValue
        self.assumedValue=assumedValue
        

    def validValue(aVal):
        """
        True if aValue is valid with respect to the expressed constraint.
        """

 
class ICBoolean(Interface):
    """
    Boolean constraint.
    """
    
    trueValid=Bool(
        title=_(u"True Valid"),
        description=_(u"True if value True is allowed."),
        
    )
    
    falseValid=Bool(
        title=_(u"False Valid"),
        description=_(u"True if the value False is allowed."),
        
    )
    
    assumedValue=Bool(
        title=_(u"Assumed Value"),
        description=_(u"The value to assume of this item is not included in the data."),
        
    )
    
    
class CBoolean(CPrimitive):
    """
    Boolean constraint.
    """
    
    implements(ICBoolean)
    pass

 

class ICDate(Interface):
    """
    ISO 8601 compatible constraint on instances of Date.
    """
    
    monthValidity=Object(
        schema=IValidityKind,
        title=_(u"Month Validity"),
        description=_(u" "),
        required=False,
    )
    

    dayValidity=Object(
        schema=IValidityKind,
        title=_(u"Day Validity"),
        description=_(u" "),
        required=False,
    )
    
    timezoneValidity=Object(
        schema=IValidityKind,
        title=_(u"Timezone Validity"),
        description=_(u" "),
        required=False,
    )
    """ Interval is not a Zope schema field
    range_=Interval(
        title=_(u"Range"),
        description=_(u"Interval of dates."),
        required=False,
    )
    """
    
    assumedValue=Date(
        title=_(u"Assumed Value"),
        description=_(u" "),
        
    )

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """


class CDate(CPrimitive):
    """
    ISO 8601 compatible constraint on instances of Date.
    """
    
    implements(ICDate)

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """

class ICDateTime(Interface):
    """
    ISO 8601 compatible constraint on instances of DateTime.
    """
    
    monthValidity=Object(
        schema=IValidityKind,
        title=_(u"Month Validity"),
        description=_(u" "),
        required=False,
    )
    

    dayValidity=Object(
        schema=IValidityKind,
        title=_(u"Day Validity"),
        description=_(u" "),
        required=False,
    )
    
    timezoneValidity=Object(
        schema=IValidityKind,
        title=_(u"Timezone Validity"),
        description=_(u" "),
        required=False,
    )
    
    hourValidity=Object(
        schema=IValidityKind,
        title=_(u"Hour Validity"),
        description=_(u" "),
        required=False,
    )

   
    minuteValidity=Object(
        schema=IValidityKind,
        title=_(u"Minute Validity"),
        description=_(u" "),
        required=False,
    )
    

    secondValidity=Object(
        schema=IValidityKind,
        title=_(u"Second Validity"),
        description=_(u" "),
        required=False,
    )
    
    millisecondValidity=Object(
        schema=IValidityKind,
        title=_(u"Millisecond Validity"),
        description=_(u" "),
        required=False,
    )
    
    timezoneValidity=Object(
        schema=IValidityKind,
        title=_(u"Timezone Validity"),
        description=_(u" "),
        required=False,
    )

    """
    range=Interval(
        title=_(u"Range"),
        description=_(u"Interval of times."),
        required=False,
    )
    """
    
    assumedValue=Datetime(
        title=_(u"Assumed Value"),
        description=_(u" "),
        
    )

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """
        
class CDateTime(CPrimitive):
    """
    ISO 8601 compatible constraint on instances of DateTime.
    """
    
    implements(ICDateTime)
    pass
    

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """

class ICDuration(Interface):
    """
    Constraints on durations.  openEHR allows the 'W' indicator to be mixed in.
    """

    yearsAllowed=Bool(
        title=_(u"Years Allowed"),
        description=_(u"True if years are allowed in the constrained duration."),
        required=False,
    )

    monthsAllowed=Bool(
        title=_(u"Months Allowed"),
        description=_(u"True if months are allowed in the constrained duration."),
        required=False,
    )

    weeksAllowed=Bool(
        title=_(u"Weeks Allowed"),
        description=_(u"True if weeks are allowed in the constrained duration."),
        required=False,
    )

    daysAllowed=Bool(
        title=_(u"Days Allowed"),
        description=_(u"True if days are allowed in the constrained duration."),
        required=False,
    )

    hoursAllowed=Bool(
        title=_(u"Hours Allowed"),
        description=_(u"True if hours are allowed in the constrained duration."),
        required=False,
    )

    minutesAllowed=Bool(
        title=_(u"Minutes Allowed"),
        description=_(u"True if minutes are allowed in the constrained duration."),
        required=False,
    )

    secondsAllowed=Bool(
        title=_(u"Seconds Allowed"),
        description=_(u"True if seconds are allowed in the constrained duration."),
        required=False,
    )

    fractionalSecondsAllowed=Bool(
        title=_(u"Fractional Seconds Allowed"),
        description=_(u"True if fractional seconds are allowed in the constrained duration."),
        required=False,
    )

    range=Interval(
        title=_(u"Range"),
        description=_(u"Interval of duration."),
        required=False,
    )


class CDuration(CPrimitive):
    """
    Constraints on durations.  openEHR allows the 'W' indicator to be mixed in.
    """
    
    implements(ICDuration)
    pass

        
class ICInteger(Interface):
    """
    Constraint on integers.
    """
    
    list_=Set(
        title=_(u"List"),
        description=_(u"Set of integers specifying constraints."),
        required=False,
    )
    
    range=Interval(
        title=_(u"Range"),
        description=_(u"Range of integers specifying constraint."),
        required=False,
    )
    
    
    assumedValue=Int(
        title=_(u"Assumed Value"),
        description=_(u"The value to assume if this item is not in the data."),
        
    )
    
   
class CInteger(CPrimitive):
    """
    Constraint on integers.
    """
    
    implements(ICInteger)
    pass

       
class ICReal(Interface):
    """
    Constraints on instances of Real
    """
    
    list_=Set(
        title=_(u"List"),
        description=_(u"Set of Reals specifying constraint"),
        required=False,
    )

   
    range=Interval(
        title=_(u"Range"),
        description=_(u" "),
        required=False,
    )
    
    
    assumedValue=Float(
        title=_(u"Assumed Value"),
        description=_(u""),
        
    )

    
class CReal(CPrimitive):
    """
    Constraints on instances of Real
    """
    
    implements(ICReal)
    pass

      
    
class ICTime(Interface):
    """
    ISO 8601 compatible constraint on instances of Time.
    """
    
    minuteValidity=Object(
        schema=IValidityKind,
        title=_(u"Minute Validity"),
        description=_(u" "),
        required=False,
    )
    

    secondValidity=Object(
        schema=IValidityKind,
        title=_(u"Second Validity"),
        description=_(u" "),
        required=False,
    )
    
    millisecondValidity=Object(
        schema=IValidityKind,
        title=_(u"Millisecond Validity"),
        description=_(u" "),
        required=False,
    )
    
    timezoneValidity=Object(
        schema=IValidityKind,
        title=_(u"Timezone Validity"),
        description=_(u" "),
        required=False,
    )
    
    range=Interval(
        title=_(u"Range"),
        description=_(u"Interval of times."),
        required=False,
    )
    
    assumedValue=Time(
        title=_(u"Assumed Value"),
        description=_(u" "),
        
    )

    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """

class CTime(CPrimitive):
    """
    ISO 8601 compatible constraint on instances of Time.
    """
    
    implements(ICTime)
    pass


    def validityIsRange():
        """
        Returns True if the validity is in the form of a range.
        """


     
        
        
class ArchetypeOntology(grok.Container):
    """
    Local ontology of an archetype.
    """
    
    implements(IArchetypeOntology)
    
    # assign the attributes to their schema definitions
    terminologiesAvailable = FieldProperty(IArchetypeOntology['terminologiesAvailable'])
    specialisationDepth = FieldProperty(IArchetypeOntology['specialisationDepth'])
    termCodes = FieldProperty(IArchetypeOntology['termCodes'])
    constraintCodes = FieldProperty(IArchetypeOntology['constraintCodes'])
    termAttributeNames = FieldProperty(IArchetypeOntology['termAttributeNames'])
    parentArchetype = FieldProperty(IArchetypeOntology['parentArchetype'])
    
    
    
    def hasLanguage(aLang):
        """
        True if aLang is present in ontology.
        """
        
    def hasTerminology(aTermId):
        """
        True if ontology has aTermId, terminology Id.
        """
        
    def hasTermCode(tcode):
        """
        True if tcode is in termCodes.
        """
        
    def hasConstraintCode(ccode):
        """
        True if ccode is in constraintCodes.
        """
        
    def constraintDefinition(aLang,aCode):
        """
        Constraint definition for aCode expressed in aLang.
        """
        
    def termBinding(aTermId,aCode):
        """
        Return a CodePhrase for aCode in aTermId.
        """
        
    def constraintBinding(aTermId,aCode):
        """
        Return a string that describes the constraint aCode in aTermId usually in the form of a query expression.
        """
        
class IArchetypeTerm(Interface):
    """
    Representation of any coded entity in the archetype ontology.
    """
    
    code=TextLine(
        title=_(u"Code"),
        description=_(u"Code of this term."),
        
    )

    items=Dict(
        title=_(u"Items"),
        description=_(u"Hash of keys (text,description) and corresponding values."),
        required=False,
        key_type=TextLine(),
        value_type=TextLine(),
    )
    
    def keys(set):
        """
        List of all keys used in this term.
        """
 
class ArchetypeTerm(grok.Model):
    """
    Representation of any coded entity in the archetype ontology.
    """
    
    implements(IArchetypeTerm)
    
    def __init__(self,code,items):
        self.code=code
        self.items=items
    
    def keys(set):
        """
        List of all keys used in this term.
        """
        
        return self.items.keys()
        
        
#Begin Template package


