'''
monster
-----

monster is a python general template framework for new project,
you can fastly build yourself projects.and before you know: It's MIT licensed!

some tips:
  1. setup setuptools tool
  2. run pip requirements.txt, setup the required modules
  3. others
 
'''

import codecs
from setuptools import setup,find_packages
from setuptools.command.test import test as TestCommand
import os
import sys
import re
import ast

HERE = os.path.abspath(os.path.dirname(__file__))

_version_re = re.compile(r'__version__\s+=\s+(.*)')

class RunTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

def read(*parts):             
    return codecs.open(os.path.join(HERE, *parts), 'r').read()

monster_version = str(ast.literal_eval(_version_re.search(read("monster/__init__.py")).group(1)))

'''str(read('README.md'))'''
long_description = 'faf'

setup(
    name='monster',
    version=monster_version,
    url='https://github.com/haomiao/monster',
    author='colper',
    author_email='635541412@qq.com',
    description='a python general template framework for new project',
    long_description=long_description,
    license='MIT',
    packages=['monster'],
    include_package_data=True,
    #package_data={}
    zip_safe=False,
    platforms='any',
    cmdclass={'test': RunTest},
    tests_require=['pytest','nose'],
    #install_requires=['pytest'],
    #entry_points={}
    extras_require={
        'testing': ['pytest'],
      },
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)

