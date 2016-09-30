from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'deform>=2.0a2',
    'pyramid_sqlalchemy',
    'pyramid_tm'
]
setup(name='mysite',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = mysite:main
      """
      )
