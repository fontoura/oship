from setuptools import setup, find_packages

version = '1.0-oshipdemo'

setup(name='oship',
    version=version,
    description="Open Source Health Information Platform",
    long_description=""" A Python implementation of the openEHR information model.\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], 
      keywords="health medical informatics Python healthcare",
      author="Timothy W. Cook & contributors",
      author_email="timothywayne.cook@gmail.com",
      url="http://launchpad.net/oship",
      license="MPL1.1 tri-license",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'grokui.admin',
                        'z3c.testsetup',
                        'grokcore.startup',
                        # Add extra requirements here
                        'pyparsing',
                        'mglob',
                        'hurry.workflow',
                        'megrok.kss' 
                        ],
      entry_points = """
      [console_scripts]
      oship-debug = grokcore.startup:interactive_debug_prompt
      oship-ctl = grokcore.startup:zdaemon_controller
      [paste.app_factory]
      main = grokcore.startup:application_factory
      """,
      )
