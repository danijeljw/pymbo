import sys


try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup


if sys.version_info <= (2, 4):
  error = 'Requires Python Version 3.6 or above... exiting.'
  print >> sys.stderr, error
  sys.exit(1)


requirements = [
    'requests>=2.11.1,<3.0',
]

setup(name='pymbo',
      version='0.1.0-dev',
      description='Python Messenger Bot made simple',
      scripts=[],
      url='https://danijeljw.github.io/pymbo/',
      packages=['pymbo'],
      license='MIT,
      platforms='Posix; MacOS X; Windows; Linux',
      setup_requires=requirements,
      install_requires=requirements,
      classifiers=['Development Status :: 1 - Development',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Internet',
                   ]
      )

