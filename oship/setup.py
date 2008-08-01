from setuptools import setup, find_packages

setup(name='oship',

      # Fill in project info below
      version='1.0.1a1',
      description="oship",
      long_description="Open Source Helth Information Platform",
      keywords='',
      author='Timothy W. Cook',
      author_email='timothywayne.cook@gmail.com',
      url='',
      license='',
      # Get more from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Environment :: Web Environment',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                   'Framework :: Zope3',
                   ],

      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'ZODB3',
                        'ZConfig',
                        'zdaemon',
                        'zope.publisher',
                        'zope.traversing',
                        'zope.app.wsgi>=3.4.0',
                        'zope.app.appsetup',
                        'zope.app.zcmlfiles',
                        # The following packages aren't needed from the
                        # beginning, but end up being used in most apps
                        'zope.annotation',
                        'zope.copypastemove',
                        'zope.formlib',
                        'zope.i18n',
                        'zope.app.authentication',
                        'zope.app.session',
                        'zope.app.intid',
                        'zope.app.keyreference',
                        'zope.app.catalog',
                        # The following packages are needed for functional
                        # tests only
                        'zope.testing',
                        'zope.app.testing',
                        'zope.app.securitypolicy',
                        'z3c.form',
                        'z3c.formui',
                        'z3c.layer'
                        ],
      entry_points = """
      [console_scripts]
      oship-debug = oship.startup:interactive_debug_prompt
      oship-ctl = oship.startup:zdaemon_controller
      [paste.app_factory]
      main = oship.startup:application_factory
      """
      )
