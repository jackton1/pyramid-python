#!/usr/bin/env python

from distutils.core import setup

requires = [
    'pyramid',
    'pyramid_jinja2'
]
setup(name='MySite',
      version='1.0.1',
      install_requires=requires,
      description='Simple Web Application',
      author='Tonye Jack',
      author_email='jtonye@ymail.com',
      entry_points="""\
            [paste.app_factory]
            main = mysite:main
            """
     )
