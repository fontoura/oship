#!/home/tim/oship-openehr/bin/python

import sys
sys.path[0:0] = [
  '/home/tim/oship-openehr/oship/oship',
  '/home/tim/.buildout/eggs/z3c.evalexception-2.0-py2.5.egg',
  '/home/tim/.buildout/eggs/Paste-1.7.1-py2.5.egg',
  '/home/tim/.buildout/eggs/setuptools-0.6c8-py2.5.egg',
  '/home/tim/.buildout/eggs/PasteScript-1.6.3-py2.5.egg',
  '/home/tim/.buildout/eggs/PasteDeploy-1.3.2-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.security-3.4.1-py2.5-linux-x86_64.egg',
  '/home/tim/.buildout/eggs/mglob-0.4-py2.5.egg',
  '/home/tim/.buildout/eggs/pyparsing-1.5.0-py2.5.egg',
  '/home/tim/.buildout/eggs/z3c.testsetup-0.2.1-py2.5.egg',
  '/home/tim/.buildout/eggs/grokui.admin-0.1.2-py2.5.egg',
  '/home/tim/.buildout/eggs/grok-1.0a1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.schema-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.proxy-3.4.2-py2.5-linux-x86_64.egg',
  '/home/tim/.buildout/eggs/zope.location-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.interface-3.4.1-py2.5-linux-x86_64.egg',
  '/home/tim/.buildout/eggs/zope.i18nmessageid-3.4.3-py2.5-linux-x86_64.egg',
  '/home/tim/.buildout/eggs/zope.exceptions-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.deferredimport-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.configuration-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.component-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/pytz-2007k-py2.5.egg',
  '/home/tim/.buildout/eggs/martian-0.11-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.testing-3.4.3-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.testing-3.5.4-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.session-3.5.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.securitypolicy-3.4.6-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.error-3.5.1-py2.5.egg',
  '/home/tim/.buildout/eggs/z3c.autoinclude-0.2.2-py2.5.egg',
  '/home/tim/.buildout/eggs/z3c.flashmessage-1.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zc.catalog-1.2.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.viewlet-3.4.2-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.testbrowser-3.4.2-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.traversing-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.securitypolicy-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.publisher-3.4.6-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.pagetemplate-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.lifecycleevent-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.hookable-3.4.0-py2.5-linux-x86_64.egg',
  '/home/tim/.buildout/eggs/zope.formlib-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.event-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.deprecation-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.dottedname-3.4.2-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.zcmlfiles-3.4.3-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.twisted-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.security-3.5.2-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.renderer-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.publisher-3.5.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.publication-3.4.3-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.pagetemplate-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.keyreference-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.intid-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.folder-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.container-3.5.6-py2.5-linux-x86_64.egg',
  '/home/tim/.buildout/eggs/zope.app.component-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.catalog-3.5.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.authentication-3.4.3-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.appsetup-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.applicationcontrol-3.4.3-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.apidoc-3.4.3-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.annotation-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/ZODB3-3.8.0-py2.5-linux-x86_64.egg',
  '/home/tim/.buildout/eggs/simplejson-1.7.1-py2.5.egg',
  '/home/tim/.buildout/eggs/grokcore.viewlet-1.0-py2.5.egg',
  '/home/tim/.buildout/eggs/grokcore.view-1.2.1-py2.5.egg',
  '/home/tim/.buildout/eggs/grokcore.security-1.0-py2.5.egg',
  '/home/tim/.buildout/eggs/grokcore.formlib-1.1-py2.5.egg',
  '/home/tim/.buildout/eggs/grokcore.component-1.5.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.i18n-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.dependable-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.debug-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.session-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.minmax-1.1.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.http-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.form-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.error-3.5.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zc.buildout-1.0.6-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.contentprovider-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/ClientForm-0.2.9-py2.5.egg',
  '/home/tim/.buildout/eggs/mechanize-0.1.7b-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.tal-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.tales-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.schema-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.wsgi-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.rotterdam-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.basicskin-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.principalannotation-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.zopeappgenerations-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.locales-3.4.5-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.i18n-3.4.4-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.interface-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.generations-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.content-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.modulealias-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.zapi-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.server-3.4.2-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.copypastemove-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zdaemon-2.0.2-py2.5.egg',
  '/home/tim/.buildout/eggs/ZConfig-2.5.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.structuredtext-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/docutils-0.4-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.datetime-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.contenttype-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.exception-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.size-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.dublincore-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.broken-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.filerepresentation-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.cachedescriptors-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.thread-3.4-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.index-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.tree-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.skins-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.preference-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.onlinehelp-3.4.1-py2.5.egg',
  '/home/tim/.buildout/eggs/zodbcode-3.4.0-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.server-3.4.3-py2.5.egg',
  '/home/tim/.buildout/eggs/RestrictedPython-3.4.2-py2.5.egg',
  '/home/tim/.buildout/eggs/zope.app.file-3.4.4-py2.5.egg',
  ]

from atbldr import CreateAT
CreateAT()
