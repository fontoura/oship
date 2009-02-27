from setuptools import setup, find_packages

version = '0.0'

setup(name='oship',
      version=version,
      description="",
      long_description="""\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], 
      keywords="",
      author="",
      author_email="",
      url="",
      license="",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'grokui.admin',
                        'z3c.testsetup',
                        # Add extra requirements here
                        'pyparsing',
                        'mglob'
                        ],
      entry_points = """
      [console_scripts]
      oship-debug = oship.startup:interactive_debug_prompt
      oship-ctl = oship.startup:zdaemon_controller
      [paste.app_factory]
      main = oship.startup:application_factory
      """,
      )
