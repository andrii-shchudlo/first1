
from setuptools import setup, find_packages


setup(name='two',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['setuptools'],

      entry_points="""\
      [paste.filter_factory]
      main = two:main
      """,
)
