#!/home/tim/projects/bin/python
import sys
    
sys.path[0:0] = [
  '/home/tim/projects/oship/src',
  '/home/tim/buildout-eggs/z3c.evalexception-2.0-py2.4.egg',
  '/home/tim/buildout-eggs/Paste-1.7-py2.4.egg',
  '/home/tim/buildout-eggs/setuptools-0.6c7-py2.4.egg',
  '/home/tim/buildout-eggs/PasteScript-1.6.2-py2.4.egg',
  '/home/tim/buildout-eggs/PasteDeploy-1.3.1-py2.4.egg',
  '/home/tim/buildout-eggs/mglob-0.4-py2.4.egg',
  '/home/tim/buildout-eggs/pyparsing-1.4.11-py2.4.egg',
  '/home/tim/buildout-eggs/RestrictedPython-3.4.2-py2.4.egg',
  '/home/tim/buildout-eggs/ZConfig-2.5.1-py2.4.egg',
  '/home/tim/buildout-eggs/ZODB3-3.8.0-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/jquery.javascript-1.0.0-py2.4.egg',
  '/home/tim/buildout-eggs/jquery.layer-1.0.0-py2.4.egg',
  '/home/tim/buildout-eggs/lxml-1.3.6-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/z3c.coverage-1.1.1-py2.4.egg/z3c/coverage',
  '/home/tim/buildout-eggs/z3c.csvvocabulary-1.0.0-py2.4.egg/z3c/csvvocabulary',
  '/home/tim/buildout-eggs/z3c.etestbrowser-1.0.4-py2.4.egg/z3c/etestbrowser',
  '/home/tim/buildout-eggs/z3c.form-1.8.2-py2.4.egg/z3c/form',
  '/home/tim/buildout-eggs/z3c.formdemo-1.5.1-py2.4.egg/z3c/formdemo',
  '/home/tim/buildout-eggs/z3c.formjs-0.3.0-py2.4.egg/z3c/formjs',
  '/home/tim/buildout-eggs/z3c.formjsdemo-0.3.0-py2.4.egg/z3c/formjsdemo',
  '/home/tim/buildout-eggs/z3c.formui-1.4.1-py2.4.egg/z3c/formui',
  '/home/tim/buildout-eggs/z3c.i18n-0.1.1-py2.4.egg/z3c/i18n',
  '/home/tim/buildout-eggs/z3c.layer-0.2.3-py2.4.egg/z3c/layer',
  '/home/tim/buildout-eggs/z3c.macro-1.1.0-py2.4.egg/z3c/macro',
  '/home/tim/buildout-eggs/z3c.macroviewlet-1.0.0-py2.4.egg/z3c/macroviewlet',
  '/home/tim/buildout-eggs/z3c.menu-0.2.0-py2.4.egg/z3c/menu',
  '/home/tim/buildout-eggs/z3c.optionstorage-1.0.4-py2.4.egg/z3c/optionstorage',
  '/home/tim/buildout-eggs/z3c.pagelet-1.0.2-py2.4.egg/z3c/pagelet',
  '/home/tim/buildout-eggs/z3c.rml-0.7.3-py2.4.egg/z3c/rml',
  '/home/tim/buildout-eggs/z3c.skin.pagelet-1.0.2-py2.4.egg/z3c/skin/pagelet',
  '/home/tim/buildout-eggs/z3c.template-1.1-py2.4.egg/z3c/template',
  '/home/tim/buildout-eggs/z3c.testing-0.2.0-py2.4.egg/z3c/testing',
  '/home/tim/buildout-eggs/z3c.traverser-0.2.1-py2.4.egg/z3c/traverser',
  '/home/tim/buildout-eggs/z3c.viewlet-1.0.0-py2.4.egg/z3c/viewlet',
  '/home/tim/buildout-eggs/z3c.viewtemplate-0.3.2-py2.4.egg/z3c/viewtemplate',
  '/home/tim/buildout-eggs/z3c.zrtresource-1.0.1-py2.4.egg/z3c/zrtresource',
  '/home/tim/buildout-eggs/zc.catalog-1.2.0-py2.4.egg',
  '/home/tim/buildout-eggs/zc.datetimewidget-0.5.2-py2.4.egg',
  '/home/tim/buildout-eggs/zc.i18n-0.5.2-py2.4.egg',
  '/home/tim/buildout-eggs/zc.recipe.filestorage-1.0.0-py2.4.egg',
  '/home/tim/buildout-eggs/zc.recipe.testrunner-1.0.0-py2.4.egg',
  '/home/tim/buildout-eggs/zc.resourcelibrary-0.8.2-py2.4.egg',
  '/home/tim/buildout-eggs/zc.table-0.6-py2.4.egg',
  '/home/tim/buildout-eggs/zc.zope3recipes-0.6.1-py2.4.egg',
  '/home/tim/buildout-eggs/zdaemon-2.0.1-py2.4.egg',
  '/home/tim/buildout-eggs/zodbcode-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.annotation-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.annotation-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.apidoc-3.4.3-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.applicationcontrol-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.appsetup-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.authentication-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.basicskin-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.boston-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.broken-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.cache-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.catalog-3.5.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.component-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.container-3.5.3-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/zope.app.content-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.dav-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.debug-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.debugskin-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.dependable-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.dtmlpage-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.error-3.5.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.exception-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.externaleditor-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.file-3.4.2-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.folder-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.form-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.ftp-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.generations-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.homefolder-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.http-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.i18n-3.4.4-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.i18nfile-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.interface-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.interpreter-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.intid-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.keyreference-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.layers-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.locales-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.locking-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.module-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.onlinehelp-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.pagetemplate-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.pluggableauth-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.preference-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.preview-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.principalannotation-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.publication-3.4.3-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.publisher-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.pythonpage-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.renderer-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.rotterdam-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.schema-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.security-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.securitypolicy-3.4.6-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.server-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.session-3.5.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.skins-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.sqlscript-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.testing-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.traversing-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.tree-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.twisted-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.undo-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.wfmc-0.1.2-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.workflow-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.wsgi-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.xmlrpcintrospection-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.zapi-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.zcmlfiles-3.4.3-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.zopeappgenerations-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.app.zptpage-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.cachedescriptors-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.component-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.configuration-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.contentprovider-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.contenttype-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.copypastemove-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.datetime-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.decorator-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.deferredimport-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.deprecation-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.documenttemplate-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.dottedname-3.4.2-py2.4.egg',
  '/home/tim/buildout-eggs/zope.dublincore-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.error-3.5.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.event-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.exceptions-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.file-0.3.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.filerepresentation-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.formlib-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.hookable-3.4.0-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/zope.html-1.0.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.i18n-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.i18nmessageid-3.4.3-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/zope.index-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.interface-3.4.1-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/zope.lifecycleevent-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.location-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.mimetype-0.3.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.minmax-1.1.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.modulealias-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.pagetemplate-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.proxy-3.4.0-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/zope.publisher-3.4.2-py2.4.egg',
  '/home/tim/buildout-eggs/zope.rdb-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.schema-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.security-3.4.0-py2.4-linux-x86_64.egg',
  '/home/tim/buildout-eggs/zope.securitypolicy-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.sendmail-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.sequencesort-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.server-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.session-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.size-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.structuredtext-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.tal-3.4.1-py2.4.egg',
  '/home/tim/buildout-eggs/zope.tales-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.testbrowser-3.4.2-py2.4.egg',
  '/home/tim/buildout-eggs/zope.testrecorder-0.3.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.thread-3.4-py2.4.egg',
  '/home/tim/buildout-eggs/zope.traversing-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.viewlet-3.4.2-py2.4.egg',
  '/home/tim/buildout-eggs/zope.wfmc-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/zope.xmlpickle-3.4.0-py2.4.egg',
  '/home/tim/buildout-eggs/ClientForm-0.2.7-py2.4.egg',
  '/home/tim/buildout-eggs/mechanize-0.1.7b-py2.4.egg',
  '/home/tim/buildout-eggs/pytz-2007k-py2.4.egg',
  '/home/tim/buildout-eggs/zope.testing-3.5.1-py2.4.egg',
  '/home/tim/buildout-eggs/docutils-0.4-py2.4.egg',
  '/home/tim/buildout-eggs/zc.recipe.egg-1.0.0-py2.4.egg',
  '/home/tim/buildout-eggs/zc.buildout-1.0.0-py2.4.egg',
  '/home/tim/buildout-eggs/pyPdf-1.11-py2.4.egg',
  ]

