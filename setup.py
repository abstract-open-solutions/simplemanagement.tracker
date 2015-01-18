from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='simplemanagement.tracker',
      version=version,
      description="Simplemanagement Tracker customizations",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
      ],
      keywords='plone project management',
      author='Simone Orsi',
      author_email='simone.orsi@abstract.it',
      url='https://github.com/abstract-open-solutions/simplemanagement.tracker',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['simplemanagement'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.api',
          'collective.simplemanagement',
          'plone.app.referenceablebehavior',
          'Products.Poi',
          'archetypes.schemaextender',
          'archetypes.referencebrowserwidget',
          'z3c.jbot',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
