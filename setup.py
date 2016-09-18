#!/usr/bin/env python
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# explicitly config
test_args = [
    '--cov-report=term',
    '--cov-report=html',
    '--cov=lib',
    'test'
]


class PyTest(TestCommand):
  user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

  def initialize_options(self):
    TestCommand.initialize_options(self)
    self.pytest_args = test_args

  def run_tests(self):
    # import here, cause outside the eggs aren't loaded
    import pytest
    errno = pytest.main(self.pytest_args)
    sys.exit(errno)


setup(name='farming',
      version='1.0.0',
      description='Two engineers decide to become farmers',
      packages=find_packages(),
      test_suite='tests',
      cmdclass={'test': PyTest}
      )
