from setuptools import setup, find_packages

version = '1.0.1a2'

setup(name='oship',
      version=version,
      description="OSHIP",
      long_description="""Open Source Health Information Platform""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], 
      keywords="healthcare EMR EHR openEHR",
      author="Timothy Cook & Contributors",
      author_email="",
      url="",
      license="MPL",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'grokui.admin',
                        'z3c.testsetup',
                        'pyparsing',
                        'mglob',
                        # Add extra requirements here
                        ],
      entry_points = """
      [console_scripts]
      oship-debug = oship.startup:interactive_debug_prompt
      oship-ctl = oship.startup:zdaemon_controller
      [paste.app_factory]
      main = oship.startup:application_factory
      """,
      )
