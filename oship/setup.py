from setuptools import setup, find_packages

version = '1.0.1-1a1dev'

setup(name='oship',
      version=version,
      description="Open Source Health Information Platform",
      long_description="""\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords="healthcare grok zope oship",
      author="Timothy W. Cook",
      author_email="timothywayne.cook@gmail.com",
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
                        # Add extra requirements here
                        ],
      entry_points="""
      # Add entry points here
      """,
      )
