# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2007, Timothy W. Cook and Contributors. All rights reserved.
# Redistribution and use are governed by the license in OSHIP-LICENSE.txt
#
# Use and/or redistribution of this file assumes you have read and accepted the
# terms of the license.
##############################################################################


"""
Returns a string to atbldr for the Python classnames and parameters in the definition section.
"""


__author__  = u'Timothy Cook <timothywayne.cook@gmail.com>'
__docformat__ = u'plaintext'
__contributors__ = u'<name> <email address>'


def getClassName(keyword):
    u"""
    Map all of the ADL class workds to OSHIP classes and parameters.
    """

    definClassMap={'SECTION':'Section(items,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'COMPOSITION':'Composition(content,context,composer,category,lang,terr,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'OBSERVATION':'Observation(data,state,nodeid,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,atnodeid,name,atdetails,fdraudit,links)',\
                   'ITEM_SINGLE':'ItemSingle(item)',\
                   'ITEM_LIST':'ItemList(items)',\
                   'ITEM_TREE':'ItemTree(uid,nodeid,name, atdetails, fdraudit, links, items)',\
                   'ADMIN_ENTRY':'AdminEntry(data,lang,encod,subject,provider,opart,wfid,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'ACTION':'Action(time,desc,ism,inst,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'EVALUATION':'Evaluation(data,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'INSTRUCTION':'Instruction(narr,act,exp,wfd,nodeid,protocol,gid,lang,encod,subject,provider,opart,wfid,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'ELEMENT':'Element(value,nullFlavor,nodeid,uid,name,atdetails,fdraudit,links)',\
                   'CLUSTER':'Cluster(uid,nodeid,name,archetypeDetails,feederAudit,links,items)',\
                   'EVENT':'Event(time,data,state,parent,offset)',\
                   'ADDRESS':'Address()',\
                   'DV_CODED_TEXT':'DvCodedText(definingCode,value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)',\
                   'DV_TEXT':'DvText(value,mappings=None,formatting=None,hyperlink=None,language=None,encoding=None)',\
                   'INTERVAL_EVENT':'IntervalEvent(width,mfunc,scount)',\
                   'DV_DURATION':'DvDuration(value)',\
                   'POINT_EVENT':'PointEvent(time,data,state,parent,offset)',\
                   'C_DV_QUANTITY':'CDvQuantity(list,property)',\
                   'HISTORY':'History(origin,events,period,duration,summary,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'DV_DATE_TIME':'DvDateTime(value)',\
                   'DV_COUNT':'DvCount(magnitude,accuracy,accuracyIsPercent,magnitudeStatus,normalStatus,normalRange,otherReferenceRanges)',\
                   'DV_MULTIMEDIA':'DvMultimedia(altTxt,mType,compAlg,intChk,intChkAlg,tnail,uri,data)',\
                   'DV_BOOLEAN':'DvBoolean(value)',\
                   'PARTY_RELATED':'PartyRelated(relationship)',\
                   'DV_INTERVAL':'DvInterval(lower,upper,lower_included,upper_included)',\
                   'DV_INTERVAL<DV_DATE_TIME>':'DvInterval(lower,upper,lower_included,upper_included)',\
                   'DV_INTERVAL<DV_QUANTITY>':'DvInterval(lower,upper,lower_included,upper_included)',\
                   'DV_INTERVAL<QUANTITY>':'DvInterval(lower,upper,lower_included,upper_included)',\
                   'DV_INTERVAL<DV_COUNT>':'DvInterval(lower,upper,lower_included,upper_included)',\
                   'DV_INTERVAL<COUNT>':'DvInterval(lower,upper,lower_included,upper_included)',\
                   'DV_DATE':'DvDate(value)',\
                   'DV_URI':'DvUri(value)',\
                   'DV_PROPORTION':'DvProportion(numerator,denominator,type,precision)',\
                   'ISM_TRANSITION':'IsmTransition(cstate,trans,cfs)',\
                   'ACTIVITY':'Activity(descr,tim,atid,nodeid,uid,nodeid,name,atdetails,fdraudit,links)',\
                   'EVENT_CONTEXT':'EventContext(hcf,start,end,part,loc,sett,other)',\
                   'PARTICIPATION':'Participation(performer,function,mode,time)',\
                   'ITEM_TABLE':'ItemTable(rows)',\
                   }



    if definClassMap.has_key(keyword):
        return definClassMap[keyword]
    else:
        return None

